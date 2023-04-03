from config import event_consumer_config as CFG
from src import flask_app

if __name__ == '__main__':
    flask_app.run(host=CFG['host'], port=CFG['port'], debug=CFG['debug'])
