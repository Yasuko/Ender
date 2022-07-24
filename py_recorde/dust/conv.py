# -*- coding: utf-8 -*-
from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt

from _helper import file
from _lib import csv

'''
データの平均を０とし、そこからの分布に丸める

'''
def zscore(x, axis = None):
    xmean = x.mean(axis=axis, keepdims=True)
    xstd  = np.std(x, axis=axis, keepdims=True)
    zscore = (x-xmean)/xstd
    return zscore

'''
データを最大が１、最小が０の範囲に丸め込む
大幅に外れた数値があると計算後の差が小さくなるため
実際の乖離情報が雲散することになる
'''
def min_max(x, axis=None):
    min = x.min(axis=axis, keepdims=True)
    max = x.max(axis=axis, keepdims=True)
    result = (x-min)/(max-min)
    return result

'''
ベクトルの正規化に向く
要素の合計が１になるように揃える正規化手法
３次元を２次元にといったようほうで役立つ

3次元配列で2次元配列ごとに正規化したい場合は
axis=(1,2)のように正規化したい２次元配列の軸(axis)番号を2つ指定
'''
def normalize(v, axis=-1, order=2):
    l2 = np.linalg.norm(v, ord = order, axis=axis, keepdims=True)
    l2[l2==0] = 1
    return v/l2


def npToString(np):
    txt = ''
    for x in np:
        txt = txt + str(x) + ','
    return txt

f = file.file_helper('../wave2/')
_file = f.listFiles()

data = np.arange(15523)
count = 0
f = open('./output_ather.txt', 'a')
for file in _file:
    # 音楽データの読み込み
    sound = AudioSegment.from_file(file, "wave")

    # NumPy配列に返還
    _data = np.array(sound.get_array_of_samples())
    #np.vstack((data, _data))
    
    f.write(npToString(min_max(_data)) + '\n')
    # ステレオ音声から片方を抽出
    x = min_max(_data[::sound.channels])

    #_csv = csv.csv_service()
    #_csv.writeCSV(x)

    print(x.shape)
    # グラフ化
    plt.plot(x[::10])
    plt.grid()
    plt.savefig('unko_ather.png')
'''
np.savetxt(
    './output.csv',
    data.reshape(len(_file), len(data)),
    delimiter=",")
'''
_csv = csv.csv_service()
_csv.writeCSV(data)

'''
録音済みのデータをcsvに変換

・録音と変換が同時に行えるサンプルを別で用意したため不要になる
・録音済みのwavデータをcsvに変換する場合には使える

'''

