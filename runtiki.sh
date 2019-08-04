#!/bin/sh
# capture output of script to pass info to applescript
# this is done to send the title of the post
var=$(python3 tikitracker.py); osascript msg_tiki.scpt "$var"
