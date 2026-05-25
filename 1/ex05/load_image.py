import cv2
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image, print its format and RGB pixel content.

    Args:
        path (str): Path to the image.

    Returns:
        np.ndarray: Image pixels in RGB format.

    Raises:
        Exception: If the image cannot be loaded or format is invalid.
    """

    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")

        valid_ext = (".jpg", ".jpeg")
        if not path.lower().endswith(valid_ext):
            raise ValueError("Only JPG and JPEG formats are supported")

        image = cv2.imread(path)

        if image is None:
            raise FileNotFoundError(f"Cannot load image: {path}")

        # OpenCV loads as BGR -> convert to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        print(f"Image format: {path.split('.')[-1].upper()}")
        print(f"Shape: {image_rgb.shape}")
        print("Pixel content (RGB):")
        print(image_rgb)

        return image_rgb

    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    ft_load("landscape.jpg")
