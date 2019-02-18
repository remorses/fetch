

### strategy

class Session():

    def __init__(self):
        opener = OpenerDirector()
        opener.add_handler(HTTPCookieProcessor())
        opener.add_handler(ProxyHandler(proxies=proxies)
        opener.add_headers = [...]
        self.opener = opener

    def request(self, method, url, data, headers, ):
        req = Request(...)
        res = self.opener.open(req, timeout)
        return res
        

# .open returns http.client.HTTPResponse
    class HTTPResponse(io.BufferedIOBase, BinaryIO):
        msg = ...  # type: HTTPMessage
        headers = ...  # type: HTTPMessage
        version = ...  # type: int
        debuglevel = ...  # type: int
        closed = ...  # type: bool
        status = ...  # type: int
        reason = ...  # type: str
        read()
        info().get_content_type() -> email.charset.Charset
        


### decode the response and make json
req=urllib.request.urlopen(URL)
charset=req.info().get_content_charset() or 'utf-8'
# content=req.read().decode(charset)
return json.load(req, encoding=charset)


### send json
data = json.dumps(...)
req = Request(url, data, {'Content-Type': 'application/json', 'Content-Length': len(data)})



# cookies

from urllib.request import build_opener, HTTPCookieProcessor, Request
url = 'https://www.cell.com/cell-metabolism/fulltext/S1550-4131(18)30630-2'
cj = http.cookiejar.CookieJar()

# Defining a handler for later http operations with cookies(cj).
urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))




# proxies
proxy_support = urllib.request.ProxyHandler({
'http' : 'http://user:pass@server:port',
'https': 'https://...'}
)
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)


### url query
url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
   the_page = response.read()




### headers
url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
   the_page = response.read()





### no connection error
except urllib.error.URLError as e:
          e.reason





### not 200 responses
except urllib.error.HTTPError as e:
          e.code
print(http.server.BaseHTTPRequestHandler.responses[e.code])




### ssl 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'google.com'
html = urllib.request.urlopen(url, context=ctx).read()