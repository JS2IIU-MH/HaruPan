''' gaussian filter '''

from PIL import Image
import numpy as np


def generate_gaussian_kernel(
        kernel_width: int,
        kernel_height: int,
        sigma: float):
    ''' generate gaussian kernel
        Args
            kernel_width, kernel_height: kwernel size (odd number)
            sigma: SD
        Returns
            kernel as np.ndarray
    '''

    # kernel size == even -> Assertion Error
    assert kernel_width % 2 == 1 and kernel_height % 2 == 1

    kernel = np.empty((kernel_height, kernel_width))

    for y in range(-(kernel_height // 2), kernel_height // 2 + 1):
        for x in range(-(kernel_width // 2), kernel_width // 2 + 1):
            # gaussian distribution
            h = -(x ** 2 + y ** 2) / (2 * sigma ** 2)
            h = np.exp(h) / (2 * np.pi * sigma ** 2)
            kernel[y + kernel_height // 2, x + kernel_width // 2] = h

    # normalization
    kernel /= np.sum(kernel)

    return kernel


def convolution(
        img: Image.Image,
        kernel: np.ndarray,
        x: int,
        y: int):
    ''' convolution apply to the single pixcel
        Args
            img: target image as Image.Image
            kernel: filter kernel
            x, y: coordination of kerbel center in the image
        Returns
            value
    '''

    width, height = img.size
    # numpy.ndarrayの形状（各次元のサイズ）はshape属性でタプルとして取得できる。
    kernel_height, kernel_width = kernel.shape[:2]

    value = 0

    for y_kernel in range(-(kernel_height // 2), kernel_height // 2 + 1):
        for x_kernel in range(-(kernel_width // 2), kernel_width // 2 + 1):
            # 画像の端からカーネルがはみ出る場合の処理
            x_img = max(min(x + x_kernel, width - 1), 0)
            y_img = max(min(y + y_kernel, height - 1), 0)

            h = kernel[y_kernel + kernel_height // 2,
                       x_kernel + kernel_width // 2]
            value += h * img.getpixel((x_img, y_img))

    return value


def apply_filter(img: Image.Image, kernel: np.ndarray):
    ''' 1枚の画像に対してフィルタを適用する '''

    width, height = img.size
    # filtered image to return
    img_filtered = Image.new(mode='L', size=(width, height))

    # 各画素の計算
    for y in range(height):
        for x in range(width):
            filtered_value = convolution(img, kernel, x, y)
            img_filtered.putpixel((x, y), int(filtered_value))

    return img_filtered


def main():
    kernel = generate_gaussian_kernel(5, 5, 1.3)

    img = Image.open('processed_image/point_0.5/001.jpg')

    img_filtered = apply_filter(img, kernel)
    img_filtered.save('filtered.jpg')


if __name__ == '__main__':
    main()
