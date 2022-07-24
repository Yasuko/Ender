
from array import array
import glob
from typing_extensions import Self

class file_helper():

    '''
    @path string パス
    '''
    def __init__(self, path: str) -> None:
        if path != '':
            self._path = path
        else:
            self._path = './'

    @property
    def setPath(self, path: str) -> Self:
        self._path = path
        return self
    '''
    ファイル一覧を取得
    @path string パス default('')

    引数で渡されたパスに存在するファイル一覧を返す
    引数がない場合はインスタンス作成時のデフォルトパスのファイル一覧を返す
    '''
    def listFiles(self, path: str = '') -> list:
        if path == '' :
            files = glob.glob(self.path + '*')
        else:
            files = glob.glob(path + '*')
        return files

