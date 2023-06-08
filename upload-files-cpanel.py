import os
import requests
from requests.auth import HTTPBasicAuth
import json

# Authentication information
username = 'username'
password = '12345luggage'

# The URL for the Fileman::upload_files UAPI function
url = "https://localhost:2083/execute/Fileman/upload_files"

# Headers
headers = {'Authorization': 'Basic ' + (username + ':' + password).encode('base64').rstrip('\n')}

# Directory to upload
dir_path = '/path/to/your/directory'

# For each root, dir, and file in the directory
for root, dirs, files in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)

        # Open the file in binary
        bin_data = open(file_path, 'rb')

        # Do the POST request, including the file
        response = requests.post(
            url,
            auth=HTTPBasicAuth(username, password),
            files={
                'file-1': bin_data
            },
            data={
                'dir': 'public_html',
            },
            headers=headers,
            verify=False
        )

        # Close file
        bin_data.close()

        # Handle response
        if response.status_code == 200:
            print('Uploaded file ' + file_path + ': ' + json.dumps(response.json(), indent=4))
        else:
            print('Failed to upload file ' + file_path + ', status code: ' + str(response.status_code))
