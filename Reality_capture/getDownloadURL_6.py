import requests

def get_DownloadURL(access_token,photoscene_id):
    url = f'https://developer.api.autodesk.com/photo-to-3d/v1/photoscene/{photoscene_id}?format=obj'
    headers = {"Authorization": "Bearer " + access_token}

    response = requests.get(url, headers=headers)
    scenelink = response.json()["Photoscene"]["scenelink"]

    print("\n-----Step 6------->Done")
    print("SceneLink",scenelink)


