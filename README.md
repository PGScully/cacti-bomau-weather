Cacti BOM-AU Weather
====================

This script will pull the current data for a single weather station from
www.bom.gov.au.  It takes as it's only arguement the full URL to the JSON data
for that station.  Make sure to use the "JavaScript Object Notation format
(JSON) in row-major order" URL provided at the bottom of a station's page.

e.g.
python weather.py http://www.bom.gov.au/fwo/IDN60801/IDN60801.94768.json
temp:23.0 humidity:75 pressure:1021.8 rainfall:0.0

Note
----

Please be nice to the BOM servers, and set 'Step' to 1800 when creating your
data templates.  BOM website data is typically updated every 30 minutes, so it's
pointless to update more often.

