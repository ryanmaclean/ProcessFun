#!/bin/bash

#Get info about EC2, ELB, RDS, Elasticache and Cloudformation for a particular region
#Output defaults to STDOUT in JSON format

#Set the region for the commands
region="us-east-1"

aws ec2 describe-instances --region $region
aws elb describe-load-balancers --region $region
aws rds describe-db-instances --region $region
aws elasticache describe-cache-clusters --region $region
aws cloudformation describe-stacks --region $region
