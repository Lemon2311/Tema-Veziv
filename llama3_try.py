import ollama
response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': """Genereaza o ofertă detaliată in limba romana pentru client care să includă:
■ Descrierea aplicației solicitate.
■ Tehnologiile folosite pentru dezvoltarea aplicației (ex: stack tehnologic
- front-end, back-end, baze de date, etc.).
■ Task-urile concrete și detaliate necesare pentru dezvoltarea aplicației,
inclusiv cele care nu sunt menționate direct de client dar sunt
necesare (ex: secțiuni financiare, facturare, etc.),
urmand templateul "Solicitarea client

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

    II. Propunere structură (X Ore - X Programatori):

    -to be completed by ai-

    III. Sugestii suplimentare (X ore de munca * X programatori): 

    -to be completed by ai-

    IV. Pret și timp de implementare:

    *Fiecare punct poate fi supus modificării, editării sau realizării într-un mod mai sumar, cu reducerea funcționalităților, în vederea     obținerii unei costuri mai reduse.

    *Prețul este orientativ și nu trebuie să fie limitativ; în cazul în care bugetul beneficiarului este mai restrâns decât oferta noastră      în faza de proiectare, putem identifica alternative la costuri inferioare prin integrarea unui număr redus de funcționalități.

    -to be completed by ai-"
   pentru Solicitarea client: Aplicatia sa contina 3 ramuri esentiale: 1. Sofer: harta cu traseul sau care sa contina punctele de ridicare si livrare. Timpul estimat pentru ambele . Posibilitatea de a prelua singur o solicitare de la un restaurant sau sa i se acorde livrari. Raport zilnic cu livrarile efectuate.Actualizare in timp real al parcursului sau catre client. 2. Restaurant: preluare comenzi, confirmarea lor si a statusului comenzii in timp real catre client. In orele de varf sa nu mai aiba clientul optiunea de a pune noi comenzi daca dureaza mai mult decat timpul estimat in aplicatie. Solictare sofer si optiunea de a vedea parcursul soferului. 3. Client : sa i-a la cunostinta toate detaliile legate de restaurant ( timp estimate de livrare , timp de preparare etc). sa adauge produse in cos , achizitie cu card sau numerar din aplicatie. Sa primeasca notificari cu fiecare parcurs al comenzii (confirmata, comanda urmeaza sa fie ridicata, comanda a fost ridicata, comanda livrata). Dupa plasarea si confirmarea si preluarea comenzii de catre sofer sa I se prezinte soferul, numarul de contact al acestuia si parcursul sau pe harta. FUNCTIE ADMIN : care poate observa activitatea celor 3 ramuri mentionate si poate efectua un raport pe fiecare. Firma are contracted oar cu restaurante . In aditie mai fac livrari de colete mici sau plicuri la solicitarea clientilor prin urmare ar trebui si o optiune de acest gen in aplicatie unde sa ofere cateva info despre colet (daca e plic sau e o cutie si ce demensiuni/greutate are).""",
  },
])
print(response['message']['content'])