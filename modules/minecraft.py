#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import commands
from stat import *

progname = 'minecraft'

args = sys.argv[1:]
if len(args) <= 0:
    sys.exit()

command = ' '.join(args)

filename = '/var/minecraft/pink-server/logs/latest.log'
file = open(filename, 'r')
st_results = os.stat(filename)
st_size = st_results[ST_SIZE]
file.seek(st_size)

commands.getoutput('screen -S pink_minecraft -X stuff \'%s\n\'' % command)

time.sleep(3)

file.tell()
print file.read()
