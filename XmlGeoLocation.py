import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

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
    # print the url
    print('Retrieving', url)
    
    # url open to get a handle
    uh = urllib.request.urlopen(url, context=ctx)
    # read the whole document
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    # Because data is utf-8, it is necesary to decode it into unicode
    print(data.decode())
    # Parse data into string
    tree = ET.fromstring(data)

    # Find all tags called result
    results = tree.findall('result')
    # Gets the position 0 of results, it looks for geometry into that object, then go to location and 
    # pull out lat
    lat = results[0].find('geometry').find('location').find('lat').text
    # Gets the position 0 of results, it looks for geometry into that object, then go to location and 
    # pull out lng
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)