import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    # if no address is provided, get out of the loop
    if len(address) < 1: break

    # Dictionary to store key, address pairs
    parms = dict()
    # Assign key and address
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    
    # Concatenate the serviceurl and urllib.parse.urlencode(parms) to get the endpoint of the url
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    
    # url open to get a handle
    uh = urllib.request.urlopen(url, context=ctx)
    # read the whole document and decode it
    data = uh.read().decode()
    
    print('Retrieved', len(data), 'characters')

    # This is a trigger, necesary to evaluate the following if statement
    try:
        js = json.loads(data)
    except:
        js = None

    # As the json document is a dictionary, one of the objects is status, so if status is not 
    # present, or status is not ok, return a failure to retreive
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # The dumps() method takes de dictionary of arrays and print it with indentantion of 4
    print(json.dumps(js, indent=4))

    # Gets the position 0 of results, it looks for geometry into that object, then go to location and 
    # pull out lat
    lat = js['results'][0]['geometry']['location']['lat']
    # Gets the position 0 of results, it looks for geometry into that object, then go to location and 
    # pull out lng
    lng = js['results'][0]['geometry']['location']['lng']
    
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)