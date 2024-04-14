''' サンプル画像データの一覧CSVを出力する '''

import datetime
import glob
import re

import pandas as pd


def gen_data_list_csv():

    # 出力するCSVのファイル名に日時を入れる
    now = datetime.datetime.now()
    date_str = now.strftime('%Y%m%d%H%M%S')

    csv_file = f'processed_image/image_list_{date_str}.csv'

    path_list = glob.glob('processed_image/*/*.jpg')
    point_list = []

    for f in path_list:
        res = re.search(r'point_(\d\.\d)', f)
        point_list.append(res.groups()[0])

    # リスト結合
    new_list = []
    for i in range(len(path_list)):
        new_list.append([path_list[i], point_list[i]])

    df = pd.DataFrame(new_list)
    df.columns = ['img_path', 'point']
    df.to_csv(csv_file)


def main():
    gen_data_list_csv()


if __name__ == '__main__':
    main()
