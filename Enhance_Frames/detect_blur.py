import os
from tqdm.auto import tqdm
import cv2

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
