from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
import cv2


def zoom(img: np.ndarray) -> None:
    """ 'Zoom' into the image and display information. """

    try:
        if img is None:
            raise ValueError("Empty image")

        # crop the image
        zoomed = img[100:500, 450:850]

        # grayscale
        zoomed = cv2.cvtColor(zoomed, cv2.COLOR_RGB2GRAY)

        print("New shape after slicing:", zoomed.shape)
        print(zoomed)

        # display with pixel scale
        plt.imshow(zoomed, cmap="gray")

        plt.xlabel("X axis (pixels)")
        plt.ylabel("Y axis (pixels)")
        plt.title("Zoomed Image")

        # optional tick spacing
        plt.xticks(range(0, 401, 50))
        plt.yticks(range(0, 401, 50))

        # save
        plt.savefig("zoom.png")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    try:
        img_arr = ft_load("animal.jpeg")
        zoomed = zoom(img_arr)

    except Exception as e:
        print(f"Error: {e}")
