# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
音データ識別MFCCバージョン

オーディオデータを監視し、一定チャンクサイズ毎に
デシベル換算でしきい値を超える大きさの音が検出された場合に
MFCCに変換 → 画像化 → データをNumPyに変換 → 推測APIで推測 → 結果を判定しエンダー

'''

import numpy as np
import json
import sys
import os
from PIL import Image


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _helper import record
from _helper import request
from _helper import toImage
from _helper import sound

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

while True:
    s = r.reset()

    for i in range(0, int(RATE / CHUNK * TIME)):
        data = r.getAudioData()
        s = r.stack(s, data) # 水平方向に配列を結合

    rms = r.gather_data(s)      # 
    dec = r.to_db(rms, 20e-6)   # デシベル変換

    if dec >= THRESHOLD:
        # MFCCに変換
        mfcc = toImage.toMfcc(s, RATE)
        # 一回画像で保存
        toImage.npToImage(mfcc, './capcha')
        # 画像読み込み
        img = Image.open('./capcha.jpg')
        # リサイズ（拡大）
        img_ = np.asarray(img.resize([50,50]))
        np_img_ = img_.astype(np.float32)/255.0

        # 推測APIコール
        hoge = request.call(json.dumps({'tensor' : request.npToJson(np_img_)}))
        h = json.loads(hoge.content)
        # 80%以上Enterならエンダー
        if (h['inference'][0][1] >= 0.8):
            sound.play('Enter.wav')

r.audiostop()

