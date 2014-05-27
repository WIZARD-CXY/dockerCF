#!/bin/sh

for i in "analyze" "serve_api" "evacuator" "fetch_desired" "listen" "serve_metrics" "send" "shred" 
do 
    if [ $i = "analyze" ] || [ $i = "fetch_desired" ] || [ $i = "send" ] || [ $i = "shred" ]; then /home/go/bin/hm9000 $i --config /home/hm9000.json --poll 1>>$LOG_DIR/hm9000_$i.stdout.log \
	        2>>$LOG_DIR/hm9000_$i.stderr.log &
    else 
       /home/go/bin/hm9000 $i --config /home/hm9000.json 1>>$LOG_DIR/hm9000_$i.stdout.log \
	        2>>$LOG_DIR/hm9000_$i.stderr.log & 
    fi 
 done
 bash
