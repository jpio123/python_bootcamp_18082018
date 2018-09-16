import urllib.request
import json

f = urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/a?format=json")
print(f.status)
data = f.read()
print(data)
data = json.loads(data)
print(data)


kursy = data[0]['rates']

for kurs in kursy:
    print(f"{kurs['currency']} - {kurs['code']} - {kurs['mid']}")