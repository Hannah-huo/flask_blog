import os
basedir = os.path.abspath(os.path.dirname(__file__))

class DevConfig = {
    db_uri: 'sqlite:///' + os.path.join(basedir,'data.sqlite')
}