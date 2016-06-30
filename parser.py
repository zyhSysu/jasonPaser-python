#!/usr/bin/env python

import re
import json

from collections import OrderedDict
from exceptionHandler import jsonParserException
from fileUtils import FileUtils

class JsonParser:
    def __init__(self):
        self.jsonDict = OrderedDict()

    def parseJson(self, jsonStr):

        jsonStr = self.deleteSpace(jsonStr)

        if len(jsonStr) == 0:
            raise jsonParserException("parseJson -- Empty Json string")
        elif len(jsonStr) < 2:
            raise jsonParserException("parseJson -- Syntax Error: json string length is less than 2")
        elif jsonStr[0] != '{' or jsonStr[-1] != '}':
            raise jsonParserException("parseJson -- Syntax Error: brace error")
        else:
            self.jsonDict, step = self.parseObject(str(jsonStr)[0: len(jsonStr)])

        return

    def parseObject(self, jsonStr):

        jsonObj = OrderedDict()

        # check the braces completion
        twoBraces = False

        # begin to parse the json object
        index = 0

        if jsonStr[index] != '{':
            raise jsonParserException("parseObject -- Syntax Error: brace error")

        index += 1

        while index < len(jsonStr):

            if jsonStr[index] == '}':
                twoBraces = True

                break

            # parse key(string)
            strValue, step = self.parseString(jsonStr[index: len(jsonStr)])

            key = strValue

            index += step

            # parse symbol ":"
            if index >= len(jsonStr) or jsonStr[index] != ':':
                raise jsonParserException("parseObject -- Syntax Error: missing \':\' after key: " + key)

            # parse value
            index += 1

            if jsonStr[index] == '"' or jsonStr[index] == '\'':  # value is string
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
                raise jsonParserException("parseObject -- Syntax Error: syntax error occurs in parseObject key: " + key)

            if index < len(jsonStr) and jsonStr[index] == ',':
                index += 1

        if twoBraces == True:
            return jsonObj, index + 1
        else:
            raise jsonParserException("parseObject -- Syntax Error: Missing \'}\'")

    def parseArray(self, jsonStr):

        jsonArray = list()

        # check the braces completion
        twoBraces = False

        # begin to parse json array
        index = 0

        if jsonStr[index] != '[':
            raise jsonParserException("parseArray -- Syntax Error: Missing \'[\'")

        index += 1

        while index < len(jsonStr):
            if jsonStr[index] == ']':
                twoBraces = True

                break

            if jsonStr[index] == '"' or jsonStr[index] == '\'':  # element is string
                strValue, step = self.parseString(jsonStr[index: len(jsonStr)])

                jsonArray.append(strValue)

                index += step
            elif jsonStr[index].isdigit() == True:  # element is number
                numValue, step = self.parseNumber(jsonStr[index: len(jsonStr)])

                jsonArray.append(numValue)

                index += step
            else:
                raise jsonParserException("parseArray -- Syntax Error: Json Array can only contain number and string")

            if index < len(jsonStr) and jsonStr[index] == ',':
                index += 1

        if twoBraces == True:
            return jsonArray, index + 1
        else:
            raise jsonParserException("parseArray -- Syntax Error: Missing \']\'")

    def parseString(self, jsonStr):

        # check the quotation marks completion
        twoQuotation = False

        # begin to parse string
        index = 0

        if jsonStr[index] != '"' and jsonStr[index] != '\'':
            raise jsonParserException("parseString -- Syntax Error: Missing \'\"\'")

        index += 1

        while index < len(jsonStr):
            if jsonStr[index] == '"' or jsonStr[index] == '\'':
                twoQuotation = True

                break

            index += 1

        if twoQuotation == True:
            if index > 1:
                return jsonStr[1: index], index + 1
            else:  # empty string element
                return "", index + 1
        else:
            raise jsonParserException("parseString -- Syntax Error: Missing \'\"\'")

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
                    raise jsonParserException("parseNumber -- Syntax Error: Invalid float number")

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

            raise jsonParserException("printJsonDict -- Empty Json dictionary")
        else:  # print dictionary

            jsonFormatStr = json.dumps(self.jsonDict, indent = 4, separators = (',', ': '))

            print jsonFormatStr

            return

    def outputToFile(self, outputPath):
        fileUtils = FileUtils()

        fileUtils.writeToFile(outputPath, self.jsonDict)