import requests
import json

url = 'your webhook URL here'

data = {
   "type":"message",
   "attachments":[
      {
         "contentType":"application/vnd.microsoft.card.adaptive",
         "content":{
            "$schema":"http://adaptivecards.io/schemas/adaptive-card.json",
            "type":"AdaptiveCard",
            "version":"1.2",
            "body":[
                {
                "type": "TextBlock",
                "text": "Your message here"
                }
            ]
         }
      }
   ]
}
r = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
