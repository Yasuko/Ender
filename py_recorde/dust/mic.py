# -*- coding: utf-8 -*-
#!/usr/bin/env python

# ライブラリの読込
import pyaudio
import wave
import numpy as np
from datetime import datetime

# 音データフォーマット
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 0.35

# 閾値
threshold = 0.2
threshold_brst = 0.9

# 音の取込開始
p = pyaudio.PyAudio()
stream = p.open(format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    frames_per_buffer = chunk
)

cnt = 0

while True:
    # 音データの取得
    data = stream.read(chunk)
    # ndarrayに変換
    x = np.frombuffer(data, dtype="int16") / 32768.0

    # 閾値以上の場合はファイルに保存
    if x.max() > threshold:
        filename = datetime.today().strftime("%Y%m%d%H%M%S") + ".wav"
        print(cnt, filename)

        # 2秒間の音データを取込
        all = []
        all.append(data)
        for i in range(0, int(RATE / chunk * int(RECORD_SECONDS))):
            if x.max() > threshold_brst:
                print('I BURST!!!') 
            data = stream.read(chunk)
            all.append(data)
        data = b''.join(all)

        # 音声ファイルとして出力
        out = wave.open(filename,'w')
        out.setnchannels(CHANNELS)
        out.setsampwidth(2)
        out.setframerate(RATE)
        out.writeframes(data)
        out.close()

        print("Saved.")

        cnt += 1



    # 5回検出したら終了
    if cnt > 5:
        break

stream.close()
p.terminate()

'''
しきい値を超えたマイク音データをwavファイルに保存

・録音はモノラル記録
・マイク入力を直接、CSV、MFCC等に変換するコードを用意したので
  現段階では不要
'''
