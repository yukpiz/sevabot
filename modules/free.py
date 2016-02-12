#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands

progname = 'free'

output = commands.getoutput('free -h')
print '--->' + output.replace('    ', '　')
