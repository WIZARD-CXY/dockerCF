#!/bin/sh

/dea_ng/bin/dea $JOB_DIR/config/dea.yml >>$LOG_DIR/dea.stdout.log 2>>$LOG_DIR/dea.stderr.log &


cd /warden  && bundle exec \
         rake warden:start[$WARDEN_CONF_DIR/warden.yml] \
         1>>$LOG_DIR/warden.stdout.log \
         2>>$LOG_DIR/warden.stderr.log & 
         
/dea_ng/go/bin/runner \
         -conf $JOB_DIR/config/dea.yml \
         >>$LOG_DIR/dir_server.stdout.log \
         2>>$LOG_DIR/dir_server.stderr.log