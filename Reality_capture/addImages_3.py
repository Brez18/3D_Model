import requests
import os

def add_Images(access_token,photoscene_id):

    url = 'https://developer.api.autodesk.com/photo-to-3d/v1/file'
    headers = {
        "Authorization": "Bearer " + access_token
    }
    data = {
        'photosceneid': photoscene_id,
        'type': 'image'
    }

    files = {}
    i=0
    for image in os.listdir("./Frames"):

        if (image.endswith(".jpg")):
            file_key = f'file[{i}]'
            file_path = os.getcwd() + "/Frames/" + image
            files[file_key] = open(file_path, 'rb')

            i+=1


    response = requests.post(url, headers=headers, data=data, files=files)

    for file_obj in files.values():
        file_obj.close()

    print("\n-----Step 3------>Done")
    print(response.json(),"\n")


