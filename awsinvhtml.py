#!/usr/bin/python
#import sys
import subprocess
import json
#If we use json2html we'll need this
from json2html import *
#from pprint import pprint
#print "Enter a file name:",
#filename = raw_input()
print "Starting JSON Conversion to HTML"
subprocess.call("./awsinv.sh", shell=True)

#Read JSON File
with open('/Users/ryanmaclean/ProcessFun/aws.json') as data_file:    
    data = json.load(data_file)
#pprint(data)

#data = []
#with codecs.open('/Users/string/Desktop/aws.json','rU','utf-8') as f:
#    for line in f:
#       data.append(json.loads(line))

#Create HTMNL File
f = open('aws.html','w')
message = """<html>
<head></head>
<body><p>AWS Details</p>"""+str(data)+"""</body>
</html>"""
f.write(message)
f.close()

#sys.stdout = open(filename, 'w')
print "Completed Conversion, HTML File Saved as aws.html"

#Remove once tested
print "Opening file with Safari to test"
subprocess.call("open -a Safari aws.html", shell=True)
