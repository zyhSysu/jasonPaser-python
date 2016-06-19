#!/usr/bin/env python

import sys
import re

PARSER_SUCCESS = 0
PARSER_EMPTYDICT = 1
PARSER_SYNTAXERROR = 2
PARSER_EMPTYJASON = 3


class JasonParser:
	
	def __init__(self):

		self.jasonDict = dict()

	def parseJason(self, jasonStr):

		jasonStr = self.deleteSpace(jasonStr, begin)

		elif len(jasonStr) == 0:

			return PARSER_EMPTYJASON
		elif len(jasonStr) < 2:

			return PARSER_SYNTAXERROR
		elif jasonStr[0] != '{' or jasonStr[-1] != '}':

			return PARSER_SYNTAXERROR
		else:

			self.jasonDict, status = self.parseObject(str(jasonStr)[1: -1])

			return status


	def parseObject(self, jasonStr):
		
		jasonObj = dict()

		#Begin to parse the jason object
		index = 0

		while index < len(jasonStr):
			#parse key(string)
			keyHead, keyTail = self.parseString(jasonStr)

			key = jasonStr[keyHead:keyTail]

			index = keyTail+1

			if index >= len(jasonStr) or jasonStr[index] != ':':

				return None, PARSER_SYNTAXERROR
			else:
				index += 1

				if jasonStr[index] == '"':		#value is string
					strHead, strTail = self.parseString(jasonStr[index, len(jasonStr)])

					jasonObj[key] = jasonStr[strHead:strTail]

					index = strTail
				elif jasonStr[index] == '': #regular expression:	#value is numeric
				
					pass
				elif jasonStr[index] == '[':						#value is array

					pass
				elif jasonStr[index] == '{':						#value is obj

					pass
				else:
					return PARSER_SYNTAXERROR

		return jasonObj, PARSER_SUCCESS

	def parseArray(self, jasonStr):

		pass

	def parseString(self, jasonStr):

		pass

	def deleteSpace(self, jasonStr):

		space = re.compile(r"[\r\n\s\t]")

		return re.sub(space, '', jasonStr)

	def printJasonDict(self):

		if len(self.jasonDict) == 0:

			return PARSER_EMPTYDICT
		else:

			pass



