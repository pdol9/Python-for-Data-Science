from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def rotate_counter_clockwise(img) -> np.ndarray:
    """ Manual rotation of image in counter clockwise direction. """

    height, width, channels = img.shape
    rotated = np.zeros((width, height, channels), dtype=img.dtype)

    for y in range(height):
        for x in range(width):
            rotated[width - 1 - x][y] = img[y][x]

    return rotated


def crop_img(img: np.ndarray) -> np.ndarray:
    """Crop image. """
    zoomed = img[100:500, 450:850]

    return zoomed


if __name__ == "__main__":
    try:
        img = ft_load("animal.jpeg")
        cropped_img = crop_img(img)
        rotated = rotate_counter_clockwise(cropped_img)
        gray = np.mean(rotated, axis=2).astype(np.uint8)
        print("New shape after Transpose: ", gray.shape)
        print(gray)

        plt.imshow(gray, cmap="gray")
        plt.savefig("rotated.png")

    except Exception as e:
        print(f"Error: {e}")
