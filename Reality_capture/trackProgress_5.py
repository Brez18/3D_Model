import requests

def track_Progess(access_token,photoscene_id,progress=-1):

    url = f'https://developer.api.autodesk.com/photo-to-3d/v1/photoscene/{photoscene_id}/progress'
    headers = {"Authorization": "Bearer " + access_token}

    response = requests.get(url, headers=headers)
    progress_new = response.json()["Photoscene"]["progress"]

    if(progress_new!=progress):
        print("\n-----Step 5-----")
        print("Status: ",response.json()["Photoscene"]["progressmsg"]),
        print("Progress: ",progress_new)

    if(progress != "100"):
        return track_Progess(access_token,photoscene_id,progress_new)

    print("\n-----Step 5------>Done")
    return True

