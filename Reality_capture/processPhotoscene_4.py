import requests

def process_Photoscene(access_token,photoscene_id):
    
    url = f'https://developer.api.autodesk.com/photo-to-3d/v1/photoscene/{photoscene_id}'
    headers = {"Authorization": "Bearer " + access_token}

    response = requests.post(url, headers=headers)

    print("\n-----Step 4------>Done")
    print(response.json())
