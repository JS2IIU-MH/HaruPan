''' HEICをJPEGに変換する '''

import glob
import os

import pillow_heif
from PIL import Image


def list_heic_images(target_dir):
    ''' target_dirの中にあるHEICファイルをリストにする '''
    out_list = []

    if target_dir[-1] == '/':
        target_dir = target_dir[:-1]

    tmp_list = glob.glob(f'{target_dir}/*.heic')

    # エスケープシーケンス対応
    for f in tmp_list:
        out_list.append(f.replace("\\", "/"))

    return out_list


def heic2jpg(input_img_path, out_img_path):
    ''' Args:
        input_img_path: HEICファイルパス
        out_img_path: 出力JPEGファイルパス
    '''
    heic_img = pillow_heif.read_heif(input_img_path)[0]
    img = Image.frombytes(
        heic_img.mode,
        heic_img.size,
        heic_img.data,
        'raw',
        heic_img.mode,
        heic_img.stride,
    )
    img.save(out_img_path, 'JPEG')


def main():
    org_dir = 'ORG_IMG'
    dist_dir = 'OUT_IMG'

    if not os.path.isdir(dist_dir):
        os.mkdir(dist_dir)

    heic_files = list_heic_images(org_dir)

    if heic_files:
        for f in heic_files:
            basename_without_ext = os.path.splitext(os.path.basename(f))[0]
            heic2jpg(f, f'{dist_dir}/{basename_without_ext}.jpg')


if __name__ == '__main__':
    main()
