#!/usr/bin/env python

import sys

PARSER_SUCCESS = 0
PARSER_EMPTYDICT = 1
PARSER_SYNTAXERROR = 2
PARSER_EMPTYJASON = 3


class JasonParser:
	
	def __init__(self):

		self.jasonDict = dict()

	def parseJason(self, jasonStr):

		jasonStr = self.deleteSpace(jasonStr)

		if len(jasonStr) == 0:

			return PARSER_EMPTYJASON
		elif len(jasonStr) < 2:

			return PARSER_SYNTAXERROR
		elif jasonStr[0] != '{' or jasonStr[-1] != '}':

			return PARSER_SYNTAXERROR
		else:

			self.jasonDict = self.parseObject(str(jasonStr)[1: -1])

			return PARSER_SUCCESS


	def parseObject(self, jasonStr):
		
		jasonObj = dict()

		jasonStr = self.deleteSpace(jasonStr)

		#Begin to parse the jason

		return jasonObj

	def parseArray(self, jasonStr):

		pass

	def deleteSpace(self, jasonStr):

		if len(jasonStr) > 0:
			head, tail = 0, len(jasonStr)-1

			#eliminate space in the head
			while head <= tail:
				if jasonStr[head] == ' ' or jasonStr[head] == '\r' \
					or jasonStr[head] == '\n':

					head += 1
				else:
					break

			#eliminate space in the tail
			while tail >= head:
				if jasonStr[tail] == ' ' or jasonStr[tail] == '\r' \
					or jasonStr[tail] == '\n':

					tail -= 1
				else:
					break


			return jasonStr[head: tail+1]

		else:
			return jasonStr

	def printJasonDict(self):

		if len(self.jasonDict) == 0:

			return PARSER_EMPTYDICT
		else:

			pass



