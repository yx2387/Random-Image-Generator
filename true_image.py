import requests
from datetime import date,timedelta
from PIL import Image
import time

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

# bitmap
params['rnd'] = new_rnd
params['col'] = 3
params['num'] = 128*16*3
params['max'] = 255
mat = []

for _ in range(8):
	try:
		r = requests.get("https://www.random.org/integers", params)
		data = r.content.splitlines()
	except requests.exceptions.RequestException as e:
	    print e
	    sys.exit(1)
	for line in data:
		tup = tuple(map(int,line.split()))
		mat.append(tup)
	time.sleep(1)

im = Image.new("RGB",(128,128))
im.putdata(mat)
im.save('img.jpeg')
