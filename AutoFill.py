# Autofill Google Form

import requests

# URL to the form you want to fill. formResponse should be used instead of viewform
testurl = 'https://docs.google.com/forms/d/e/1FAIpQLSekPW7KZ9EsjDsBJ2ox7OwMBGhcErhSvMx1ml3bjZWjmHx8vQ/formResponse'
actualURL = 'https://docs.google.com/forms/d/e/1FAIpQLSdmqeLLjFjYtKGxX2cwSiQ34iQhJ4ajcUbd0gVjhU3_dQidug/formResponse'



    values_list = []
        """keys are the value of 'name' element in the form POST""" "these values are for ACTUAL form"
        
        """values = {
            #NAME
            "entry.639865078": yourNameHere
            #BLOCK
            "entry.1883478312": yourBlockHere
            #Level
            "entry.507729214": yourLevelHere
            #Room
            "entry.1691923912": yourRoomHere
            #Bed number
            "entry.2005248198": yourNumberHere
            #Temperature status
            "entry.1920766654": Normal / Not Normal
            
            #idk what these values are but theyre listed in the post request 
            "entry.1920766654_sentinel": 
            "fvv": 1
            "draftResponse": [null,null,"3241614246892369303"]
            "pageHistory": 0
            "fbzx": 3241614246892369303
        }"""
        
        
        "TEST FORM at TEST URL"
        values = {
            #NAME
            "entry.955312797": aman
            #BLOCK
            "entry.1835522495": Bayley
            #Level
            "entry.1444551311": 7
            #Room
            "entry.1317176630": 14
            #Bed number
            "entry.374108602": A
            #Temperature status
            "entry.364510544": Normal
            
            #default values
            "entry.364510544_sentinel": 
            "fvv": 1
            "draftResponse": [null,null,"-2892881215578928413"]
            "pageHistory": 0
            "fbzx": -2892881215578928413
        }
        
        values_list = values_list.append(values)


def send_temperature(testurl, data):
    """It takes google form url which is to be submitted and also data which is a list of data to be submitted in the form iteratively."""

    for d in data:
        try:
            requests.post(url, data=d)
            print("Form Submitted.")
            time.sleep(10)
        except:
            print("Error Occured!")

send_temperature(testurl, values_list)
