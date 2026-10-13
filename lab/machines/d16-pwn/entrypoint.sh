#!/bin/sh
(cron || service cron start) 2>/dev/null
exec /usr/sbin/sshd -D -e
