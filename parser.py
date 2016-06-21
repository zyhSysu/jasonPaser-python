#!/usr/bin/env python

import re
import pprint
import json

from exceptionHandler import *


class JsonParser:
    def __init__(self):
        self.jsonDict = dict()

    def parseJson(self, jsonStr):

        jsonStr = self.deleteSpace(jsonStr)

        if len(jsonStr) == 0:
            raise jsonParserException("Empty Json string")
        elif len(jsonStr) < 2:
            raise jsonParserException("Syntax Error: json string length is less than 2")
        elif jsonStr[0] != '{' or jsonStr[-1] != '}':
            raise jsonParserException("Syntax Error: brace error")
        else:
            self.jsonDict, step = self.parseObject(str(jsonStr)[0: len(jsonStr)])

    def parseObject(self, jsonStr):

        jsonObj = dict()

        # check the braces completion
        twoBraces = False

        # begin to parse the json object
        index = 0

        if jsonStr[index] != '{':
            raise jsonParserException("Syntax Error: brace error")

        index += 1

        while index < len(jsonStr):

            if jsonStr[index] == '}':
                twoBraces = True

                break

            # parse key(string)
            strVlue, step = self.parseString(jsonStr[index: len(jsonStr)])

            key = strVlue

            index += step

            # parse symbol ":"
            if index >= len(jsonStr) or jsonStr[index] != ':':
                raise jsonParserException("Syntax Error: missing \':\' after key")

            # parse value
            index += 1

            if jsonStr[index] == '"':  # value is string
                strValue, step = self.parseString(jsonStr[index: len(jsonStr)])

                jsonObj[key] = strValue

                index += step
            elif jsonStr[index].isdigit() == True:  # value is number
                numValue, step = self.parseNumber(jsonStr[index: len(jsonStr)])

                jsonObj[key] = numValue

                index += step
            elif jsonStr[index] == '[':  # value is array
                arrayValue, step = self.parseArray(jsonStr[index: len(jsonStr)])

                jsonObj[key] = arrayValue

                index += step
            elif jsonStr[index] == '{':  # value is obj
                objValue, step = self.parseObject(jsonStr[index: len(jsonStr)])

                jsonObj[key] = objValue

                index += step
            else:
                raise jsonParserException("Unknown Exception")

            if index < len(jsonStr) and jsonStr[index] == ',':
                index += 1

        if twoBraces == True:
            return jsonObj, index + 1
        else:
            raise jsonParserException("Syntax Error: Missing \'}\'")

    def parseArray(self, jsonStr):

        jsonArray = list()

        # check the braces completion
        twoBraces = False

        # begin to parse json array
        index = 0

        if jsonStr[index] != '[':
            raise jsonParserException("Syntax Error: Missing \'[\'")

        index += 1

        while index < len(jsonStr):
            if jsonStr[index] == ']':
                twoBraces = True

                break

            if jsonStr[index] == '"':  # element is string
                strValue, step = self.parseString(jsonStr[index: len(jsonStr)])

                jsonArray.append(strValue)

                index += step
            elif jsonStr[index].isdigit() == True:  # element is number
                numValue, step = self.parseNumber(jsonStr[index: len(jsonStr)])

                jsonArray.append(numValue)

                index += step
            else:
                raise jsonParserException("Unknown Exception")

            if index < len(jsonStr) and jsonStr[index] == ',':
                index += 1

        if twoBraces == True:
            return jsonArray, index + 1
        else:
            raise jsonParserException("Syntax Error: Missing \']\'")

    def parseString(self, jsonStr):

        # check the quotation marks completion
        twoQuotation = False

        # begin to parse string
        index = 0

        if jsonStr[index] != '"':
            raise jsonParserException("Syntax Error: Missing \'\"\'")

        index += 1

        while index < len(jsonStr):
            if jsonStr[index] == '"':
                twoQuotation = True

                break

            index += 1

        if twoQuotation == True:
            if index > 1:
                return jsonStr[1: index], index + 1
            else:  # empty string element
                return "", index + 1
        else:
            raise jsonParserException("Syntax Error: Missing \'\"\'")

    def parseNumber(self, jsonStr):

        # whether the number is double
        isFloat = False

        # begin to parse number
        index = 0

        while index < len(jsonStr):
            if jsonStr[index].isdigit() == False:
                break
            elif jsonStr[index] == '.':
                if isFloat == False:
                    isFloat = True
                else:
                    raise jsonParserException("Syntax Error: Invalid float number")

            index += 1

        if isFloat == True:
            return float(jsonStr[0: index]), index
        else:
            return int(jsonStr[0: index]), index

    # use regular expression to eliminate all spaces
    def deleteSpace(self, jsonStr):

        space = re.compile(r"[\r\n\s\t]")

        return re.sub(space, '', jsonStr)

    def printJsonDict(self):

        if len(self.jsonDict) == 0:

            raise jsonParserException("Empty Json dictionary")
        else:  # print dictionary

            # cancel sorting module
            pprint._sorted = lambda x: x

            pp = pprint.PrettyPrinter(indent=4)

            jsonFormatStr = json.dumps(self.jsonDict)

            pp.pprint(json.loads(jsonFormatStr))

            return