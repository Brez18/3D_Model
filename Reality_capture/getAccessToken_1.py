import requests

def get_AccessToken(client_id, secret_key):

    url = "https://developer.api.autodesk.com/authentication/v1/authenticate"
    data = {
        "client_id": client_id,
        "client_secret": secret_key,
        "grant_type": "client_credentials",
        "scope": "data:read data:write data:create bucket:create bucket:read"
    }

    response = requests.post(url, data=data)
    access_token = response.json()["access_token"]

    print("\n-----Step 1------>Done")
    print("Access Token: ",access_token,"\n")

    return access_token

    

