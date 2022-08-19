import urllib.parse
import re

data = b'name=Krabat&email=krabatua%40gmail.com&text=%D0%A2%D0%B5%D1%81%D1%82+%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D0%B5'

# data_parse = urllib.parse.unquote(re.sub(r'\+', ' ', data.decode()))
data_parse = urllib.parse.unquote_plus(data.decode(), encoding='utf-8')

data_parse = data_parse.split('&')
data_parse = [el.split('=') for el in data_parse]
data_parse = {key: value for key, value in data_parse}

print(data_parse)