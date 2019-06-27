#!/bin/bash
aws dynamodb create-table \
             --region=us-east-1 \
             --table-name users \
             --attribute-definitions \
                 AttributeName=id,AttributeType=N \
                 AttributeName=name,AttributeType=S \
                 AttributeName=age,AttributeType=N \
             --key-schema \
                 AttributeName=id,KeyType=HASH \
                 AttributeName=name,KeyType=RANGE \
             --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
             --global-secondary-indexes IndexName=Index,\
KeySchema=["{AttributeName=name,KeyType=HASH}","{AttributeName=age,KeyType=RANGE}"],\
Projection="{ProjectionType=INCLUDE ,NonKeyAttributes=["age"]}",\
ProvisionedThroughput="{ReadCapacityUnits=5,WriteCapacityUnits=5}"