import requests

def get_quotes():
    #generate request url
    url = 'https://www.stands4.com/services/v2/quotes.php?uid=8849&tokenid=gp02AqhX72ek1ULk&'
    url_searchtype = ('searchtype','RANDOM')
    url_query = ('','')
    url_format = ('format','json')
    url += url_searchtype[0] + '=' + url_searchtype[1] + '&' + url_format[0] + '=' + url_format[1]

    #send request
    response = requests.get(url)
    #convert response to json
    json = response.json()
    print(response.status_code)

    #extract quote and author from response
    #json = {'result': {'quote': 'Genius is a bend in the creek where bright water has gathered, and which mirrors the trees, the sky and the banks. It just does that because it is there and the scenery is there. Talent is a fine mirror with a silver frame, with the name of the owner engraved on the back.', 'author': 'Edgar Lee Masters'}}
    quote = json['result']['quote']
    author = json['result']['author']

    return quote, author