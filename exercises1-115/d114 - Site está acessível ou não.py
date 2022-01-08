import urllib
import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('Deu erro!')
else:
    print('Deu certo!')
    print(site.read())
