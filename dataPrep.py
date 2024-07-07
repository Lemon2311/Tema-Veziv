import os
import json

input_dir = 'input'
output_dir = 'output'

with open('request_template.txt', 'r', encoding='utf-8') as f_template:
    instruction_text = f_template.read()

input_files = os.listdir(input_dir)
output_files = os.listdir(output_dir)

data = []

def prepare_data():
    for input_file in input_files:
        if input_file in output_files:
            with open(os.path.join(input_dir, input_file), 'r', encoding='utf-8') as f_input, \
                 open(os.path.join(output_dir, input_file), 'r', encoding='utf-8') as f_output:
                input_content = f_input.read()
                output_content = f_output.read()
                data.append({
                    "instruction": instruction_text,
                    "input": input_content,
                    "output": output_content
                })

    with open('data.json', 'w', encoding='utf-8') as f_json:
        json.dump(data, f_json, indent=4, ensure_ascii=False)