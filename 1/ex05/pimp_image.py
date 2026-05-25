import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Invert image colors.
    """
    inverted = 255 - array

    plt.figure()
    plt.axis("off")
    plt.imshow(inverted)
    plt.savefig("invert.png", bbox_inches="tight", pad_inches=0)

    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keep red channel only.
    """
    red = array.copy()

    red[:, :, 1] = red[:, :, 1] * 0
    red[:, :, 2] = red[:, :, 2] * 0

    plt.axis("off")
    plt.imshow(red)
    plt.savefig("red.png", bbox_inches="tight", pad_inches=0)
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keep green channel only.
    """
    green = array.copy()

    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]

    plt.axis("off")
    plt.imshow(green)
    plt.savefig("green.png", bbox_inches="tight", pad_inches=0)
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keep blue channel only.
    """
    blue = array.copy()

    blue[:, :, 0] = 0
    blue[:, :, 1] = 0

    plt.axis("off")
    plt.imshow(blue)
    plt.savefig("blue.png", bbox_inches="tight", pad_inches=0)
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Convert image to grayscale.
    """
    grey = array.copy()

    grey = (grey[:, :, 0] / 3) + \
           (grey[:, :, 1] / 3) + \
           (grey[:, :, 2] / 3)

    plt.axis("off")
    plt.imshow(grey, cmap="gray")
    plt.savefig("grey.png", bbox_inches="tight", pad_inches=0)
    return grey.astype(np.uint8)
