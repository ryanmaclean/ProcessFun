# ProcessFun

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

####Install the [AWS CLI] (http://aws.amazon.com/cli/)
The easiest way is with Python pip:
<pre>wget https://bootstrap.pypa.io/get-pip.py && sudo python get-pip.py</pre>

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

## Usage
1. Download the raw awsinv.sh and awsinvhtml.py files to the same directory
2. If needed, edit the region in the awsinv.sh file as it is currently set to "us-east-1"
3. Make the awsinv.sh executable: <pre>chmod +x awsinv.sh</pre>
4. Run the process using python: <pre>python aswinvhtml.py</pre>
5. Open the resulting aws.html file in your web browser (or add some logic to rsync/scp the file to a webserver)
