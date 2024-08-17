import csv
import os
from string import Template

# Define the path to your CSV file
CSV_FILE_PATH = '/home/pengzhan/paco/paco_aff/raw_all_ann.csv'

# Define the directory where HTML files will be saved
OUTPUT_DIR = '/home/pengzhan/annotation-task/html_anns'

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define your HTML template as a Python string with placeholders
html_template = Template('''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Image Annotation Task</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f0f0f0;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            height: auto;
        }
        h1 {
            text-align: center;
        }
        p {
            text-align: left;
        }
        .instructions {
            margin-bottom: 20px;
        }
        .task {
            text-align: center;
            margin-bottom: 20px;
        }
        .sentences {
            text-align: left;
            margin-bottom: 20px;
        }
        .annotation-tool {
            text-align: center;
            margin-bottom: 20px;
        }
        #image {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 0 auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Select the Appropriate Sentence and Revise it</h1>
        <div class="instructions">
            <p>Here is an image and several human intention sentences generated automatically that express the need of object <i><u><strong>${object}</strong></u></i> shown with the bounding box on the image.</p>
            <img id="image" src="${image_url}" alt="Task Image">
        </div>
        
        <form action="https://script.google.com/macros/s/AKfycbyDH0Wt0lLPppj8tbeuILapQ_nXaNiW_S3b7sgiNxMDJGIGhtTxhRaCJ4B_VqNfYdcsyQ/exec" method="POST">
            <!-- Hidden input to capture image URL -->
            <input type="hidden" name="image_url" value="${image_url}">
            
            <div class="task">
                <h2>Context-aware Intention Sentence</h2>
                <p><i><u><strong>Definition</strong></u></i>: An intention description that includes <i><u><strong>multiple object relationships and/or subtle background cues</strong></u></i>.</p>
                <p>Select a reasonable context-aware intention sentence and revise it if necessary. One sentence is prefered if it matches the primary object affordance or function <i><u><strong>${primary_affordance}</strong></u></i> of the target object <i><u><strong>${object}</strong></u></i>.</p>
                <div class="sentences">
                    <label><input type="radio" name="common_sentence" value="${common_sentence_1}" required> Sentence 1: ${common_sentence_1}</label><br>
                    <label><input type="radio" name="common_sentence" value="${common_sentence_2}" required> Sentence 2: ${common_sentence_2}</label><br>
                    <label><input type="radio" name="common_sentence" value="${common_sentence_3}" required> Sentence 3: ${common_sentence_3}</label><br>
                    <label><input type="radio" name="common_sentence" value="${common_sentence_4}" required> Sentence 4: ${common_sentence_4}</label><br>
                    <label><input type="radio" name="common_sentence" value="${common_sentence_5}" required> Sentence 5: ${common_sentence_5}</label><br>
                    <label><input type="radio" name="common_sentence" value="None of the above is good enough" required> None of the above is good enough</label><br>
                </div>
                <input name="common_utterance" placeholder="Type your revised sentence here..." required>
            </div>
            
            <div class="task">
                <h2>Uncommon Intention Sentence</h2>
                <p><i><u><strong>Definition</strong></u></i>: An intention description that expresses the need for an object's <i><u><strong>uncommon functionality</strong></u></i> instead of the primary affordance or function.</p>
                <p>1. Select a reasonably uncommon intention sentence that <i><u><strong>does NOT</strong></u></i> express the primary affordance or function <i><u><strong>${primary_affordance}</strong></u></i> of the target object <i><u><strong>${object}</strong></u></i>. Priority for selection: 1. The sentence must express an uncommon intention (required); 2. The sentence is related to the displayed picture (optional).</p>
                <p>2. If necessary, revise the selected sentence. If none of the candidate sentences meet the criteria, please write a new sentence that conveys an uncommon intention and <i><u><strong>does NOT</strong></u></i> describe the primary affordance or function <i><u><strong>${primary_affordance}</strong></u></i>.</p>
                <div class="sentences">
                    <label><input type="radio" name="uncommon_sentence" value="${uncommon_sentence_1}" required> Sentence 1: ${uncommon_sentence_1}</label><br>
                    <label><input type="radio" name="uncommon_sentence" value="${uncommon_sentence_2}" required> Sentence 2: ${uncommon_sentence_2}</label><br>
                    <label><input type="radio" name="uncommon_sentence" value="${uncommon_sentence_3}" required> Sentence 3: ${uncommon_sentence_3}</label><br>
                    <label><input type="radio" name="uncommon_sentence" value="${uncommon_sentence_4}" required> Sentence 4: ${uncommon_sentence_4}</label><br>
                    <label><input type="radio" name="uncommon_sentence" value="${uncommon_sentence_5}" required> Sentence 5: ${uncommon_sentence_5}</label><br>
                    <label><input type="radio" name="uncommon_sentence" value="None of the above is good enough" required> None of the above is good enough</label><br>
                </div>
                <input name="uncommon_utterance" placeholder="Type your revised sentence here..." required>
            </div>
            
            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>''')

def main():
    # Open the CSV file
    with open(CSV_FILE_PATH, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Iterate over each row in the CSV
        for idx, row in enumerate(csv_reader):
            # Extract data from the CSV row
            # Adjust the keys based on your CSV's column headers
            data = {
                'image_url': row['image_url'],
                'object': row['object'],
                'primary_affordance': row['primary_affordance'],
                'common_sentence_1': row['common_sentence_1'],
                'common_sentence_2': row['common_sentence_2'],
                'common_sentence_3': row['common_sentence_3'],
                'common_sentence_4': row['common_sentence_4'],
                'common_sentence_5': row['common_sentence_5'],
                'uncommon_sentence_1': row['uncommon_sentence_1'],
                'uncommon_sentence_2': row['uncommon_sentence_2'],
                'uncommon_sentence_3': row['uncommon_sentence_3'],
                'uncommon_sentence_4': row['uncommon_sentence_4'],
                'uncommon_sentence_5': row['uncommon_sentence_5']
            }

            image_url = row['image_url']

            # Split the URL by '/' and get the last part
            file_name = image_url.split('/')[-1]

            # Split the file name by '.' and get the first part (image ID)
            image_id = file_name.split('.')[0]
            
            # Substitute the variables in the template with data from the CSV
            html_content = html_template.substitute(data)
            
            # Define the output HTML file path
            # You can adjust the naming convention as needed
            output_file_path = os.path.join(OUTPUT_DIR, '{}.html'.format(image_id))
            
            # Write the HTML content to the file
            with open(output_file_path, mode='w', encoding='utf-8') as html_file:
                html_file.write(html_content)
            
            # Optional: Print progress every 100 files
            if (idx + 1) % 100 == 0:
                print(f'{idx + 1} HTML files generated.')
    
    print('HTML file generation completed.')

if __name__ == '__main__':
    main()
