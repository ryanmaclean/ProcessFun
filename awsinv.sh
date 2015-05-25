#!/bin/bash

#Get info about EC2, ELB, RDS, Elasticache and Cloudformation for a particular region.
#Output defaults to variable file name in JSON format which we overwrite on each run.

#Set the region for the commands
region="us-east-1"

#Set the exported file's name
filename="aws.json"

#Initialize the file
: > $filename

#Run the AWS CLI commands and concatenate contents of file
aws ec2 describe-instances --region $region 1>>$filename
#aws elb describe-load-balancers --region $region 1>>$filename
#aws rds describe-db-instances --region $region 1>>$filename
#aws elasticache describe-cache-clusters --region $region 1>>$filename
#aws cloudformation describe-stacks --region $region 1>>$filename
