import json
import os
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient

# 加载环境变量
load_dotenv()

api_key = os.getenv("API_KEY")

class ModelRegistry:
    """
    管理多个模型客户端：
    - 从 llm_config_list.json 读取 {model, api_key, api_base/base_url, name}
    - 若未提供 api_key，则回退到环境变量 OPENAI_API_KEY
    - 暴露按名称/模型获取客户端的方法
    """

    def __init__(self, config_path: str = "llm_config_list.json") -> None:
        self._entries: List[Dict[str, Any]] = []
        self._name_to_entry: Dict[str, Dict[str, Any]] = {}
        self._model_to_entries: Dict[str, List[Dict[str, Any]]] = {}
        self._load(config_path)

    def _load(self, config_path: str) -> None:
        if not os.path.exists(config_path):
            entry = {
                "name": "openai_default",
                "model": "gpt-4o-mini",
                "client": OpenAIChatCompletionClient(
                    model="gpt-4o-mini",
                    api_key=api_key
                    ),
            }
            self._entries = [entry]
            self._name_to_entry[entry["name"]] = entry
            self._model_to_entries.setdefault(entry["model"], []).append(entry)
            return

        with open(config_path, "r", encoding="utf-8") as f:
            cfg_list = json.load(f)

        for idx, cfg in enumerate(cfg_list):
            model = cfg.get("model") or "gpt-4o-mini"
            base_url = cfg.get("api_base") or cfg.get("base_url")
            name_raw = cfg.get("name") or f"client_{idx}_{model}"
            model_info = cfg.get("model_info")
            temperature = cfg.get("temperature")
            # 确保可作为 Python identifier 的名称
            name = name_raw.replace("-", "_").replace(" ", "_")
            if not (name[0].isalpha() or name[0] == "_"):
                name = f"m_{name}"

            client_kwargs = {"model": model, "api_key": api_key}
            if base_url:
                client_kwargs["base_url"] = base_url
            if temperature is not None:
                client_kwargs["temperature"] = temperature
            
            # Always provide model_info for non-standard models
            if model_info:
                client_kwargs["model_info"] = model_info
            
            try:
                entry = {
                    "name": name,
                    "model": model,
                    "client": OpenAIChatCompletionClient(**client_kwargs),
                }
                self._entries.append(entry)
                self._name_to_entry[name] = entry
                self._model_to_entries.setdefault(model, []).append(entry)
            except Exception as e:
                print(f"Warning: Failed to create client for model {model}: {e}")
                # Skip this model and continue with others
                continue

        if not self._entries:
            entry = {
                "name": "openai_default",
                "model": "gpt-4o-mini",
                "client": OpenAIChatCompletionClient(
                    model="gpt-4o-mini", api_key=api_key, temperature=0
                ),
            }
            self._entries = [entry]
            self._name_to_entry[entry["name"]] = entry
            self._model_to_entries.setdefault(entry["model"], []).append(entry)

    def get(self, name_or_model: Optional[str] = None) -> Dict[str, Any]:
        if not name_or_model:
            return self._entries[0]
        if name_or_model in self._name_to_entry:
            return self._name_to_entry[name_or_model]
        if name_or_model in self._model_to_entries:
            return self._model_to_entries[name_or_model][0]
        return self._entries[0]
