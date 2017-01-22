# Reads config/config.ini and performs sanity checks

class Config(object):

    config = None

    def __init__(self, path='config/config.ini'):
        if not self.config:
            print("[WARNING] Loading placeholder config")
            Config.config = {
                'token': 'tmp_token',
            }

    def __getattr__(self, name):
        return self.config[name]

    def __setattr__(self, name, value):
        print("[WARNING] Overriding config value")
        self.config[name] = value

conf = Config()
