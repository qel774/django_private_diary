#開発環境固有の設定ファイル
"""
from .settings_common import *

ALLOWED_HOST = []

#ロギング
LOGGING = {
    'version': 1,
    'disable_existing_loggers':False,

    #ロギング
    'loggers':{
        #Djangoが利用するロガー
        'django':{
            'handlers':['console'],
            'level':'INFO',
        },
        #diaryアプリケーションが利用するロガー
        'diary':{
            'handlers':['console'],
            'level':'DEBUG',
        },
    },
    #ハンドラの設定
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev'
        },
    },
    #フォーマッタの設定
    'formatters':{
        'dev':{
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Lime:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}
"""