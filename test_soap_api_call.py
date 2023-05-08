from wsgiref import headers

import requests
import xml.etree.ElementTree as ET

"""
<ns0:getaccountholderinforequest xmlns:ns0="http://www.ericsson.com/em/emm/provisioning/v1_0">
 <identity>ID:256772712716/MSISDN</identity>
</ns0:getaccountholderinforequest>
"""

# SOAP request URL
url = 'http://www.ericsson.com/em/emm/provisioning/v1_0'
payload = """
    <?xml version="1.0" encoding="UTF-8"?>
    <ns5:getaccountholderinforesponse
    xmlns:ns5="http://www.ericsson.com/em/emm/provisioning/v1_2"
    xmlns:ns3="http://www.ericsson.com/em/emm/v1_2/common"
    xmlns:op="http://www.ericsson.com/em/emm/v1_0/common"
    xmlns:xs="http://www.w3.org/2001/XMLSchema">
     <accountholderbasicinfo>
     <msisdn>229123456789/msisdn>
     <firstname>Test </firstname>
     <surname>bank</surname>
     <profilename>MTN AGENT PROFILE</profilename>
     <internalidentity>ID:470780/ID</internalidentity>
     <defaultfris>
     <defaultfri>
     <fri>FRI:1528233/MM</fri>
     <currency>
     <code>XOF</code>
     </currency>
     </defaultfri>
     </defaultfris>
    <loyaltypointsaccountfri>FRI:1528232/MM</loyaltypointsaccountfri>
     <acceptedtc/>
     <accountholderstatus>ACTIVE</accountholderstatus>
     <bankdomainname>{bank_name}</bankdomainname>
     <hasparent>false</hasparent>
     <languagecode>
     <code>en</code>
     </languagecode>
     <children xmlns:xsi="http://www.w3.org/2001/XMLSchemainstance" xsi:nil="true"/>
     </accountholderbasicinfo>
    </ns5:getaccountholderinforesponse>
"""

headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'text/xml ; charset=utf-8',
    'SOAPAction': ''
}

response = requests.request("POST", url, headers=headers, data=payload)

root = ET.fromstring(response.text)
