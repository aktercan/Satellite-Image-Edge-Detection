import numpy as np
import rasterio
import cv2
import matplotlib.pyplot as plt


def load_image(path):
    """Load image data from a raster file."""
    try:
        with rasterio.open(path) as src:
            image = src.read(1)
        return image
    except Exception as e:
        print(f"Error loading the image: {e}")
        return None


def normalize_image(image):
    """Normalize image data to 0-255 range."""
    max_value = np.amax(image)
    if max_value == 0:
        raise ValueError("Maximum pixel value is 0, normalization is not possible.")
    return (image / max_value * 255).astype(np.uint8)


def apply_gaussian_blur(image, kernel_size=(5, 5)):
    """Apply Gaussian blur to reduce noise."""
    return cv2.GaussianBlur(image, kernel_size, 0)


def detect_edges(image, threshold1=40, threshold2=80):
    """Detect edges using the Canny edge detector."""
    return cv2.Canny(image, threshold1, threshold2)


def display_images(original, edges):
    """Display the original image and its edges."""
    plt.figure(figsize=(10, 5))
    plt.subplot(121), plt.imshow(original, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Canny Edges'), plt.xticks([]), plt.yticks([])
    plt.show()


# File path
B02path = "61.jp2"

# Main workflow
imageB02 = load_image(B02path)
if imageB02 is not None:
    norm_image = normalize_image(imageB02)
    blurred = apply_gaussian_blur(norm_image)
    edges = detect_edges(blurred)
    display_images(norm_image, edges)