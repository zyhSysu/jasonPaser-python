#!/usr/bin/env python

class jsonParserException(Exception):
    def __init__(self, mInfo):
        self.info = mInfo

    def __str__(self):
        return self.info