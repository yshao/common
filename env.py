from event.jsonconfig import JsonConfig
class Env(object):
    param={'HOME':'c:/Users/Ping/Workspace/weathergit'}
    def __init__(self):
        ""
        d=JsonConfig('config.json')
        d2=dump_password('config.kbd')

        d.merge(d2)

        self.d=d
    @classmethod
    def getpath(self,param):
        return self.param[param]

    @classmethod
    def getConfig(self):
        return self.d