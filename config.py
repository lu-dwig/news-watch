import os
# from distutils.debug import DEBUG
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY=os.environ.get("API_KEY")
    SECRET_KEY=os.environ.get("SECRET_KEY")
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources?country=us&category={}&API_KEY={}'
    NEWS_ARTICLES_APL_URL='https://newsapi.org/v2/everything?q={}&API_KEY={}'
    SOURCE_ARTICLES_URL='https://newsapi.org/v2/everything?sources={}&API_KEY='


class ProdConfig(Config):
    DEBUG =  False
class DevConfig(Config):
    DEBUG = True
    

config_options = {
'production': ProdConfig,
'development':DevConfig

}