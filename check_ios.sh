#!/bin/bash
# Before running this script it is necessary to create a subfolder with running config files
# Task: this script to use output from  "show version"
exec > check_ios.rep

echo $(date +"%F")
echo
echo "STARTING IOSCHECK"
REQUIRED_IOS='16.9.101'
VERSION_SEARCH_TEXT='version'

for f in ios_configs/* 
do 
  cat $f | grep hostname  
  IOS_VERSION=$(cat $f | grep $VERSION_SEARCH_TEXT | cut -d' ' -f2)
  echo "Current IOS Version: " $IOS_VERSION
  if [ $IOS_VERSION != $REQUIRED_IOS ] 
  then
    echo "This device needs an upgrade, please upgrade to: " $REQUIRED_IOS
  else 
    echo "No Upgrade needed"
  fi

  echo 
done
echo "ENDING IOS CHECK"