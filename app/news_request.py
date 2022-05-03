import urllib.request,json
from .models import Articles,Sources
import os
import requests

api_key = None
s_url = None
art_url = None

def configure_request(app):
    global api_key,s_url,art_url
    api_key = app.config['API_KEY']
    articles_url = app.config['SOURCE_ARTICLES_URL']
    s_url = app.config['NEWS_API_BASE_URL']
    art_url = app.config['NEWS_ARTICLES_APL_URL']
    

def get_sources(category):
    """
    function that gets response from the api call
    """    
    sources_url = s_url.format(category,api_key)

    with urllib.request.urlopen(sources_url) as url:
        sources_data = url.read()
        response = json.loads(sources_data)

        sources_outcome = None

        if response['sources']:
            sources_outcome_items = response['sources']
            sources_outcome = process_new_sources(sources_outcome_items)
    return sources_outcome

