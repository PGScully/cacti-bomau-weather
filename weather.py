#! /usr/bin/env python

import openanything
import sys

from BeautifulSoup import BeautifulSoup

if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except IndexError:
        sys.exit("Usage: weather.py url")

    useragent = "myWeatherFetcher/1.0"   
    htmlsource = openanything.fetch(url, agent=useragent)

    data = BeautifulSoup(htmlsource['data'])
    data = data.findAll(['table'], attrs = {"class" : "tabledata"}, limit = 1)[0]
    data = data.tbody.findAll(['tr'], limit = 1)[0].findAll(['td'])

    print "temp:" + data[1].contents[0], "humidity:" + data[4].contents[0], "pressure:" + data[11].contents[0], "rainfall:" + data[13].contents[0]
