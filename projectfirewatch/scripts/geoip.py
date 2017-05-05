import requests, json

def get_ip():
	'''finds the useres IP address and returns it.'''
	ipdata = requests.get('https://jsonip.com/')
	ipresp = ipdata.json()
	ip = ipresp.get('ip')
	return ip


def geoip(ip):
	'''retireves and reports users geoip information'''
	resp = requests.get('http://freegeoip.net/json/' + ip)
	data = resp.json()
	return(data)

def geoip_coords(ip):
    '''retrieves and reports users geoip infromations limited down to 
	location coordinates only'''
    resp = requests.get('http://freegeoip.net/json/' + ip)
    data = resp.json()
    lat = data.get('latitude')
    lng = data.get('longitude')
    return(lat,lng)

ip = get_ip()
lat, lng = geoip_coords(get_ip())
print(ip, lat, lng)

upper = lat + 25
right = lng + 25
lower = lat - 25
left =  lng - 25


print('upper = ' + str(upper))
print('lower = ' + str(lower))
print('left = ' + str(left))
print('right = ' + str(right))