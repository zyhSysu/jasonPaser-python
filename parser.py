#!/usr/bin/env python

import sys
import re

PARSER_SUCCESS = 0
PARSER_EMPTYDICT = 1
PARSER_SYNTAXERROR = 2
PARSER_EMPTYJASON = 3
PARSER_NUMERICERROR = 4


class JasonParser:
	
	def __init__(self):

		self.jasonDict = dict()

	def parseJason(self, jasonStr):

		jasonStr = self.deleteSpace(jasonStr, begin)

		if len(jasonStr) == 0:
			return PARSER_EMPTYJASON
		elif len(jasonStr) < 2:
			return PARSER_SYNTAXERROR
		elif jasonStr[0] != '{' or jasonStr[-1] != '}':
			return PARSER_SYNTAXERROR
		else:
			self.jasonDict, step, status = self.parseObject(str(jasonStr)[0: len(jasonStr)])

			return status


	def parseObject(self, jasonStr):
		
		jasonObj = dict()

		#check the braces completion
		twoBraces = False

		#begin to parse the jason object
		index = 0

		if jasonStr[index] != '{':
			return None, -1, PARSER_SYNTAXERROR

		index += 1

		while index < len(jasonStr):

			if jasonStr[index] == '}':
				twoBraces = True

				break

			#parse key(string)
			strVlue, step, status = self.parseString(jasonStr[index: len(jasonStr)])

			if status != PARSER_SUCCESS:
				return None, -1, PARSER_SYNTAXERROR

			key = strVlue

			index += step

			#parse symbol ":"
			if index >= len(jasonStr) or jasonStr[index] != ':':
				return None, PARSER_SYNTAXERROR

			#parse value
			index += 1

			if jasonStr[index] == '"':							#value is string
				strValue, step, status = self.parseString(jasonStr[index: len(jasonStr)])

				if status != PARSER_SUCCESS:
					return None, -1, PARSER_SYNTAXERROR

				jasonObj[key] = strValue

				index += step
			elif jasonStr[index].isdigit() == True:				#value is number
				numValue, step, status = self.parseNumber(jasonStr[index: len(jasonStr)])

				if status != PARSER_SUCCESS:
					return None, -1, PARSER_SYNTAXERROR

				jasonObj[key] = numValue

				index += step
			elif jasonStr[index] == '[':						#value is array
				arrayValue, step, status = self.parseArray(jasonStr[index: len(jasonStr)])

				if status != PARSER_SUCCESS:
					return None, -1, PARSER_SYNTAXERROR

				jasonObj[key] = arrayValue

				index += step
			elif jasonStr[index] == '{':						#value is obj
				objValue, step, status = self.parseObject(jasonStr[index: len(jasonStr)])

				if status != PARSER_SUCCESS:
					return None, -1, PARSER_SYNTAXERROR

				jasonObj[key] = objValue

				index += step
			else:
				return None, -1, PARSER_SYNTAXERROR

			if index < len(jasonStr) and jasonStr[index] == ',':
				index += 1

		if twoBraces == True:
			return jasonObj, index+1, PARSER_SUCCESS
		else:
			return None, -1, PARSER_SYNTAXERROR

	def parseArray(self, jasonStr):

		jasonArray = list()

		#check the braces completion
		twoBraces = False

		#begin to parse jason array
		index = 0

		if jasonStr[index] != '[':
			return None, -1, PARSER_SYNTAXERROR

		index += 1

		while index < len(jasonStr):
			if jasonStr[index] == ']':
				twoBraces = True

				break

			if jasonStr[index] == '"':						#element is string
				strValue, step, status = self.parseString(jasonStr[index: len(jasonStr)])

				if status != PARSER_SUCCESS:
					return None, -1, PARSER_SYNTAXERROR

				jasonArray.append(strValue)

				index += step
			elif jasonStr[index].isdigit() == True:			#element is number
				numValue, step, status = self.parseNumber(jasonStr[index: len(jasonStr)])

				if status != PARSER_SUCCESS:
					return None, -1, PARSER_SYNTAXERROR

				jasonArray.append(numValue)

				index += step
			else:
				return None, -1, PARSER_SYNTAXERROR

		if twoBraces == True:
			return jasonArray, index+1, PARSER_SUCCESS
		else:
			return None, -1, PARSER_SYNTAXERROR


	def parseString(self, jasonStr):

		#check the quotation marks completion
		twoQuotation = False

		#begin to parse string
		index = 0

		if jasonStr[index] != '"':
			return None, -1, PARSER_SYNTAXERROR

		index += 1

		while index < len(jasonStr):
			if jasonStr[index] == '"':
				twoQuotation = True

				break
			
			index += 1


		if twoQuotation == True:
			if index > 1:
				return jasonStr[1: index], index+1, PARSER_SUCCESS
			else:												#empty string element
				return "", index+1, PARSER_SUCCESS
		else:
			return None, -1, PARSER_SYNTAXERROR

	def parseNumber(self, jasonStr):

		#whether the number is double
		isFloat = False

		#begin to parse number
		index = 0

		while index < len(jasonStr):
			if jasonStr[index].isdigit() == False:
				break
			elif jasonStr[index] == '.':
				if isFloat == False:
					isFloat = True
				else:
					return None, -1, PARSER_NUMERICERROR

			index += 1

		if isFloat == True:
			return float(jasonStr[0: index]), index, PARSER_SUCCESS
		else:
			return int(jasonStr[0: index]), index, PARSER_SUCCESS

	#use regular expression to eliminate all spaces
	def deleteSpace(self, jasonStr):

		space = re.compile(r"[\r\n\s\t]")

		return re.sub(space, '', jasonStr)

	def printJasonDict(self):

		if len(self.jasonDict) == 0:

			return PARSER_EMPTYDICT
		else:									#print dictionary

			pass



