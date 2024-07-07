import ollama
response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': """creaza un exemplu de cerinta a unui client fata de o firma it si completeaza template-ul urmator corespunzator cerintei:

Oferta pentru firma

    I. Scopul documentului: 

    Această ofertă preliminară este bazată pe informațiile pe care ni le-ați furnizat. Înainte de a începe efectiv dezvoltarea și de a vă       putea oferi o estimare exactă a costurilor și timpului necesar, va fi necesar să parcurgem câteva etape esențiale de planificare

    1. Elaborarea unei diagrame logice pentru a defini arhitectura aplicației. 
    2. Crearea unei diagrame ER pentru a structura baza de date. 
    3. Realizarea unui design inițial în Figma pentru a elimina orice ambiguitate legată de interfața grafică. 

    Pentru începerea etapelor de mai sus, va fi necesar să semnăm un contract de colaborare și să achitați în avans prețul acestora: 

    Diagrama logică și diagrama ER: X Euro + TVA 
    Proiectul în Figma: X Euro + TVA 
    Acești bani se vor scădea din prețul total de dezvoltare odată acceptată oferta fermă. 

    Oferta de mai jos este doar orientativă și urmărește să vă ofere o perspectivă asupra modului în care operăm și a costurilor probabile.     Pentru o ofertă și un timp de implementare exact, va fi necesar să completăm etapele de planificare menționate

    Definitii:

    -to be completed by ai-    

    II. Propunere structură (335 Ore - 2 Programatori):

    -to be completed by ai-

    III. Sugestii suplimentare (24 ore de munca * 2 programatori): 

    -to be completed by ai-

    IV. Pret și timp de implementare:

    *Fiecare punct poate fi supus modificării, editării sau realizării într-un mod mai sumar, cu reducerea funcționalităților, în vederea     obținerii unei costuri mai reduse.

    *Prețul este orientativ și nu trebuie să fie limitativ; în cazul în care bugetul beneficiarului este mai restrâns decât oferta noastră      în faza de proiectare, putem identifica alternative la costuri inferioare prin integrarea unui număr redus de funcționalități.

    -to be completed by ai-""",
  },
])
print(response['message']['content'])