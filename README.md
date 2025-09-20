Information:
This repo currently supports experiments on 2 parallel tools and 2 sequential tools scenario. It should work fine on the 1 tool scenario, but I have not tested the case so far.

Attention:
The structure of the json tasks has changed!!! Please check the latest structure in configs and apply this structure for your data.
When adding your tasks, please put them into the corresponding json files.
Deduplicate before adding your servers (in the tools folder).

Instruction:
Construct your env using requirements.txt.
Add your servers.
Add your tasks.
Add your api in configs/config.json.
To run an experiment, simply go to runbenchmark.py. The first para is the model you are going to test, and the second para is the type of task for assessment, i.e. sequential/parallel.
The log file will be saved in the folder logs, and it will contain the reponses from the agent; The results will be saved in the folder results, and it will contain the agent performance. You will also see an output in terminal specifying details of the experiment results.

Plan to do:
Further polish the codes.
Fix potential bugs (I do not know why my gpt-4o test result this time is far worse than previous test results (yet still reasonable). This result is current stored in the logs and results folder. I will look into it later.)
If you encounter any difficulties in setup, please do not hesitate to contact me. And please share with me any ideas on how to improve the coding, I am more than grateful.

**Remember to change the max_tool_iterations para in the "assistant agent" in agenttest.py to the exact number of tools involved in your test tasks**