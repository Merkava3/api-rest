class Config:
    pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    Debug:bool = True
    

Config = {
    'development': DevelopmentConfig
}