#encoding:UTF-8
import urllib.request

def download(url):
    print('downloading:'+url)
    try:
        html=urllib.request.urlopen(url).read().decode('utf-8')
    except urllib.request.URLError as e:
        print('download error:'+e.reason)
        html=None
    return html

print(download('http://119.29.176.196'))