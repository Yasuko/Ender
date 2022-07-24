import numpy as np

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