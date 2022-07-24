# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
音データをMFCC化 → 画像データ化


'''


import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _helper import record
from _helper import toImage

RATE = 44100
CHUNK = 2**12
TIME = 0.5
# 閾値
THRESHOLD = 40

r = record.AudioService(
    RATE,              # RATE
    1,                 # Channel
    1,                 # DeviceIndex
    CHUNK              # CHUNK bit
)

# 音の取込開始
r.audiostart()

cnt = 0

while True:
    s = r.reset()
    for i in range(0, int(RATE / CHUNK * TIME)):
        data = r.getAudioData()
        s = r.stack(s, data) # 水平方向に配列を結合

    rms = r.gather_data(s)
    dec = r.to_db(rms, 20e-6)
    if dec >= THRESHOLD:
        print(s.shape)
        unko = toImage.toMfcc(s, RATE)
        print(unko.shape)
        toImage.npToImage(unko, './cap2/image' + str(cnt))

        cnt += 1

    # 最大1000回検出したら終了
    if cnt > 1000:
        break

r.audiostop()
