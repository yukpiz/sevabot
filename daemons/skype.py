#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Skype4Py
import os

class SkypeConnection:

    def init_skype(self):
        os.environ['DISPLAY'] = ':1'
        skype = Skype4Py.Skype()
        skype.Attach()
        return skype

    def get_room(self, skype):
        rooms = [room for room in skype.Chats]
        for room in rooms:
            if room.Name == '#mecha_pentagon/$e75f7942bb206915':
                return room
        return rooms[0]

