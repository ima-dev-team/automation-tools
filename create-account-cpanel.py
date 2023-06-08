import requests

user = 'root'
token = 'QWPC4JPZJVD1YAW6U1O6EY2DQD72AYFO'

headers = {
    'Authorization': f'whm {user}:{token}',
}

data = {
    'username': 'dafsiusernameere',
    'domain': 'dafsi.gov.ao',
    'password': 'StrongerPassword123!',
}

try:
    response = requests.post(
        "https://172.18.40.17:2087/json-api/createacct",
        headers=headers,
        params=data,
        verify=False
    )

    response.raise_for_status()

    data = response.json()

    print(data)  # Print the whole response

    if 'status' in data and data['status'] == 1:
        print(f"[+] Account {data['username']} created successfully")
    else:
        print(f"[-] Account creation failed: {data.get('statusmsg', 'No status message returned')}")

except requests.exceptions.HTTPError as errh:
    print(f"[!] An HTTP error occurred: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"[!] An Error Connecting to the API occurred: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"[!] A Timeout Error occurred: {errt}")
except requests.exceptions.RequestException as err:
    print(f"[!] An Unknown Error occurred: {err}")
