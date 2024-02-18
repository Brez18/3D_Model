import ffmpeg
import os
import time

from Enhance_Frames.detect_blur import detect_blur
from Enhance_Frames.basicsr.demo import unblur
from Enhance_Frames.remove_bg import remove_bg
from tqdm.auto import tqdm

from Reality_capture.getAccessToken_1 import get_AccessToken
from Reality_capture.getPhotoSceneID_2 import get_PhotoSceneID
from Reality_capture.addImages_3 import add_Images
from Reality_capture.processPhotoscene_4 import process_Photoscene
from Reality_capture.trackProgress_5 import track_Progess
from Reality_capture.getDownloadURL_6 import get_DownloadURL




### Step 1 - Taking video as input and getting Frames ####

for video in os.listdir("./Video"):
    if(video.endswith('.mp4')):
        input_file = "./Video/"+ video 

input = ffmpeg.input(input_file)
input.output("./Frames/frame_%3d.jpg",vf='fps=2',q="0",s="1920x1080").run()


#### Step 2 - Enhancing Frames ####

# gathering blurry frames
blurry_images = []

for image in os.listdir("./Frames"):
    if (image.endswith(".jpeg") or image.endswith(".jpg")):
        image_path = os.getcwd()+"/Frames/"+ image
        if detect_blur(image_path):
           blurry_images.append(image_path)

# unbluring blurry frames

main_dir = os.getcwd()
os.chdir("Enhance_Frames")

print()
for blurry_image in tqdm(blurry_images):
    print("\n....Unbluring ", os.path.basename(blurry_image),"....")
    unblur(blurry_image)
    print()

os.chdir(main_dir)

# removing background
time.sleep(60)
remove_bg(".\Frames")


#### Step 3 - Making Model ####

print("\n\n........Starting to make model")

client_id = "fAicA3sdx43mVgOiGWmPWt6unhqv9exT"
secret_key = "X3qiwH1LJcwDdQAs"

access_token = get_AccessToken(client_id,secret_key) #Step 1
photoscene_id = get_PhotoSceneID(access_token) #Step 2

add_Images(access_token, photoscene_id) #Step 3
process_Photoscene(access_token,photoscene_id) #Step 4


if(track_Progess(access_token,photoscene_id)): #Step 5
    get_DownloadURL(access_token,photoscene_id) #Step 6

