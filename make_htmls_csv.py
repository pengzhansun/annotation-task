import os
import csv

# Define the folder path
folder_path = '/home/pengzhan/annotation-task/tasklist_htmls'
url_prefix = "https://pengzhansun.github.io/annotation-task/tasklist_htmls"

# Get all files in the folder
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Combine the URL prefix with each file name using os.path.join
urls = [os.path.join(url_prefix, file_name) for file_name in file_names]

# Save the URLs to a CSV file
csv_file_path = 'paco_sentences_tasklist.csv'  # You can specify the path where you want to save the CSV file

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    for url in urls:
        writer.writerow([url])  # Write each URL into column A

# print(f"CSV file with URLs has been saved to {csv_file_path}")
