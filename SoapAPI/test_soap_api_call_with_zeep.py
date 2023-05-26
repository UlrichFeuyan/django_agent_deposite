from zeep import Client

client = Client(wsdl='https://www.w3schools.com/xml/tempconvert.asmx?wsdl')


def callCelsiusToFahrenheitAPI(temperature): return client.service.CelsiusToFahrenheit(f"{temperature}")


if __name__ == '__main__':
    callCelsiusToFahrenheitAPI("54")
