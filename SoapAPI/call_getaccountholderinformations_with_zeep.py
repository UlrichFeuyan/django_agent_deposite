from zeep import Client
from zeep.wsse.username import UsernameToken

# URL de l'API
url = "https://10.10.104.181:46003/getaccountholderinfo"

# Création du client SOAP
client = Client(url, wsse=UsernameToken("", ""))  # Ajoutez les identifiants appropriés dans les guillemets vides

# Construction de la requête
request_body = {
    "identity": "ID:22956090016/MSISDN"
}

# Envoi de la requête
response = client.service.getaccountholderinforequest(**request_body)

# Extraction des données de la réponse
firstname = response.accountholderbasicinfo.firstname
surname = response.accountholderbasicinfo.surname
profilename = response.accountholderbasicinfo.profilename
accountholderstatus = response.accountholderbasicinfo.accountholderstatus

# Affichage des résultats
print("Firstname:", firstname)
print("Surname:", surname)
print("Profilename:", profilename)
print("Accountholder Status:", accountholderstatus)


from zeep import Client
from zeep.transports import Transport

# URL de l'API
url = "https://10.10.104.181:46003/getaccountholderinfo"

# Configuration du transport avec désactivation de la vérification SSL
transport = Transport(verify=False)

# Création du client SOAP
client = Client(url, transport=transport)

# Corps de la requête
request_body = {
    'identity': 'ID:22956090016/MSISDN'
}

# Envoi de la requête et récupération de la réponse
response = client.service.getaccountholderinforequest(**request_body)

# Extraction des données
firstname = response.accountholderbasicinfo.firstname
surname = response.accountholderbasicinfo.surname
profilename = response.accountholderbasicinfo.profilename
accountholderstatus = response.accountholderbasicinfo.accountholderstatus

# Affichage des résultats
print("Firstname:", firstname)
print("Surname:", surname)
print("Profilename:", profilename)
print("Accountholder Status:", accountholderstatus)
