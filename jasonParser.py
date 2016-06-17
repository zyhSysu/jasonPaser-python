#!/usr/bin/env python

import sys
from parser import *
from fileUtils import *
from exceptionHandler import *

if __name__ == '__main__':

	mParser = JasonParser()

	mFileUtils = FileUtils()

	mStatusHandler = StatusHandler()

	status = mParser.parseJason(' \n  {"name":"zyh"}   \r  \r\n')

	mStatusHandler.displayStatus(status)