from zeep import Client

client = Client(wsdl='https://www.w3schools.com/xml/tempconvert.asmx?wsdl')

# Appeler une méthode de l'API SOAP avec le client zeep
print(client.service.CelsiusToFahrenheit("100"))
