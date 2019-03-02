import urllib.request

password="APS_._113920"

def send_to_twitter(msg):
    password_manager = urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API",
                   "https://twitter.com/statuses", "Flyhieeofficial", password)
    http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener = urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params = urllib.parse.urlencode( {'status': msg} )
    params = params.encode('utf-8')
    resp = urllib.request.urlopen("https://twitter.com/statuses/update.json", params)
    resp.read().decode('utf-8')

send_to_twitter("Welcome!")
