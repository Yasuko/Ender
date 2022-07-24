# -*- coding: utf-8 -*-
#!/usr/bin/env python

# ライブラリの読込

import numpy as np
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _helper import record
from _helper import request
from _helper import sound
from _lib import tensor_convert

RATE = 44100
CHUNK = 2**12
TIME = 0.5
# 閾値
THRESHOLD = 40

r = record.AudioService(
    RATE,              # RATE
    1,                  # Channel
    1,                  # DeviceIndex
    5120                # CHUNK
)

# 閾値
threshold = 0.1

# 音の取込開始
r.audiostart()

cnt = 0

while True:
    # 音データの取得
    data = r.getAudioData()

    # ndarrayに変換
    x = np.frombuffer(data, dtype="int16") / 32768.0

    # 閾値以上の場合はファイルに保存
    if x.max() > threshold:
        # 2秒間の音データを取込
        all = []
        all.append(data)
        for i in range(0, int(44100 / 5120 * int(0.1))):
            data = r.getAudioData()
            all.append(data)
        _data = np.frombuffer(data, dtype="int16") / 32768.0

        _x = tensor_convert.min_max(_data)
        hoge = request.call(json.dumps({'tensor' : _x.tolist()}))
        h = json.loads(hoge.content)
        print(h)
        if (h['inference'][0][1] >= 0.8):
            sound.play('Enter.wav')

        cnt += 1

    # 5回検出したら終了
    if cnt > 5:
        break

r.audiostop()

'''
パーセプトロン向け音変換　テスト１

・しきい値判定と録音部分で音データの取得に無駄処理あり
・オーディオデータのスタックの考えに誤りがあり
  必要な長さのオーディオデータで判定が出来ていない
  「録音 → 待機」の切り替えに謎の待ち時間が出る原因になっている


'''
