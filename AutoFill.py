# Simple script to experiment with Python's requests library.

import requests

# URL to the form you want to fill. formResponse should be used instead of viewform

url = 'https://docs.google.com/forms/d/e/1FAIpQLSdmqeLLjFjYtKGxX2cwSiQ34iQhJ4ajcUbd0gVjhU3_dQidug/formResponse'

# Fill this in
name = ""
block = ""
level = ""
room = ""
bednumber = ''
temperature_status = ""
    

data = {
            #NAME
            "entry.639865078": name,
            #BLOCK
            "entry.1883478312": block,
            #Level
            "entry.507729214": level,
            #Room
            "entry.1691923912": room,
            #Bed number
            "entry.2005248198": bednumber,
            #Temperature status
            "entry.1920766654": temperature_status
        }
        

requests.post(url, data=data)
print("Form Submitted.")

