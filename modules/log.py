#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import commands

progname = 'log'

args = sys.argv[1:]
if len(args) != 1:
    print '♡Usage: !log [int]'
    sys.exit()

line = args[0]
log_path = '/var/minecraft/pink-server/logs/latest.log'
command = 'tail -n %d %s' % (int(line), log_path)
output = commands.getoutput(command)
print output
