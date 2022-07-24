
# Enterキーを判別し、エンダーする

# システム構成

## Jupyter
* ニューラルネットの学習を行う
* 学習済みのモデルの検証を行う

## py_inferance
* 学習済みモデルを使用し、キーの判別を行う
* Flaskを使用したAPIサーバー形式で行う
  
## py_recorder
* マイク音声をMFCCの画像形式でディレクトリに保存
* マイク音声をwavデータでディレクトリに保存
* マイクデータをMFCC形式で推論サーバーに投げる
* マイクデータを波形データを配列に変換し推論サーバーに投げる
* 推論結果を判定しエンダーを鳴らす



# 学習済みモデルデータ等
### [wav 全結合モデル](https://yasukosan-my.sharepoint.com/:u:/g/personal/masayuki_yasukosan_onmicrosoft_com/EZv5CD6ec4FCkGfAns2p0iEB74rdmKgpT0u1_LkW_tfPHQ?e=67HiUd)
### [mfcc モデル](https://yasukosan-my.sharepoint.com/:u:/g/personal/masayuki_yasukosan_onmicrosoft_com/EcnapzshUmtLk74c0CDMImcB00rKttCmlpIVekGTU9Vn9Q?e=Qr0eIv)

# 以下更新中



