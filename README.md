# Tema-Veziv
Tema prentru evaluarea competentelor primita de la firma Veziv.

Modelul llama3:8b fine-tuned pentru a genera oferte clientilor ca raspuns la solicitarea client.
## Generare oferte
Dupa ce ati citit [necesitatile hardware si software](#Necesitati-hardware-&-software) si ati instalat [dependentele](#Dependentele-necesare-bazate-pe-systemul-de-operare-folosit).

1.)Adaugati in directory-ul client_requests fisiere de tip .txt continand Solicitarea client ale caror text sa urmeze structura:

```
Solicitarea client: O aplicatie care sa...
```


2.)

```
python create_offer.py
```

Dupa executarea scriptului create_offer.py, directory-ul client_offers_docx contine ofertele ca rezultat a solicitarilor clientilor in fisiere word numite corespunzator, precum fisierele .txt din client_requests astfel incat sa aiba acelasi nume, diferentiand doar locatia si extensia.


## Necesitati hardware & software
 - linux machine
 - placa video cu aproximativ 20 VRam

 *note: Am folosit un nVidia L4 cu 25 ram, in general consumul a fost de aproximativ 15 vram. Am reusit sa il rulez si pe un t4 cu 15 vram dar cu placa video t4 am intampinat adesea eroarea: not enaught Vram*

## Functionalitate
Functionalitatea este impartita in 3 procese principale:
 - process_data.py
    - acest script extrage datele pentru antrenare din documentele word aflate in directory-ul Oferte_test si creaza fisierul data.json care contine datasetul impartit urmand formatul alpaca prompt(instruction, input, output) dupa care acesta poate fi adaugat ca dataset pe siteul huggingface pentru a fi folosit ulterior in functia train.py 
 - train.py
    - acest script antreneaza(fine-tuning) modelul llama3:8b pe orice dataset de pe huggingface pasat ca argument la chemarea scriptului, respectiv pe datasetul creat cu process-data.py dupa adaugarea lui pe huggingface sau precum precizat orice dataset de pe huggingface. Fine-tuning-ul este salvat ca un adaptor [LoRa](# "Low-Rank Adaptation") in directory-ul lora_model, pentru a putea fi "merged" cu llama3:8b si folosit ulterior.<br>

      *exemplu de folosire*
      ```
      python train.py --model Lemon2311/clientOffer
      ```
      *note: Lemon2311/clientOffer este datasetul creat cu process_data.py din fisierul Oferte pentru test AI downloadad din arhiva care acum se regaseste pe huggingface*
 - create_offer.py
     - acest script este folosit pentru a extrage textul din fisierele txt din directoy-ul client_requests, a folosi modelul fine tuned llama3:8b si a crea in directory-ul client-offers_docx fisiere de tip word continand oferta generata pe baza cerintei clientului.
       <br>
       
       *exemplu de text care se regaeseste intr-un fisier din client_requests (exemplu.txt)*
       ```
       Solicitarea client: O alpicatie web care sa....
       ```

## Dependentele necesare bazate pe systemul de operare folosit
Python & pip corespunzator cu pytorch pentru orice system de operare
*note: Daca intampinati erori in pasii urmatori*
```
pip install --upgrade pip
```
Pentru mai multe detalii legate de instalarea unsloth care urmeaza precum instalare pentru cuda 11.8 aveti acest [link](https://github.com/unslothai/unsloth)
- Linux
   - Cuda drivers
       - cuda toolkit [link](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04)
           - dupa downlodarea .deb:
           ```python
           cd Downloads
           sudo dpkg -i fileName.deb
           ```
           *note: fileName este un placeholder pentru numele fisierului downloadat*
       - pytorch cu driverele cuda
       ```python
       pip install --upgrade --force-reinstall --no-cache-dir torch==2.1.0 triton \  --index-url https://download.pytorch.org/whl/cu121
       ```
       - unsloth
          - pentru gpu-uri moderne RTX30xx or higher
          ```python
          pip install "unsloth[cu121-ampere-torch220] @ git+https://github.com/unslothai/unsloth.git"
          ```
          - older 
          ```python
          pip install "unsloth[cu121] @ git+https://github.com/unslothai/unsloth.git"
          ```
       - python-docx
     ```python
     pip install python-docx
     ```
- Windows
   - Wsl si un distro de linux care e compatibil cu pyTorch
  
   *note: cel mai usor este sa downlodati ubuntu de pe microsoft store care instaleaza wsl si versiunea de ubuntu selectata si creaza aplicatia ubuntu care cand este folosita deschide un terminal de linux care e conectat la enviromentul linux instalat.*
   - Cuda drivers
       - pytorch cu driverele cuda
     ```python
     pip install --upgrade --force-reinstall --no-cache-dir torch==2.1.0 triton \  --index-url https://download.pytorch.org/whl/cu121
     ```
       - unsloth
          - pentru gpu-uri moderne RTX30xx or higher
          ```python
          pip install "unsloth[cu121-ampere-torch220] @ git+https://github.com/unslothai/unsloth.git"
          ```
          - older 
          ```python
          pip install "unsloth[cu121] @ git+https://github.com/unslothai/unsloth.git"
          ```
       - python-docx
     ```python
     pip install python-docx
     ```
       - cuda wsl drivers in windows folosing [link](https://developer.nvidia.com/cuda/wsl)
       - cuda toolkit varianta pentru wsl in enviromentul linux:
     ```python
     sudo wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
     sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
     sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/3bf863cc.pub
     sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/ /"
     sudo apt-get update
     sudo apt-get install cuda
     echo 'export PATH=/usr/local/cuda/bin:$PATH' >> ~/.bashrc
     echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
     source ~/.bashrc
      ```

## Plan
Run llama3 locally:
       tried 70b, but computer not good enaught
       tried layered inference version but didnt have enaught memory on my ssd
       using llama3 8b
