''' 学習 '''

import pandas as pd
from sklearn.model_selection import train_test_split

image_list_file = 'processed_image/image_list_20240413104832.csv'


def larning():

    # 学習用とテスト用データを分割する
    df = pd.read_csv(image_list_file, index_col=0)
    X = df.loc[:, 'img_path']
    y = df.loc[:, 'point']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2)


def main():
    larning()


if __name__ == '__main__':
    main()
