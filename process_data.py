import subprocess

scripts = ['process_data_subprocesses/split_Oferte_test.py', 'process_data_subprocesses/data_preparation.py']

for script in scripts:
    try:
        result = subprocess.run(['python', script], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f'Error running {script}: {e}')
        print('Error Output:', e.stderr)

print('Prepared training dataset as data.json!')