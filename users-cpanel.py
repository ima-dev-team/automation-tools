import requests
import json

user = 'root'
token = 'QWPC4JPZJVD1YAW6U1O6EY2DQD72AYFO'

headers = {
    'Authorization': f'whm {user}:{token}',
}

try:
    response = requests.get(
        "https://172.18.40.17:2087/json-api/listaccts?api.version=1",
        headers=headers,
        verify=False
    )

    response.raise_for_status()  # Will raise an exception for 4xx and 5xx status codes

    data = response.json()  # Automatically decodes the JSON response
    print("[+] Current cPanel users on the system:")
    for account in data['data']['acct']:
        print(f"\t{account['user']}")
except requests.exceptions.HTTPError as errh:
    print(f"[!] An HTTP error occurred: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"[!] An Error Connecting to the API occurred: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"[!] A Timeout Error occurred: {errt}")
except requests.exceptions.RequestException as err:
    print(f"[!] An Unknown Error occurred: {err}")
