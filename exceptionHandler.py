#!/usr/bin/env python

import sys

PARSER_SUCCESS = 0
PARSER_EMPTYDICT = 1
PARSER_SYNTAXERROR = 2
PARSER_EMPTYJASON = 3
PARSER_NUMERICERROR = 4

class StatusHandler:

	def status_success(self):

		print "JasonParser Success"


	def status_emptyDict(self):

		print "JasonParser Exception: EmptyDict Exception"


	def status_syntaxError(self):

		print "JasonParser Exception: SyntaxError Exception"

	def status_emptyJason(self):

		print "JasonParser Exception: EmptyJason Exception"

	def status_numericError(self):

		print "JasonParser Exception: InvalidNumber Exception"

	def displayStatus(self, code):

		statusCase = {
		0: self.status_success,
		1: self.status_emptyDict,
		2: self.status_syntaxError
		3: self.status_emptyJason
		4: self.status_numericError
		}

		statusCase[code]()