PORT="443"
LOG="error"
OUTPUT="$(find /home -name JuizServer -type d)/logs/$LOG-$(date +%s)"

DAEMON_OPTS="SiriServer.py -p $PORT"

if [ "$LOG" != "" ]; then
    if [ "$OUTPUT" = "" ]; then
        OUTPUT="$APP_PATH/logs/$(date +%s)-$LOG"
    fi
    DAEMON_OPTS="$DAEMON_OPTS -l $LOG --logfile $OUTPUT"
fi

sudo python $DAEMON_OPTS