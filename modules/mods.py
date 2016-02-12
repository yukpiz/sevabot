#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands

progname = 'mods'

mods_path = '/var/minecraft/pink-server/mods'
output = commands.getoutput('ls -w 1 %s' % mods_path)
print output
