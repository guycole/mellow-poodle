#!/bin/bash
#
# Title: rpi-sensor-hat.sh
# Description: read rpi-sensor-hat and post to mellow-skunk
# Development Environment: Ubuntu 22.04.05 LTS
# Author: Guy Cole (guycole at gmail dot com)
#
# * * * * * /home/gsc/Documents/github/mellow-poodle/bin/rpi-sensor-hat.sh > /dev/null 2>&1
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
FILE_NAME="/tmp/sensor.json"
HOME_DIR="/home/gsc/Documents/github"
#
echo "start scan"
unlink $FILE_NAME
cd $HOME_DIR/mellow-poodle/src
python collector.py 
echo "end scan"
#
echo "start skunk post"
cd $HOME_DIR/mellow-poodle/src
#source venv/bin/activate
python ./skunk_post.py
echo "end skunk post"
#
