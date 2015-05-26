#!/usr/bin/python

#Use subprocess to call Bash script
import subprocess

#Use JSON in order to parse Bash output
import json

#If we use json2html we'll need this
from json2html import *

#In order to make things look nice, we use Pretty Print
#from pprint import pprint

print "Starting JSON Conversion to HTML"
json_temp = subprocess.Popen(['/bin/bash', './awsinv.sh'], stdout=subprocess.PIPE).communicate()[0]
#json_temp = subprocess.Popen(['/bin/sh', 'ls'])
#json.loads(json_temp)
#Read JSON File
#with open('aws.json') as data_file:    
#    data = json.load(data_file)
#pprint(data)

#data = []
#with codecs.open('/Users/string/Desktop/aws.json','rU','utf-8') as f:
#    for line in f:
#       data.append(json.loads(line))

#Create HTML File
f = open('aws.html','w')
message = """<html>
<head></head>
<body><p>AWS Details</p>"""+json2html.convert(json = json_temp)+"""</body>
</html>"""
f.write(message)
f.close()

#sys.stdout = open(filename, 'w')
print "Completed Conversion, HTML File Saved as aws.html"

#Remove once tested
print "Opening file with Safari in order to test results"
subprocess.call("open -a Safari aws.html", shell=True)
