PORT="443"
#APP_PATH="$(find /Users -name SiriServerCore -type d)"
APP_PATH="../"
LOG="error"
#OUTPUT="$(find /Users -name SiriDebug -type d)/$LOG-$(date +%s)"
OUTPUT="../../SiriDebug/$LOG-$(date +%s)"

DAEMON_OPTS="SiriServer.py -p $PORT"

cd $APP_PATH

if [ "$LOG" != "" ]; then
    if [ "$OUTPUT" = "" ]; then
        OUTPUT="$APP_PATH/logs/$(date +%s)-$LOG"
    fi
    DAEMON_OPTS="$DAEMON_OPTS -l $LOG --logfile $OUTPUT"
fi

sudo python $DAEMON_OPTS