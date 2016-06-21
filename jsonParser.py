#!/usr/bin/env python

from parser import *
from fileUtils import *
from exceptionHandler import *

if __name__ == '__main__':

    mParser = JsonParser()

    # mFileUtils = FileUtils()

    try:
        mParser.parseJson(
            ' \n  {"name":"zyh", \r \n "ID" : 123, "friend":[1,2,"bie"], "stuff":{"brand":"nike", "Type":"running shoe", "price": 500}}   \r  \r\n')

        mParser.printJsonDict()
    except jsonParserException as e:
        print e
