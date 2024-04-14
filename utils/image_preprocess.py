''' データセットの元となる画像を前処理する '''

import glob
import os
import re

import numpy as np
from PIL import Image, ImageFilter

# 処理後の画像サイズ
IMG_ROWS, IMG_COLS = 28, 28

def img_preprocess(filename, outfilename):
    # ロード
    img = Image.open(filename)
    # リサイズ
    img = img.resize((IMG_ROWS, IMG_COLS), Image.LANCZOS)
    # グレースケール変換
    img = img.convert('L')
    # uint8
    img = np.array(img, dtype=np.uint8)

    if not os.path.isdir(os.path.split(outfilename)[0]):
        os.mkdir(os.path.split(outfilename)[0])
    # Save
    Image.fromarray(img).save(outfilename)


    return img

def main():
    DESTINATION_DIR = 'processed_image'

    if not os.path.isdir(DESTINATION_DIR):
        os.mkdir(DESTINATION_DIR)

    files = glob.glob('sample_image/*/*.jpg')

    for file in files:
        outfilename = re.sub(r'sample_image', DESTINATION_DIR, file)
        img_preprocess(file, outfilename)


if __name__ == '__main__':
    main()
