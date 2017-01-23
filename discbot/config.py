# Reads config/config.ini and performs sanity checks

class Config(object):

    config = None

    def __init__(self, path='config/config.ini'):
        if not self.config:
            print("[WARNING] Loading placeholder config")

            # this has to be replaced by reading the actual .ini config file
            with open(path, 'r') as cfg:
                token = cfg.readline().rstrip()
                initial_channel = cfg.readline().rstrip()
                default_playlist = cfg.readline().rstrip()
            Config.config = {
                'token': token,
                'initial_channel': initial_channel,
                'default_playlist': default_playlist
            }

    def __getattr__(self, name):
        return self.config[name]

    def __setattr__(self, name, value):
        print("[WARNING] Overriding config value")
        self.config[name] = value

conf = Config()
