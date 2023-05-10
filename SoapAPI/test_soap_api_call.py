from xml.etree import ElementTree
import requests
from django.core.files import temp

tempF = "100"  # valeur d'entrée; température en Fahrenheit

url = 'https://www.w3schools.com/xml/tempconvert.asmx'  # URL de l'endpoint
namespace = 'https://www.w3schools.com/xml/'  # namespace
action = 'FahrenheitToCelsius'  # fonction à appeler


def callApi(url, namespace, action, param):
    # En-têtes de la requête
    headers = {'Content-Type': 'text/xml; charset=utf-8',
               'SOAPAction': f'{namespace}{action}'
               }
    # Corps de la requête
    body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <FahrenheitToCelsius xmlns="https://www.w3schools.com/xml/">
          <Fahrenheit>{param}</Fahrenheit>
        </FahrenheitToCelsius>
      </soap:Body>
    </soap:Envelope>"""

    # Envoi de la requête
    response = requests.post(url, data=body, headers=headers)

    root = ElementTree.fromstring(response.content)
    temp = ""

    for child in root.iter("{https://www.w3schools.com/xml/}FahrenheitToCelsiusResult"):
        temp = child.text

    return temp


if __name__ == "__main__":
    print(callApi(url, namespace, action, tempF))
