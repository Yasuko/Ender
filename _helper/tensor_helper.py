import tensorflow as tf
from tensorflow import keras

class TensorHelper():
    def __init__(self, path) -> None:
        if path != '':
            self.path = path
        else:
            self.path = './'
    '''
    '''
    def loadModel(self, model = 'model.h5'):
        self.load_model = keras.models.load_model(self.path + 'enter_model_mfcc.h5')
    '''
    読み込んだモデルの評価を実施
    '''
    def evaluate(self, test, lavel):
        self.load_model.evaluate(test, lavel, verbose=1)
    '''
    推論を実施
    @data 
    '''
    def predict(self, data):
        return self.load_model.predict(data, batch_size=32, verbose=0, steps=None)
    
    def summary(self):
        self.load_model.summary()