# ProcessFun

A collection of examples demonstrating ability with current systems, Git, Bash, Python and AWS. 

File list:

|File Name    | Purpose                                |
|-------------|----------------------------------------|
|awsinv.sh    |AWS Inventory Bash script               |
|awsinvhtml.py|Python conversion to HTML for awsinv.sh |
|httpdcount.sh|Count number of running Apache processes|
|README.md    |This file - an overview of the contents |

## HTTPd Count Shell Script (httpdcount.sh)

*NB: This command should be run via sudo (or as root), otherwise the service restart command could fail.* 

Counts either httpd or apache2 (uncomment the service required) processes and:
 - Prints messages to screen at counts of 1~10, 20~99 and 100+
 - Will restart the service based on the variable if over 100

### Running the Script
 - In order to run the script, download the raw code and pipe it to Bash:
```
curl -L https://raw.githubusercontent.com/ryanmaclean/ProcessFun/master/httpdcount.sh | sudo bash 
```

### Resources
If you'd like to make a similar script, or to fork and modify this for your own needs, here are the resources I used:
 - [Check Reply In Range of Numbers] (http://unix.stackexchange.com/questions/118856/check-if-reply-is-in-a-range-of-numbers)
 - [ps Man Page] (http://linux.about.com/od/commands/l/blcmdl1_ps.htm)
 - [grep Man Page] (http://linux.about.com/od/commands/l/blcmdl1_grep.htm)
 - [TLDP on Bash Operators] (http://www.tldp.org/LDP/abs/html/comparison-ops.html)
 - [Large portion of code - Check Process Running] (http://stackoverflow.com/questions/9117507/linux-unix-command-to-determine-if-process-is-running?newreg=f94bc028011b476eae7b6b89bd237934)
 


## AWS Inventory (awsinv.sh and awsinvhtml.py)
A simple script to check the inventory of the following in the "us-east-1" region:
 - EC2 
 - RDS 
 - ELB 
 - Elastic Cache 
 - Cloudformation

The results are output to a JSON file, then parsed by a script to create an HTML page.

### Requirements
This script is built using the Amazon AWS CLI and uses Python to output to the HTML file. You will need to have the command line tools installed and configured prior to running the script.

Further, you will also need to have JSON2HTML and the "json" command line application installed in order to have better processing of the JSON files (otherwise, you'd be looking at a Python dict dump). 

####Install the [AWS CLI] (http://aws.amazon.com/cli/)
The easiest way is with Python pip:
<pre>curl -O https://bootstrap.pypa.io/get-pip.py && sudo python get-pip.py</pre>

Once pip is installed, you can grab the AWS CLI and install it easily: 
<pre>sudo pip install awscli</pre>

#### Configure AWS CLI
Run the configuration steps:
<pre>aws configure</pre>

You will be asked to input your Access Key (Type it in, then press enter):
<pre>AWS Access Key ID [None]:</pre>

And your secret key:
<pre>AWS Secret Access Key [None]:</pre>

The follwowing can be left blank as we will define output and region on each run:
```
Default region name [None]:
Default output format [None]:
```

###Install JSON2HTML
Installing JSON2HTML is a snap on a system with Python already setup:
<pre>sudo pip install json2html</pre>

####Install JSON Command Line Tool
We'll use this to concatenate the various JSON files retrieved from Amazon. The install is straightforward: I've forked the repository in order to make sure we have a working version, but here's a link to [the source repository] (https://github.com/trentm/json)

Quick and easy install:
```
curl -L https://github.com/trentm/json/raw/master/lib/json.js > json
chmod 755 json
```

###Usage
1. Download the raw awsinv.sh and awsinvhtml.py files to the same directory
2. If needed, edit the region in the awsinv.sh file as it is currently set to "us-east-1"
3. Make the awsinv.sh executable: <pre>chmod +x awsinv.sh</pre>
4. Run the process using python: <pre>python aswinvhtml.py</pre>
5. Open the resulting aws.html file in your web browser (or add some logic to rsync/scp the file to a webserver)

###Resources
 - [Python Subprocess (Popen and running bash from Python)] (https://docs.python.org/2/library/subprocess.html)

##Bonus

###Running the Script With a Rotating Log
We'll take the HTTPdcount.sh script and pipe it's output to a logfile that rotates. In this case, we're assuming logrotate is installed, but just in case, here's the install procedure:
- Debian/Ubuntu:
<pre>sudo apt-get install logrotate</pre>
- RedHat/CentOS/Amazon Linux:
<pre>yum install logrotate</pre>
- MacOS:
<pre>brew install logrotate</pre>

####The One-Liner
We'll want to capture both the output as well as the errors, so we'll use "2>&1" as a parameter, and pipe the result to logrotate using the 86400 (60*60*24) option (every day):
<pre>./httpdcount.sh 2>&1 | logrotate -l httpdcount.%F 86400</pre>

###Streaming the Log with Logstash
We'll send our logs from our server to a centralized location (we're using [ElasticSearch Logstash Kibana] (https://github.com/electronic-arts/opsworks-logstash-ea) for this example). In order to accomplish this on each node, we'll need to set up Logstash and a config file taylored to our script. 

####Logstash Install
The Logstash install is quite straightforward. There's a [Logstash Chef recipe](https://github.com/lusis/chef-logstash), but to keep things simple:

1. Download [Logstash] (https://www.elastic.co/downloads/logstash) 
<pre>curl -O https://download.elasticsearch.org/logstash/logstash/logstash-1.5.0.tar.gz</pre>
2. Extract the file
<pre>tar -zxvf logstash-1.5.0.tar.gz</pre>
3. Run Logstash
```
cd logstash-1.5.0
bin/logstash -e 'input { stdin { } } output { stdout {} }'
```

#WIP - TO BE CONTINUED!