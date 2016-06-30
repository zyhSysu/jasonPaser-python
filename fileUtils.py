#!/usr/bin/env python

import json

class FileUtils:
    def readFromFile(self, filePath):
        """

        :rtype: string
        """
        jsonStrFromFile = ''

        jsonFile = open(filePath, 'r')

        while True:
            lines = jsonFile.readlines(10000)

            if not lines:
                break
            else:
                for line in lines:
                    jsonStrFromFile += line

        return jsonStrFromFile

    def writeToFile(self, filePath, jsonDict):
        with open(filePath, 'w') as outputFile:
            json.dump(jsonDict, outputFile, indent = 4, separators = (',', ': '))


