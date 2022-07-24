import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _helper import flask

if __name__ == '__main__':
    flask.run()
