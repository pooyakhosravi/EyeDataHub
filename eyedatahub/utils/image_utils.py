"""Image utility functions for EyeDataHub."""
from __future__ import annotations

from pathlib import Path
from typing import List, Optional, Tuple, Union

import numpy as np
from PIL import Image


def resize_image(
    image: Union[Image.Image, np.ndarray],
    size: Tuple[int, int],
    resample: int = Image.BILINEAR,
) -> Image.Image:
    """
    Resize an image to the given (width, height).

    Args:
        image: PIL Image or numpy array
        size: Target (width, height)
        resample: PIL resampling filter

    Returns:
        Resized PIL Image (RGB)
    """
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    return image.convert("RGB").resize(size, resample)


def pad_to_square(
    image: Union[Image.Image, np.ndarray],
    fill: int = 0,
) -> Image.Image:
    """
    Pad an image with constant fill to make it square.

    Args:
        image: PIL Image or numpy array
        fill: Fill pixel value (0 = black)

    Returns:
        Square PIL Image (RGB)
    """
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image).convert("RGB")
    else:
        image = image.convert("RGB")

    w, h = image.size
    if w == h:
        return image

    side = max(w, h)
    new_img = Image.new("RGB", (side, side), (fill, fill, fill))
    offset_x = (side - w) // 2
    offset_y = (side - h) // 2
    new_img.paste(image, (offset_x, offset_y))
    return new_img


def center_crop(
    image: Union[Image.Image, np.ndarray],
    size: Tuple[int, int],
) -> Image.Image:
    """
    Centre-crop an image to the given (width, height).

    Args:
        image: PIL Image or numpy array
        size: Target (width, height)

    Returns:
        Cropped PIL Image
    """
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)

    w, h = image.size
    crop_w, crop_h = size
    left = max(0, (w - crop_w) // 2)
    top = max(0, (h - crop_h) // 2)
    right = left + crop_w
    bottom = top + crop_h
    return image.crop((left, top, right, bottom))


def normalize_image(
    image: np.ndarray,
    mean: Tuple[float, float, float] = (0.485, 0.456, 0.406),
    std: Tuple[float, float, float] = (0.229, 0.224, 0.225),
) -> np.ndarray:
    """
    Normalise a float image array with ImageNet-style mean/std.

    Args:
        image: Float array of shape (H, W, 3) with values in [0, 1]
        mean: Per-channel mean
        std: Per-channel standard deviation

    Returns:
        Normalised float array of same shape
    """
    image = np.asarray(image, dtype=np.float32)
    if image.max() > 1.0:
        image = image / 255.0

    mean_arr = np.array(mean, dtype=np.float32)
    std_arr = np.array(std, dtype=np.float32)
    return (image - mean_arr) / std_arr


def load_image_as_array(
    path: Union[str, Path],
    target_size: Optional[Tuple[int, int]] = None,
    normalise: bool = False,
) -> np.ndarray:
    """
    Load an image from disk and optionally resize and normalise it.

    Args:
        path: Path to image file
        target_size: If provided, resize to (width, height)
        normalise: If True, divide by 255 to get float values in [0, 1]

    Returns:
        numpy array of shape (H, W, 3)
    """
    img = Image.open(path).convert("RGB")
    if target_size is not None:
        img = img.resize(target_size, Image.BILINEAR)
    arr = np.array(img, dtype=np.float32 if normalise else np.uint8)
    if normalise:
        arr /= 255.0
    return arr


def apply_clahe(
    image: Union[Image.Image, np.ndarray],
    clip_limit: float = 2.0,
    tile_grid_size: Tuple[int, int] = (8, 8),
) -> Image.Image:
    """
    Apply CLAHE (Contrast Limited Adaptive Histogram Equalisation) to a fundus image.

    Enhances vessel contrast. Applies to the L-channel in LAB colour space.

    Args:
        image: PIL Image or numpy array (RGB)
        clip_limit: CLAHE clip limit
        tile_grid_size: Grid size for CLAHE

    Returns:
        Contrast-enhanced PIL Image (RGB)
    """
    try:
        import cv2
    except ImportError:
        raise ImportError(
            "opencv-python-headless is required for CLAHE. "
            "Run: pip install opencv-python-headless"
        )

    if isinstance(image, Image.Image):
        arr = np.array(image.convert("RGB"))
    else:
        arr = np.asarray(image)

    if arr.dtype != np.uint8:
        arr = (np.clip(arr, 0, 1) * 255).astype(np.uint8)

    lab = cv2.cvtColor(arr, cv2.COLOR_RGB2LAB)
    l_channel, a_channel, b_channel = cv2.split(lab)

    clahe = cv2.createCLAHE(
        clipLimit=clip_limit, tileGridSize=tile_grid_size
    )
    l_eq = clahe.apply(l_channel)

    lab_eq = cv2.merge((l_eq, a_channel, b_channel))
    result = cv2.cvtColor(lab_eq, cv2.COLOR_LAB2RGB)
    return Image.fromarray(result)


def create_image_grid(
    images: List[Union[Image.Image, np.ndarray]],
    n_cols: int = 4,
    cell_size: Tuple[int, int] = (224, 224),
    padding: int = 4,
    background: Tuple[int, int, int] = (240, 240, 240),
) -> Image.Image:
    """
    Arrange images in a grid.

    Args:
        images: List of PIL Images or numpy arrays
        n_cols: Number of columns in the grid
        cell_size: (width, height) for each cell
        padding: Pixel gap between cells
        background: Background fill colour (RGB)

    Returns:
        PIL Image with all images arranged in a grid
    """
    n = len(images)
    n_rows = (n + n_cols - 1) // n_cols
    cell_w, cell_h = cell_size

    total_w = n_cols * cell_w + (n_cols + 1) * padding
    total_h = n_rows * cell_h + (n_rows + 1) * padding

    grid = Image.new("RGB", (total_w, total_h), background)

    for idx, img in enumerate(images):
        if isinstance(img, np.ndarray):
            img = Image.fromarray(img)
        img = img.convert("RGB").resize(cell_size, Image.BILINEAR)

        row = idx // n_cols
        col = idx % n_cols
        x = padding + col * (cell_w + padding)
        y = padding + row * (cell_h + padding)
        grid.paste(img, (x, y))

    return grid
