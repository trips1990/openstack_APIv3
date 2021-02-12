import requests
import json

payload = {
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "admin",
                    "domain": {
                        "name": "Default"
                    },
                    "password": "P@ssw0rd"}
            }
        },
        "scope": {
            "project": {
                "domain": {
                    "id": "default"
                },
                "name": "admin"
            }
        }
    }
}

res = requests.post('http://10.0.1.4/identity/v3/auth/tokens',
                    headers = {'content-type':'application/json'},
                    data=json.dumps(payload))

print(res.headers)
