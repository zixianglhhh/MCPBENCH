from .utilities import *
from .evaluate import *
from .config import *
from .agenttest import *
import asyncio
import os
import json
import datetime


def get_experiment_config(model, tasks_type):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    model = model.replace("/", "_")
    if tasks_type == "sequential":
        log_path = f"logs/{model}_response_sequential_{timestamp}.json"
        task_path = "data/tasks_with_2_sequential_tools.json"
        output_path = f"results/{model}_results_sequential_{timestamp}.json"

    elif tasks_type == "parallel":
        log_path = f"logs/{model}_response_parallel_{timestamp}.json"
        task_path = "data/tasks_with_2_parallel_tools.json"
        output_path = f"results/{model}_results_parallel_{timestamp}.json"

    elif tasks_type == "3_tools":
        log_path = f"logs/{model}_response_3_tools_{timestamp}.json"
        task_path = "data/tasks_with_3_tools.json"
        output_path = f"results/{model}_results_3_tools_{timestamp}.json"

    return log_path, task_path, output_path


async def run_experiment(model, tasks_type, num):

    scores = []
    detailed_results = []

    log_path, task_path, output_path = get_experiment_config(model, tasks_type)
        # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)
    await generate_response(model, task_path, log_path, num)

    task_data = load_data(task_path)
    response_data = load_data(log_path)
    num_tasks = len(task_data)

    timing_info = None
    for response in response_data:
        if 'timing_info' in response:
            timing_info = response['timing_info']
            break

    filtered_response_data = [response for response in response_data if 'timing_info' not in response]
    for i in range(num_tasks):
        try:
            response = filtered_response_data[i]
            task = task_data[i]
            
            # Extract expected tools and inputs
            expected_tools = task.get('tools', [])
            expected_inputs = task.get('inputs', [])

            tools_used, inputs_used = extract_tools_and_inputs(response)
        
            # Evaluate performance
            score = evaluate_task_performance(response, expected_tools, expected_inputs)
            scores.append(score)
        except Exception as e:
            print(f"Error evaluating task {i+1}: {str(e)}")
            scores.append(0)  # Give 0 score for failed evaluations
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
            'match': score == 1
        }
        detailed_results.append(result)
        
        # Print result for this task
        status = "✅ PASS" if score == 1 else "❌ FAIL"
        print(f"Task {i+1:2d}: {status} | Expected: {expected_tools} | Used: {tools_used}")
        if score == 0:
            print(f"         Expected inputs: {expected_inputs}")
            print(f"         Used inputs:     {inputs_used}")

    # Calculate overall performance
    total_score = sum(scores)
    average_score = total_score / len(scores) if scores else 0
    percentage = average_score * 100

    total_prompt_tokens, total_completion_tokens = calculate_total_tokens(response_data)
    total_tokens = total_prompt_tokens + total_completion_tokens
    
    # Print summary
    print("\n" + "=" * 50)
    print("📈 EVALUATION SUMMARY")
    print("=" * 50)
    print(f"Total Tasks Evaluated: {len(scores)}")
    print(f"Tasks Passed: {total_score}")
    print(f"Tasks Failed: {len(scores) - total_score}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Success Rate: {percentage:.1f}%")
    
    # Show failed tasks in detail
    failed_tasks = [r for r in detailed_results if not r['match']]
    if failed_tasks:
        print(f"\n❌ FAILED TASKS ({len(failed_tasks)}):")
        print("-" * 50)
        for task in failed_tasks:
            print(f"Task ID: {task['task_id']}")
            print(f"Content: {task['task_content']}")
            print(f"Expected Tools: {task['expected_tools']}")
            print(f"Used Tools:     {task['tools_used']}")
            print(f"Expected Inputs: {task['expected_inputs']}")
            print(f"Used Inputs:     {task['inputs_used']}")
            print()
    
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
        'tasks_passed': total_score,
        'tasks_failed': len(scores) - total_score,
        'average_score': average_score,
        'success_rate_percentage': percentage,
        'total_prompt_tokens': total_prompt_tokens,
        'total_completion_tokens': total_completion_tokens,
        'total_tokens': total_tokens
    }

    if timing_info:
        evaluation_summary.update(timing_info)

    results_summary = {
        'evaluation_summary': evaluation_summary,
        'detailed_results': detailed_results
    }
    
    os.makedirs("results", exist_ok=True)
    save_data(output_path, results_summary)
    
    print(f"\n💾 Detailed results saved to '{output_path}'")
    
    return average_score
