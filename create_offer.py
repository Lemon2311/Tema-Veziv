import subprocess

scripts = ['create_offer_subprocesses/offer_tuned_llama3.py', 'create_offer_subprocesses/parseResponse.py']

for script in scripts:
    try:
        result = subprocess.run(['python', script], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f'Error running {script}: {e}')
        print('Error Output:', e.stderr)

print('created offers based on client_requests and placed them in client_offers!')