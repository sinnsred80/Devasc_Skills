

This is the readme file where I will document everything I do during this skills exam..

TASK 1 -- GitHub Skills Test *** Task name: GitHub 
Task preparation: 
Task Implementation: Lage ny reposotory på github og koble dette sammen med lokale filer.
Task Troubleshoothing: 
Task Verification: Sjekket at filen lokalt ble synkronisert til github. 

TASK 2 -- Ansible Skills Test *** Task name: Ansible 
Task preparation: Bruke csr1000v installasjonen og en tidlligere ansible playbook som mal for de kommandoen som skulle kjøres.

Task Implementation: Gikk stegvis gjennom oppsettet og la til en og en ny kommando for å sørge for at det fungerte greit. To av oppgavene eller kommandoene fungerte ikke, da det henviste til interface som ikke eksisterte. Har gjort endringer der det var nødvendig.

Task Troubleshoothing: La til en kommando av gangen, testet og verifiserte. 

Task Verification:
devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$ ansible-playbook ios_status.yaml 

PLAY [IOS STATUS] ************************************************************************************

TASK [run show version on remote devices] ************************************************************
ok: [CSR1kv]

TASK [run show version on remote devices] ************************************************************
ok: [CSR1kv]

TASK [run show version and check to see if output contains IOS] **************************************
ok: [CSR1kv]

TASK [run multiple commands on remote nodes] *********************************************************
ok: [CSR1kv]

TASK [run multiple commands and evaluate the output] *************************************************
ok: [CSR1kv]

TASK [run commands that require answering a prompt] **************************************************
ok: [CSR1kv]

PLAY RECAP *******************************************************************************************
CSR1kv                     : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

TASK 3 -- Docker *** 
Task name: Docker 
Task preparation: Måtte forstå hvordan jeg skulle bruke informasjonen i oppgaven. Jeg trodde jeg skulle implementere en playbook i Docker, men skjønte etter hvert at jeg skulle gjenskape det samme som var i playbook i docker.
Task Implementation: Lagde et script basert på det som var i sample-app oppgaven, men brukte ubuntu som OS. Installerte apache server, endret portnummer til 8081.
Task Troubleshoothing: 
Task Verification: Fikk opp apache-serveren ved å skrive localhost:8081.

TASK 4 -- Jenkins ** Task name: Jenkins Task preparation: Task Implementation: Task Troubleshoothing: Task Verification:

TASK 5 -- REST API & RESTCONF **** Task name: restconf Task preparation: Task Implementation: Task Troubleshoothing: Task Verification:

TASK 6 -- Webex Teams API *** 
Task name: Webex 
Task preparation: Få tak i token og se på API dokumentasjonen
Task Implementation: Har funnet noen eksempler her og der som jeg har brukt. Har forsøkt å gjøre flere ting i samme kode og har derfor slått sammen to og to av oppgavene.
Task Troubleshoothing: Litt vrient med å sende flere filer samtidig, men fikk det til.
Task Verification: Ser alt dukker oppi WebEx

TASK 7 -- BASH *** Task name: Bash 
Task preparation: Gjøre klar konfigfiler som skal sjekkes
Task Implementation: Brukte en mal som utgangspunkt, men gjorde noen mindre enringer
Task Troubleshoothing: 
Task Verification: filen check_ios.rep blir oppdatert

