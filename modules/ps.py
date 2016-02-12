#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands

progname = 'ps'

output = commands.getoutput('ps aux | grep minecraft')
print output
