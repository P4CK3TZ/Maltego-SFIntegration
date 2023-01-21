import base64
from MaltegoTransform import *
import requests

# Encode the code
encoded_code = base64.b64encode(b'''
class a(MaltegoTransform):
    def __init__(self):
        MaltegoTransform.__init__(self)

    def b(self, request, response, config):
        api_key = "YOUR_API_KEY"
        c = request.Value
        d = "https://api.spiderfoot.net"
        e = d + "/scan?key=" + api_key + "&target=" + c
        f = requests.get(e)
        if f.status_code == 200:
            response.addUIMessage("Item sent to SpiderFoot successfully!")
        else:
            response.addUIMessage("An error occurred while sending the item to SpiderFoot.")

if __name__ == '__main__':
    a()
''')

# Decode the code
decoded_code = base64.b64decode(encoded_code).decode()

# Run the decoded code
exec(decoded_code)
