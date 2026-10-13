#!/bin/sh
exec socat -T20 TCP-LISTEN:9000,reuseaddr,fork,su=chal EXEC:/chal
