#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import sys
from stat import *
import re
import random
import datetime
from skype import SkypeConnection


uuid_aliases = {
    "yukpiz": ["きぴ"],
    "chihiroe1": ["ちーちゃん", "ちゃんちー"],
    "sashiire": ["みっちゃん", "みちこ"],
    "ruxu_fox": ["ルゥさん"],
    "hagetaka3": ["はーげん", "ちゃんはげ"],
    "dearuma": ["ひなちゃん", "ちゃんひな"],
}

filename = '/var/minecraft/pink-server/logs/latest.log'

def init(filename):
    file = open(filename, 'r')
    st_results = os.stat(filename)
    st_size = st_results[ST_SIZE]
    file.seek(st_size)
    return file

def joined_handler(room, uuid):
    nicknames = uuid_aliases[uuid.lower()]
    room.SendMessage(random.choice(nicknames) + 'がログインしました！')

def left_handler(room, uuid):
    nicknames = uuid_aliases[uuid.lower()]
    room.SendMessage(random.choice(nicknames) + 'がログアウトしました！')

def parse(line):
    pattern = r']:\s(\w*)\sjoined\sthe\sgame'
    match = re.findall(pattern, line)
    if match:
        joined_handler(room, match[0])

    pattern = r']:\s(\w*)\sleft\sthe\sgame'
    match = re.findall(pattern, line)
    if match:
        left_handler(room, match[0])


def tail_f(usec):
    msec = usec / 1000

    while 1:
        os.environ['DISPLAY'] = ':1'
        file = init(filename)
        fpos = file.tell()
        line = file.readline()
        if not line:
            time.sleep(msec)
            file.seek(fpos)
        else:
            print line
            parse(line)

        file.close()
    pass


if __name__ == '__main__':
    skype_connection = SkypeConnection()
    skype = skype_connection.init_skype()
    room = skype_connection.get_room(skype)
    tail_f(500)
