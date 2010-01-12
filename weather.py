#! /usr/bin/env python

# Get the latest weather information for a station from the Australian Bureau of
# Meteorology website (www.gom.gov.au). Takes the URL of a web page containing a
# stations observations as the only arguement.

import sys
import urllib
import simplejson as json

if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except IndexError:
        sys.exit("Usage: weather.py url")

    data = json.load(urllib.urlopen(url))

    data = data["observations"]["data"][0]

    try:
        temp = data["press"]
        press_key = "press"
    except KeyError:
        press_key = "press_qnh"

    print "temp:%s" % data["air_temp"], "humidity:%s" % data["rel_hum"], "pressure:%s" % data[press_key], "rainfall:%s" % data["rain_trace"]
    # Other fields:
    # Apparent Temp.: "apptemp:%s" % data["apparent_t"]
