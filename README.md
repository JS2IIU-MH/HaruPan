# HaruPan
HaruPanどんなツールなのでしょうか

![](https://byob.yarr.is/JS2IIU-MH/HaruPan/passing_lints)
![](https://byob.yarr.is/JS2IIU-MH/HaruPan/time1)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)


## files

| file | description |
|---|---|
| [`main/count_circle.py`](main/count_circle.py) | 円を検出。OpenCV利用 |
| [`utils/heic_to_jpeg.py`](utils/heic_to_jpeg.py) | HEIC -> JPEG変換 |
| [`utils/image_preprocess.py`](utils/image_preprocess.py) | データセットの元となる画像を前処理する |
| [`utils/gaussian_filter.py`](utils/gaussian_filter.py) | ガウシアンフィルタ |
| [`sample_image/sampledata_listing.py`](sample_image/sampledata_listing.py) | `sample_image`フォルダ以下にあるイメージファイルのリストを作成する。リストは`sample_image/image_list_####.csv` |

## Resources

|directory | description |
|---|---|
| [`sample_image`](sample_image) | シールの元データ。1つ1つのシールに切り取られている状態。サイズ不定。カラー。 |

## メモ
### 学習用画像セットの準備
- 元のJPEGファイルを各種処理してuint8のndarrayに変換した後に画像ファイルとして保存する。
  - `Image.fromarray()`にndarrayを渡すとPIL.Imageに変換される
  - PIL.Imageのsave()メソッドで画像ファイルとして保存
  - 画像ファイルフォーマットはsave()の引数に指定したファイル名から自動で判定する
  - [Python, NumPyで画像処理（読み込み、演算、保存） | note.nkmk.me](https://note.nkmk.me/python-numpy-image-processing/)

- [画像認識の基礎から応用まで: Pythonで学ぶ機械学習 - AI・データサイエンス情報館](https://data-science.media/machine-learning/python-image-recognition/)
- [OpenCV 入門：画像処理・画像認識・機械学習の実装を徹底解説（全実装コード公開）](https://www.codexa.net/opencv_python_introduction/)
- [Pythonの画像処理ライブラリPillow(PIL)の使い方 | note.nkmk.me](https://note.nkmk.me/python-pillow-basic/)
- [機械学習を用いた画像処理の全て｜4種の処理手法・活用事例を解説 | AI専門ニュースメディア AINOW](https://ainow.ai/2022/06/28/266114/)
- [画像を読み込んで前処理する  |  TensorFlow Core](https://www.tensorflow.org/tutorials/load_data/images?hl=ja)
- [ランチョス法 - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%A9%E3%83%B3%E3%83%81%E3%83%A7%E3%82%B9%E6%B3%95)

- 画像処理ライブラリ Python Image Library: PIL
  - インポート：`from PIL import Image`
  - 読み込み：`img = Image.open('path/img.jpg')`

## 学習させる
- scikit-learnをつかう
- 全体の流れはこちらを参照
  - [画像認識の基礎から応用まで: Pythonで学ぶ機械学習 - AI・データサイエンス情報館](https://data-science.media/machine-learning/python-image-recognition/)
  
### 学習用、テスト用データ分割
- sklearn.model_selection.train_test_splitという関数を使って、データを学習用とテスト用に分ける
  - `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)`
  - [sklearn.model_selection.train_test_split — scikit-learn 1.4.2 documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

- [scikit-learnのtrain_test_split関数を使用してデータを分割する - AI人工知能テクノロジー](https://newtechnologylifestyle.net/rain_test_split%E9%96%A2%E6%95%B0%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%A6%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92%E5%88%86%E5%89%B2%E3%81%99%E3%82%8B/)
- [【サンプルコード付き】画像認識をPython×機械学習で実装していこう！｜スタビジ](https://toukei-lab.com/python-image#i)

### モデルの選択

## 参考
### HEIC -> JPEG
- [pillow-heif · PyPI](https://pypi.org/project/pillow-heif/)
- [Python_HEICファイルで保存された画像をJEPGに変換する　#431｜モリユウキ|YM202110](https://note.com/ym202110/n/n9c9f6ebb7a9a)

### 二値化
- [OpenCV-Pythonで画像処理　～二値化～ #Python - Qiita](https://qiita.com/ToppaD/items/c0bd354bc7dfcc4318a4)
- [【Python・OpenCV】適応的閾値処理による二値化(cv2.adaptiveThreshold)](https://www.codevace.com/py-opencv-adaptivethreshold/)


### 円検出
- [OpenCVのfindContours関数を使った画像の輪郭検出　画像処理｜OpenCV オープンソースのすすめ｜株式会社アルゴ](https://www.argocorp.com/OpenCV/imageprocessing/opencv_find_contours.html)
- [[OpenCV] 円を検出する #Python - Qiita](https://qiita.com/kotai2003/items/ebfd07b89a0de6335598)

### 機械学習
- [Pythonを使った機械学習と画像認識の完全ガイド：基礎から応用まで | Reinforz Insight](https://reinforz.co.jp/bizmedia/7415/)
- [kerasを使ってみよう #Python - Qiita](https://qiita.com/iss-f/items/b12308b44376ba69ac6a)
- [Keras: Deep Learning for humans](https://keras.io/)
- [深層学習用ライブラリKeras入門](https://indico2.riken.jp/event/2492/attachments/4803/5587/Tanaka_Lecture.pdf)

### 学習用画像セット
- [NNCチュートリアル：画像分類用データセットを作成するには - YouTube](https://www.youtube.com/watch?v=v6Rr6IODwK4)
- [機械学習向けのデータセットの作り方とは？手順や注意点を解説 | TRYETING Inc.（トライエッティング）](https://www.tryeting.jp/column/2663/)
- [画像を扱う機械学習のためのデータセットまとめ #機械学習 - Qiita](https://qiita.com/leetmikeal/items/7c0d23e39bf38ab8be23): 利用できそうないろいろなデータセットをまとめたページ。

#### アノテーション
- [AIアノテーションツールの比較11選。何ができるようになる？｜アスピック](https://www.aspicjapan.org/asu/article/16061)
- [画像アノテーションの基本と効果的な手法まとめ - TechSuite Blog](https://techsuite.biz/image-annotation/#index_id14)
  - （1）Labelbox: Labelboxは、クラウド上でアノテーション作業を行うことができる無料のツールです。使いやすいインターフェースと豊富な機能が魅力で、画像アノテーションだけでなく、動画やテキストのアノテーションも可能です。
  - （2）VGG Image Annotator (VIA): VIAは、オックスフォード大学のVGGグループが開発した、オープンソースの画像アノテーションツールです。Webブラウザ上で動作し、インストール不要で使える点が特徴です。画像アノテーションに加えて、動画アノテーションもサポートしています。