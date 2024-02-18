from rembg import remove
import imageio as iio
from PIL import Image
import os
from tqdm.auto import tqdm

def remove_bg(frames_dir):

    for image in tqdm(os.listdir(frames_dir)):

        if (image.endswith(".jpg")):
            image_path = frames_dir + "\\" + image
            
            input_image = Image.open(image_path)
            output_image = remove(input_image)
            # image_path_png = image_path.replace("jpg","png")
            rgb_img = output_image.convert("RGB")
            os.remove(image_path)
            rgb_img.save(image_path)
            # output_image.save(image_path_png)
        