import requests

def get_PhotoSceneID(access_token):
        
    url = "https://developer.api.autodesk.com/photo-to-3d/v1/photoscene/"

    headers = {"Authorization": "Bearer " + access_token}
    data = {"scenetype": "object", "format": "obj","scenename":"3d test"}
    response = requests.post(url, headers=headers, data=data)

    
    photoscene_id = response.json()["Photoscene"]["photosceneid"]
    
    print("\n-----Step 2------>Done")
    print("Photoscene ID: ",photoscene_id,"\n")
    
    return photoscene_id
