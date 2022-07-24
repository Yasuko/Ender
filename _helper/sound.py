import simpleaudio as sa

'''
エンダーを鳴らすだけのヘルパー
'''
def play(sound):
    wave_obj = sa.WaveObject.from_wave_file(sound)
    play_obj = wave_obj.play()
    play_obj.wait_done()

