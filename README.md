# Snapshotalyzer-30K
Demo project to manage my AWS EC2 instance snapshots

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance shapshots.

## Configuration

shotty uses the configuration file created by the AWS cli. eg.

'aws configure --profile shotty'

## Running

'pipenv run python shotty.py <command> <subcommand> <--project=Project>
*command* is instance, volumes, or snapshots
*subcommand* - depends on command
*project* is optional
