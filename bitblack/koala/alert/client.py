import requests

alerts = [
  {
    "labels": {
      "alertname": "test",
      "client": "<labelvalue>"
    },
    "annotations": {
      "<labelname>": "<labelvalue>"
    },
    "startsAt": "<rfc3339>",
    "endsAt": "<rfc3339>",
    "generatorURL": "<generator_url>"
  }
]

req = requests.get("http://localhost:9093/#/alerts")

#print(req.content)