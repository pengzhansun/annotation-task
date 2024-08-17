import os

# Define the folder path
folder_path = '/home/pengzhan/annotation-task/html_anns'
url_prefix = "https://pengzhansun.github.io/annotation-task/html_anns"

# Get all files in the folder
html_tasks = [os.path.join(url_prefix, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Number of tasks per HTML file
tasks_per_file = 480

# Directory to save the generated HTML files
output_dir = '/home/pengzhan/annotation-task/tasklist_htmls'
os.makedirs(output_dir, exist_ok=True)

# Template for the task list HTML file
html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Annotation Task List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        .task-list {
            list-style-type: none;
            padding: 0;
        }
        .task-item {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }
        .task-item label {
            margin-left: 10px;
        }
        .task-item input[type="checkbox"] {
            transform: scale(1.5);
            margin-right: 10px;
        }
        .task-item a {
            text-decoration: none;
            color: #007bff;
            margin-left: 5px;
        }
        .task-item a:hover {
            text-decoration: underline;
        }
        .save-progress {
            display: block;
            margin-top: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <p>You're given ${tasks_count} tasks shown in this task list. For each task, please select one appropriate sentence from the candidate set generated according to the requirements detailed in the task. You can copy and paste the selected sentence if the quality is good, otherwise please revise the sentence to be natural and similar to human expression.</p>
        <p>Please check the box next to each task as you complete it. This will help you keep track of your progress and identify any tasks that still need to be finished.</p>
        <h1>Annotation Task List</h1>
        <ul class="task-list">
            ${task_items}
        </ul>
        <button class="save-progress" onclick="saveProgress()">Save Progress</button>
    </div>

    <script>
        // Load progress from local storage
        document.addEventListener('DOMContentLoaded', function () {
            for (let i = 1; i <= ${tasks_count}; i++) {
                let checkbox = document.getElementById('task-' + i);
                if (localStorage.getItem('task-' + i) === 'true') {
                    checkbox.checked = true;
                }
                checkbox.addEventListener('change', function () {
                    localStorage.setItem('task-' + i, checkbox.checked);
                });
            }
        });

        // Save progress to local storage
        function saveProgress() {
            alert('Progress saved! You can resume your work anytime.');
        }
    </script>
</body>
</html>'''

# Function to create task items for HTML
def create_task_items(task_paths, start_id):
    task_items = []
    for i, task_path in enumerate(task_paths):
        task_id = start_id + i
        task_items.append(f'''
            <li class="task-item">
                <input type="checkbox" id="task-{task_id}">
                <label for="task-{task_id}"><a href="{task_path}" target="_blank">Task {task_id}</a></label>
            </li>
        ''')
    return '\n'.join(task_items)

# Generate HTML files
total_tasks = len(html_tasks)
for i in range(0, total_tasks, tasks_per_file):
    task_batch = html_tasks[i:i + tasks_per_file]
    start_id = i + 1
    task_items = create_task_items(task_batch, start_id)
    tasks_count = len(task_batch)
    
    # Create the HTML content
    html_content = html_template.replace('${task_items}', task_items).replace('${tasks_count}', str(tasks_count))
    
    # Determine the output file name
    file_number = (i // tasks_per_file) + 1
    output_file_path = os.path.join(output_dir, f'task_list_{file_number}.html')
    
    # Save the HTML content to the file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    
    print(f'Generated {output_file_path} with {tasks_count} tasks.')

print('All HTML files have been generated.')
