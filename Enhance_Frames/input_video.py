import ffmpeg
import os
from basicsr.demo import unblur
from tqdm.auto import tqdm
import cv2
from remove_bg import remove_bg
import time


def detect_blur(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Laplacian filter for edge detection
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)

    # Calculate maximum intensity and variance
    laplacian_variance = laplacian.var()

    # Check blur condition based on variance of Laplacian image
    if laplacian_variance < 49:
        return True # Blurry

    return False # Not Blurry

main_dir = os.getcwd()


# path/directory for video
os.chdir("..\Video")
video_dir = os.getcwd()

for video in os.listdir(video_dir):
    if(video.endswith('.mp4'))
        input_file = os.path.abspath(video) 


os.chdir("..\Frames")

# path/directory for frames
# frames_dir = os.getcwd()
# os.chdir(main_dir)


# input = ffmpeg.input(input_file)
# input.output(frames_dir + "\\frame_%3d.jpg",vf='fps=2',q="0",s="1920x1080").run()
 
blurry_images = []

for image in os.listdir(frames_dir):
    if (image.endswith(".jpeg") or image.endswith(".jpg")):
        image_path = os.path.abspath(image) 
        if detect_blur(image_path):
           blurry_images.append(image_path)

print()

for blurry_image in tqdm(blurry_images):
    print("\n....Unbluring ", os.path.basename(blurry_image),"....")
    unblur(blurry_image)
    print()

time.sleep(60)
remove_bg(frames_dir)

            