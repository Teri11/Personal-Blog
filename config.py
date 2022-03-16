import os
class Config:
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/augustine'
 
  #Email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  #PHOTOS UPLOAD CONFIGURATION
  url = 'http://quotes.stormconsultancy.co.uk/random.json'
  UPLOADED_PHOTOS_DEST = 'app/static/photos'
  @staticmethod
  def init_app(app):
        pass
class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  
class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/augustine'
  DEBUG = True

class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/augustine_test'

config_options = {
  'production':ProdConfig,
  'development':DevConfig,
  'test':TestConfig
}