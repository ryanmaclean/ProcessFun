#!/usr/bin/python

#Use subprocess to call Bash script
import subprocess

#Use JSON in order to parse Bash output
import json

#If we use json2html we'll need this
from json2html import *

print "Starting JSON Conversion to HTML"

subprocess.Popen(['/bin/bash', './awsinv.sh'], stdout=subprocess.PIPE).communicate()[0]
with open('aws.json') as data_file:    
    data = json.load(data_file)

#Create HTML File and Inject Converted JSON Data using JSON2HTML
f = open('aws.html','w')
message = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>AWS Details</title>

    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <h1>AWS Details</h1><div class="table-striped"><ul class="list-group">"""+json2html.convert(json = data, table_attributes="class=\".table-striped\"")+"""</ul></div>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>"""
f.write(message)
f.close()

#sys.stdout = open(filename, 'w')
print "Completed Conversion, HTML File Saved as aws.html"

#Used for testing
#print "Opening file with Safari in order to test results"
#subprocess.call("open -a Safari aws.html", shell=True)
