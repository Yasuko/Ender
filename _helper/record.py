import pyaudio
import numpy as np
import matplotlib.pyplot as plot

class AudioService():

    def __init__(self, rate, channels, device_index, chunk):
        self.RATE       = rate
        self.CHANNELS   = channels
        self.deviceIndex = device_index
        self.CHUNK      = chunk

    '''
    オーディオストリームを開始
    '''
    def audiostart(self) -> None:
        self.audio = pyaudio.PyAudio() 
        self.stream = self.audio.open(
                            format = pyaudio.paInt16,
                            rate = self.RATE,
                            channels = self.CHANNELS, 
                            input_device_index = self.deviceIndex,
                            input = True,
                            frames_per_buffer = self.CHUNK)

    '''
    オーディオストリームを止める
    '''
    def audiostop(self) -> None:
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    '''
    サウンドデータを取得、CHUNK(ビット指定)単位でオーディオストリームから音を取得
    format（pyaudio.paInt6）を使用した場合に[-32768, 32768]の範囲の数値になるため
    32768で割ることで1を最大とした正規化を行う
    正規化された数値をint16の制度で数値化したデータを返す
    '''
    def getAudioData(self) -> float:
        audio = self.stream.read(self.CHUNK, exception_on_overflow = False)
        return np.frombuffer(audio, dtype="int16") / float((np.power(2, 16) / 2) - 1)

    '''
    オーディオストリームからデータを取得し
    pngデータに保存

    @name string 保存ファイル名 default('plot_audio')
    '''
    def read_plot_data(self, name='plot_audio') -> None:
        data = self.stream.read(self.CHUNK)
        audiodata = np.frombuffer(data, dtype='int16')
        
        plot.plot(audiodata)
        plot.grid()
        plot.savefig(name + '.png')

    '''
    オーディオデータの取得開始
    '''
    def record(self) -> None:
        (audio, stream) = self.audiostart()
        
        while True:
            try:
                self.read_plot_data(stream)
            except KeyboardInterrupt:
                break

        self.audiostop(audio,stream)
    '''
    音データをデシベルに変換し返す
    '''
    def to_db(self, x: float, base: int = 1) -> float:
        y=20*np.log10(x/base)
        return y
    '''
    オーディオデータ配列を水平方向に結合して返す

    @s numpy 結合元numpy配列
    @data numpy 結合されるnumpy配列
    '''
    def stack(self, s: list, data: int) -> list:
        return np.hstack([s, data])

    '''
    # np.mean 行列ごとの平均を算出
    # np.sqrt ルート計算

    データを集計し返す
    @s numpy 集計対象のnumpy配列
    '''
    def gather_data(self, s: list) -> list:
        return np.sqrt(np.mean([data * data for data in s]))

    '''
    空のnumpy配列を返す
    '''
    def reset(self):
        return np.empty(0)