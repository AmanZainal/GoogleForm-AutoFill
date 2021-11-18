# Autofill Google Form
# Submits a Normal temperature record to a testURL and the actualURL.

# For usage of Raffles Institution Boarding students. 
# Ideally, the script can be automatically executed from a server such as PythonAnywhere so you dont have to do it manually.
# Users are responsible for their own temperature.  

import requests

# URL to the form you want to fill. formResponse should be used instead of viewform
testurl = 'https://docs.google.com/forms/d/e/1FAIpQLSekPW7KZ9EsjDsBJ2ox7OwMBGhcErhSvMx1ml3bjZWjmHx8vQ/formResponse'
realurl = 'https://docs.google.com/forms/d/e/1FAIpQLSdmqeLLjFjYtKGxX2cwSiQ34iQhJ4ajcUbd0gVjhU3_dQidug/formResponse'

# Fill in your particulars and execute the code.
name = ""
block = ""
level = ""
room = ""
bednumber = ''
temperature_status = ""


# GoogleForm data entries extracted.
realdata={
"entry.639865078": name,
"entry.1883478312": block,
"entry.507729214": level,
"entry.1691923912": room,
"entry.2005248198": bednumber,
"entry.1920766654": temperature_status,
"entry.1920766654_sentinel":"",
"pageHistory": 0,
"fvv":1,
"draftResponse": ["","","3069998196324029432"],
"fbzx": 3069998196324029432
}

# Test data to be submitted to a test url to verify the code actually works. (I don't have access to the real url)
testdata={
"entry.955312797": name,
"entry.1835522495": block,
"entry.1444551311": level,
"entry.1317176630": room,
"entry.374108602": bednumber,
"entry.364510544": temperature_status,
"entry.364510544_sentinel": "",
"fvv": 1,
"draftResponse": ["","","4733745314106942646"],
"pageHistory": 0,
"fbzx": 4733745314106942
}

# Update: Since RIB changes the form to have 1 or 2 pages, the following "pageHistory" argument needs to be added for when the pages change.
# The following code is only successfully executed if the form changes to have 2 pages. Otherwise, it is ignored. (Or rather, fails to execute because the pageHistory argument doesn't work for 0-page forms)

realdata3={
"entry.639865078": name,
"entry.1883478312": block,
"entry.507729214": level,
"entry.1691923912": room,
"entry.2005248198": bednumber,
"entry.1920766654": temperature_status,
"entry.1920766654_sentinel":"",
#change page history = 0 for no "next" pages, pH = 1 if there is a next page
"pageHistory": "0,1",
"fvv":1,
"draftResponse": ["","","3069998196324029432"],
"fbzx": 3069998196324029432
}

testdata3={
"entry.955312797": name,
"entry.1835522495": block,
"entry.1444551311": level,
"entry.1317176630": room,
"entry.374108602": bednumber,
"entry.364510544": temperature_status,
"entry.364510544_sentinel": "",
"fvv": 1,
"draftResponse": ["","","4733745314106942646"],
"pageHistory": "0,1",
"fbzx": 4733745314106942
}

requests.post(testurl, data=testdata3)
requests.post(realurl, data=realdata3)

requests.post(testurl, data=testdata)
requests.post(realurl, data=realdata)

print("Forms Submitted.")
