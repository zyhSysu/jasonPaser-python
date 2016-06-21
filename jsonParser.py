#!/usr/bin/env python

from parser import JsonParser
from fileUtils import FileUtils
from exceptionHandler import jsonParserException

if __name__ == '__main__':

    mParser = JsonParser()

    mFileUtils = FileUtils()

    try:
        jsonStr = mFileUtils.readFromFile('JsonFiles/json2.txt')

        mParser.parseJson(jsonStr)
        mParser.printJsonDict()

        mParser.outputToFile('OutputFiles/output2.txt')

    except jsonParserException as e:
        print e
    except Exception as e:
        print e
