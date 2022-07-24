import librosa
import numpy as np
import matplotlib.pyplot as plt

'''
画像変換ヘルパー
'''
def toMfcc(sound: list, rate: int) -> list:
    # n_mfccでMFCCの次元数（特徴ベクトルの次元数）を指定している
    # 大きいほどより細かい表現が出来るが次元数が増えてしまうので通常は12～24が設定される
    return librosa.feature.mfcc(sound, rate, n_mfcc=20, dct_type=3)

def npToImage(data: list, name: str) -> None:
    array = np.reshape(data, data.shape)

    plt.imsave( name + '.jpg', array)
    