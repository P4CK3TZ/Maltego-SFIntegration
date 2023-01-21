from MaltegoTransform import *
import requests

class SpiderFootTransform(MaltegoTransform):
    def __init__(self):
        MaltegoTransform.__init__(self)

    def do_transform(self, request, response, config):
        # Replace with your SpiderFoot API key
        api_key = "YOUR_API_KEY"
        
        # Get the item to send to SpiderFoot
        item = request.Value
        
        # Set the base URL for the SpiderFoot API
        base_url = "https://api.spiderfoot.net"
        
        # Build the URL for the scan API endpoint
        url = f"{base_url}/scan?key={api_key}&target={item}"
        
        # Send the request to SpiderFoot
        response = requests.get(url)
        
        # Check the status code of the response
        if response.status_code == 200:
            response.addUIMessage("Item sent to SpiderFoot successfully!")
        else:
            response.addUIMessage("An error occurred while sending the item to SpiderFoot.")

if __name__ == '__main__':
    SpiderFootTransform()
