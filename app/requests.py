import requests



quote_url=None

def config_request(app):
    global quote_url
    quote_url=app.config['url']

def get_quote():
    """
    Function to consume http request and return a Quote class instance
    """
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()

    print(response)

    return response