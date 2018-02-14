import requests
from datetime import date,timedelta
import time
from scipy.io.wavfile import write

# Random twice based on previous records
start = date(2006,3,11)
end = date.today()
num_days = (end-start).days

params = {'min':0,
'max':num_days,
'col':1,
'rnd':'new',
'format':'plain',
'num':1,
'base':10}

try:
	r = requests.get("https://www.random.org/integers", params)
	data = int(r.content)
except requests.exceptions.RequestException as e:
    print e
    sys.exit(1)

new_date = start + timedelta(data)
new_rnd = new_date.strftime('%Y-%m-%d')

# wav
params['rnd'] = new_rnd
params['col'] = 1
params['num'] = 4410
params['max'] = 32767
params['min'] = -32767

mat = []

for _ in range(15):
	try:
		r = requests.get("https://www.random.org/integers", params)
		data = r.content.splitlines()
	except requests.exceptions.RequestException as e:
	    print e
	    sys.exit(1)
	for line in data:
		num = int(line)
		mat.append(num)
	time.sleep(1)

write('test.wav', 22050, mat)