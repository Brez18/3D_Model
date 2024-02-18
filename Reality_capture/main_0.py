from getAccessToken_1 import get_AccessToken
from getPhotoSceneID_2 import get_PhotoSceneID
from addImages_3 import add_Images
from processPhotoscene_4 import process_Photoscene
from trackProgress_5 import track_Progess
from getDownloadURL_6 import get_DownloadURL



client_id = "fAicA3sdx43mVgOiGWmPWt6unhqv9exT"
secret_key = "X3qiwH1LJcwDdQAs"

access_token = get_AccessToken(client_id,secret_key) #Step 1
photoscene_id = get_PhotoSceneID(access_token) #Step 2

add_Images(access_token, photoscene_id) #Step 3
process_Photoscene(access_token,photoscene_id) #Step 4


if(track_Progess(access_token,photoscene_id)): #Step 5
    get_DownloadURL(access_token,photoscene_id) #Step 6