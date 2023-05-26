import requests
from xml.etree import ElementTree as ET


def getAccountHolderInformations(telephone):
    """
    Réalise le call api getaccountholderinfo et retourne les informations de l'agent
    """

    # URL de l'API
    url = "https://10.10.104.181:46003/getaccountholderinfo"

    # En-têtes de la requête
    headers = {
        "Content-Type": "text/xml;charset=UTF-8",
    }

    # Corps de la requête
    request_body = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                        <ns0:getaccountholderinforequest xmlns:ns0="http://www.ericsson.com/em/emm/provisioning/v2_1">
                           <identity>ID:229{telephone}/MSISDN</identity>
                        </ns0:getaccountholderinforequest>
                    """
    try:
        # Envoi de la requête
        response = requests.post(url, data=request_body, headers=headers, verify=False)

        # Vérification du statut de la réponse
        if response.status_code == 200:

            # Parsing de la réponse XML
            xml_response = response.content
            root = ET.fromstring(xml_response)

            firstname = root.find('.//firstname').text
            surname = root.find('.//surname').text
            profilename = root.find('.//profilename').text
            identityvalues = [identityvalue.text for identityvalue in root.findall('.//identityvalue')]
            fri = root.find('.//fri').text
            currency_code = root.find('.//currency/code').text
            loyaltypointsaccountfri = root.find('.//loyaltypointsaccountfri').text
            accountholderstatus = root.find('.//accountholderstatus').text
            bankdomainname = root.find('.//bankdomainname').text
            languagecode = root.find('.//languagecode/code').text

            telephone = identityvalues[0]
            identity = identityvalues[1]

            code_agent = identity[identity.index(':') + 1:identity.index('/')]
            msisdn = telephone[telephone.index(':') + 1:telephone.index('/')]
            nom_agent = f"{firstname} {surname}"
            status_agent = accountholderstatus == 'ACTIVE'

            # Extraction des données
            agentInformations = {
                'code_agent': code_agent,
                'msisdn': msisdn,
                'nom_agent': nom_agent,
                'status_agent': status_agent,
            }
            return agentInformations
        else:
            return False
    except:
        print("erreur lors du call api")
        return False


if __name__ == '__main__':

    # URL de l'API
    url = "https://10.10.104.181:46003/getaccountholderinfo"

    # En-têtes de la requête
    headers = {
        "Content-Type": "text/xml;charset=UTF-8",
    }

    # Corps de la requête
    request_body = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                        <ns0:getaccountholderinforequest xmlns:ns0="http://www.ericsson.com/em/emm/provisioning/v2_1">
                           <identity>ID:22956090016/MSISDN</identity>
                        </ns0:getaccountholderinforequest>
                    """

    # Envoi de la requête
    response = requests.post(url, data=request_body, headers=headers, verify=False)

    # Vérification du statut de la réponse
    if response.status_code == 200:
        # Parsing de la réponse XML
        xml_response = response.content
        print("\n\n")
        root = ET.fromstring(xml_response)

        # Extraction des données
        firstname = root.find('.//firstname').text
        surname = root.find('.//surname').text
        profilename = root.find('.//profilename').text
        identityvalues = [identityvalue.text for identityvalue in root.findall('.//identityvalue')]
        fri = root.find('.//fri').text
        currency_code = root.find('.//currency/code').text
        loyaltypointsaccountfri = root.find('.//loyaltypointsaccountfri').text
        accountholderstatus = root.find('.//accountholderstatus').text
        bankdomainname = root.find('.//bankdomainname').text
        languagecode = root.find('.//languagecode/code').text

        # Affichage des résultats
        print(f"First Name: {firstname}")
        print(f"Surname: {surname}")
        print(f"Profile Name: {profilename}")
        print(f"Identity Values: {identityvalues}")
        print(f"FRI: {fri}")
        print(f"Currency Code: {currency_code}")
        print(f"Loyalty Points Account FRI: {loyaltypointsaccountfri}")
        print(f"Account Holder Status: {accountholderstatus}")
        print(f"Bank Domain Name: {bankdomainname}")
        print(f"Language Code: {languagecode}")
    else:
        print("Erreur lors de la requête:", response.status_code, response.text)
