# Tema-Veziv
Tema prentru evaluarea competentelor primita de la firma Veziv.

Modelul llama3:8b fine-tuned pentru a genera oferte clientilor ca raspuns la solicitarea client.

Un mod usor pentru a observa functionalitatea este acest [google colab](https://colab.research.google.com/drive/15vOSnOfnwcV8B8udUKv_Yrv-unr20N5C?usp=sharing) dar ca sa ruleze este necesar de un gpu nvidia L4, varianta free ofera un T4 iar aceasta rezulta in eroarea: not enaught VRam, si din pacate nu exista un sistem pt a impartasi resurse.
## Inainte de a folosi modelul, dupa git clone trebuie rulate 2 comenzi in Tema-Veziv
```
gdown https://drive.google.com/uc?id=1WEP9C_sPiO5ktzb4nDrgRE-JP71xEgsz
```
```
mv adapter_model.safetensors lora_model
```
*note: Acestea downloadeaza modelul din google drive-ul meu, deoarece am ramas fara credite in git large file storage*
## Cuprins
1. [Generare Oferte](#generare-oferte)
2. [Necesitati Hardware & Software](#necesitati-hardware--software)
3. [Functionalitate](#functionalitate)
   - process_data.py
   - train.py
   - create_offer.py
4. [Inbunatatiri](#Inbunatatiri)
5. [Dependentele Necesare Bazate pe Sistemul de Operare Folosit](#Dependentele-necesare-bazate-pe-systemul-de-operare-folosit)
   - Linux
   - Windows
6. [Note Aditionale Legate de Design](#note-aditionale-legate-de-design)
7. [Note Suplimentare](#note-suplimentare)

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

## Inbunatatiri
 Un set de date mai mare generat cu ajutorul llama3 pe baza exemplelor din Oferte pentru test AI. Exemplele avand o structura asemanatoare dar cu unele diferente precum unde este precizata durata unui proces si costurile, cea mai buna sansa pentru a realiza un rezultat asemanator a fost antrenarea modelului sa genereze tot fisierul intr-un prompt, datele find de asemenea interconectate(ex: structura si definitiile, structura si pretul). Rezultatele in urma antrenarii pe baza celor 16 documente este promitatoare, iar o cale de a optimiza rezultatele este crearea mai multor documente cu ajutorul llama3, si folosindu-ne de llama3 pentru a verifica de asemenea asemanarea dintre documentele generate de llm si cele date ca exemplu.

## Dependentele necesare bazate pe systemul de operare folosit
Python & pip corespunzator cu pytorch.
*[Note from pytorch website](https://pytorch.org/): Latest PyTorch requires Python 3.8 or later.*

*note: Daca intampinati erori in pasii urmatori*
```
pip install --upgrade pip
```
Pentru mai multe detalii legate de instalarea unsloth care urmeaza precum instalare pentru cuda 11.8 aveti acest [link](https://github.com/unslothai/unsloth)
- Linux
   - Cuda drivers
       - cuda toolkit [link](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04)
           - dupa downloadarea .deb:
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
  *Note: dupa instalarea pytorch in wsl am intampinat o eroare legata de versiune de numpy pe care am resolvat-o reinstaland numpy urmand versiunea din mesajul de eroare*

  *Note: Nu am avut destul VRam pt a rula modelul in wsl asa ca am folosit google colab pt testing din pricina faptului ca nu mai erau gpu-uri available pe google cloud*

## Note Aditionale legate de design
Calculatorul meu nu a fost capabil sa ruleze llama3:70b

Nu am avut destula memorie pe ssd pentru a folosi llama3:70b layerd inference facut de [AirLLM](https://github.com/lyogavin/Anima/tree/main/air_llm), care ar trebui sa ofere performanta impresionanta facand llama3:70b sa ruleze pe o placa video de 4GB ram.

Am folosit unsloth pt antrenare si rulare llama3:8b deoarece scade durata de antrenare la jumatate si ofera functi precum RoPe scalling(a primi un input mai mare decat llama3:8b suporta nativ) si 4 bit quantization(care face modelul sa ruleze mai bine/mai repede local)

Calculatorul meu nu a fost capabil sa ruleze unsloth local deoarece am 8g VRam si am intampinat eroarea not enaught VRam asa ca am antrenat si testat modelul in google colab deoarece google cloud nu mai avea disponibile gpu-uri si asa am putut sa ma foloses de un nVidia L4 pentru antrenare si rulare.

## Note suplimentare
exemplu.txt din client_requests este exemplul oferit in Test job Veziv

[huggingface website](https://huggingface.co/)
