import requests
import json

payload= {
    "server": {
        "name": "test2",
        "imageRef": "23605eb4-e4b9-4601-a2cc-cab2689b9c28",
        "flavorRef": "1",
        "networks": [{
            "uuid": "90399677-c3dd-47cd-90dc-9e5a19d57103"
        }]
    }
}


res = requests.post('	http://10.0.1.4/compute/v2.1/servers',
                    headers={'content-type': 'application/json',
                             'X-Auth-Token': 'gAAAAABgJkLW_kstND7bZ54fVdhnVxaFnaSUHhvDok54LYGsWY40kLvCBMIjjIuji0B9zjyfKZqj44wMgyvSrizXSudqzZWwoIALQ8VKJmrHCfaLY_48zt_zSQzVcCNEl99Pg2gJ0kzanhqh-zVoTeoOx3FzMBC1NuLpeHJ2FcrTClBK8FA_24c',
                             },
                    data=json.dumps(payload)
                   )

print(res.text)
