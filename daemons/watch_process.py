#!/usr/bin/env python
# -*- coding: utf-8 -*-

from skype import SkypeConnection
import commands

def watch_process(room):
    command = 'ps aux | grep minecraft | grep -v grep'
    output = commands.getoutput(command)
    runned = True if output else False

    while 1:
        output = commands.getoutput('ps aux | grep minecraft | grep -v grep')
        tmp = True if output else False
        if tmp == runned: continue
        runned = tmp
        if runned:
            print 'Startup of Pink Server.'
            room.SendMessage('ぴんくくらふとサーバーが起動します。')
        else:
            print 'Stopping of Pink Server.'
            room.SendMessage('ぴんくくらふとサーバーが停止します。')

if __name__ == '__main__':
    skype_connection = SkypeConnection()
    skype = skype_connection.init_skype()
    room = skype_connection.get_room(skype)
    watch_process(room)
