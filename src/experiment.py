from .utilities import *
from .evaluate import *
from .config import *
from .agenttest import *
import os
import datetime


def get_experiment_config(model, tasks_type):
    """
    Get the experiment configuration.

    Args:
        model: The model to test.
        tasks_type: The type of tasks to test. Support daily tasks (day), professional tasks (pro), and all combined tasks (general_test).

    Returns:
        log_path: The path to the log file.
        task_path: The path to the task file.
        output_path: The path to the result file.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    model = model.replace("/", "_")
    if tasks_type == "day":
        log_path = f"logs/{model}_response_day_{timestamp}.json"
        task_path = "data/daytasks.json"
        output_path = f"results/{model}_results_day_{timestamp}.json"

    elif tasks_type == "pro":
        log_path = f"logs/{model}_response_pro_{timestamp}.json"
        task_path = "data/protasks.json"
        output_path = f"results/{model}_results_pro_{timestamp}.json"
    
    elif tasks_type == "general_test":
        log_path = f"logs/{model}_response_general_test_{timestamp}.json"
        task_path = "data/tasks.json"
        output_path = f"results/{model}_results_general_test_{timestamp}.json"

    return log_path, task_path, output_path


async def run_experiment(model, tasks_type, concurrency=10, num_servers=10):
    """
    Run the benchmark.

    Args:
        model: The model to test.
        tasks_type: The type of tasks to test.
        concurrency: The number of concurrent requests to send.
        num_servers: The number of servers for agent construction.
    """

    scores = []
    detailed_results = []
    tools_summed_up = []

    log_path, task_path, output_path = get_experiment_config(model, tasks_type)
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)
    # Generate responses
    await generate_responses_concurrent(model, task_path, log_path, concurrency, num_servers)

    task_data = load_data(task_path)
    response_data = load_data(log_path)
    num_tasks = len(task_data)
    num_empty_responses = 0
    num_success_tasks = 0

    for i in range(num_tasks):
        
        response = response_data[i]
        task = task_data[i]
        
        # Extract expected tools and inputs
        expected_tools = task.get('tools', [])
        expected_inputs = task.get('inputs', [])
        num_expected_tools = len(list(flatten(expected_tools)))
        tools_summed_up.append(num_expected_tools)
        # assert num_expected_tools == int(task.get('id')[8])

        try:
            tools_used, inputs_used = extract_tools_and_inputs(response)
            if not tools_used:
                num_empty_responses += 1

            # Evaluate performance
            score = evaluate_task_performance(response, expected_tools, expected_inputs, num_expected_tools)

            scores.append(score)
            if score == num_expected_tools:
                num_success_tasks += 1
        except Exception as e:
            print(f"Error evaluating task {i+1}: {str(e)}")
            scores.append(0)
            tools_used, inputs_used = [], []

        # Store detailed results
        result = {
            'task_id': task.get('id', f'task_{i+1}'),
            'task_content': task.get('content', '')[:100] + '...' if len(task.get('content', '')) > 100 else task.get('content', ''),
            'expected_tools': expected_tools,
            'expected_inputs': expected_inputs,
            'tools_used': tools_used,
            'inputs_used': inputs_used,
            'score': score,
            'match': score == num_expected_tools,
            'index': i+1
        }
        detailed_results.append(result)
        
        # Print result for this task
        status = "✅ PASS" if score == num_expected_tools else "❌ FAIL"
        print(f"Task {i+1:2d}: {status}")

    # Calculate overall performance
    full_marks = sum(tools_summed_up)
    total_score = sum(scores)
    model_score = total_score / full_marks if scores else 0
    model_score = round(model_score * 100, 2)

    total_prompt_tokens, total_completion_tokens = calculate_total_tokens(response_data)
    total_tokens = total_prompt_tokens + total_completion_tokens
    average_tokens = total_tokens / (len(response_data) - num_empty_responses)

    average_time = calculate_total_time(response_data)
    average_time = average_time / (len(response_data) - num_empty_responses)
    
    # Print summary
    print("\n" + "=" * 50)
    print("📈 EVALUATION SUMMARY")
    print("=" * 50)
    print(f"Total Tasks Evaluated: {len(scores)}")
    print(f"Tasks Passed: {num_success_tasks}")
    print(f"Tasks Failed: {len(scores) - num_success_tasks}")
    print(f"Model Score: {model_score}")
    print(f"full marks: {full_marks}")

    # Show passed tasks summary
    passed_tasks = [r for r in detailed_results if r['match']]
    if passed_tasks:
        print(f"✅ PASSED TASKS ({len(passed_tasks)}):")
        print("-" * 50)
        for task in passed_tasks:
            print(f"Task ID: {task['task_id']} - Tools: {task['expected_tools']}")
    
    # Save detailed results to file
    evaluation_summary = {
        'total_tasks': len(scores),
        'tasks_passed': num_success_tasks,
        'tasks_failed': len(scores) - num_success_tasks,
        'model_score': model_score,
        'average_tokens': average_tokens,
        'average_time': average_time
    }

    results_summary = {
        'evaluation_summary': evaluation_summary,
        'detailed_results': detailed_results
    }
    
    os.makedirs("results", exist_ok=True)
    save_data(output_path, results_summary)
    
    print(f"\n💾 Detailed results saved to '{output_path}'")
    
    return model_score
