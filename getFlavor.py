import requests
import json


res = requests.get('http://10.0.1.4/compute/v2.1/flavors',
                    headers={'content-type': 'application/json',
                             'X-Auth-Token': 'gAAAAABgJkLW_kstND7bZ54fVdhnVxaFnaSUHhvDok54LYGsWY40kLvCBMIjjIuji0B9zjyfKZqj44wMgyvSrizXSudqzZWwoIALQ8VKJmrHCfaLY_48zt_zSQzVcCNEl99Pg2gJ0kzanhqh-zVoTeoOx3FzMBC1NuLpeHJ2FcrTClBK8FA_24c'
                             },
                   )

print(res.text)
