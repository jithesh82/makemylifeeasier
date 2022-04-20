#!/usr/bin/env python3

import requests
import ast
from datetime import datetime
import pickle

api_key="Qyfxrpj57mdMYbnY4d62Lq1dTyPAQtX4d"
new_york_key = 349727
def getData():
    url = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/349727?apikey=Qyfrj57dOMYDbnY4d62Lq1dTyPAQtX4d%20&details=true"

    r = requests.get(url)
    #print('request success', r.status_code)
    print(r.json(), file=open('/home/jk/jk/python/hourly_temp_nyc.txt', 'w'))
    #print(r.json(), file=open('/home/jk/jk/python/hourly_temp_nyc.json', 'w'))
    data = r.json()
    time_before = datetime.now()
    pickle.dump(time_now, open('/home/jk/jk/python/timebefore_accuweather.pickle', 'wb'))
    return data
time_now = datetime.now()
time_before = pickle.load(open('/home/jk/jk/python/timebefore_accuweather.pickle', 'rb'))
time_passed = (time_now - time_before).total_seconds()

if time_passed > 3600:
    print('getting data from web')
    data = getData()
else:
    print('getting data from file')
    data = open('/home/jk/jk/python/hourly_temp_nyc.txt').read()
    data = ast.literal_eval(data)
#data = list(data)
#print(type(data))
#print(len(data))

for key in data[0].keys():
    #print(key)
    #print(data[0]['Temperature'])
    #print(data[0]['RainProbability'])
    #print(data[0]['SnowProbability'])
    pass

print('time', "\t\t", 'temp', '\t', 'rain', '\t', 'snow', '\t', 'sky')
for i in range(len(data)):
    #print(data[i]['DateTime'])
    dT = data[i]['DateTime']
    #print(datetime.fromisoformat(dT).time().strftime("%I:%M%p"))
    timE = datetime.fromisoformat(dT).time().strftime("%I:%M%p")
    #print(data[i]['Temperature']['Value'])
    t_F = data[i]['Temperature']['Value']
    rain = data[i]['RainProbability']
    snow = data[i]['SnowProbability']
    iconphrase = data[i]['IconPhrase']
    t_C = (t_F  - 32) * (5/9)
    print(timE, "\t", "%0.2f" % t_C, '\t', rain, '\t', snow, '\t', iconphrase)

