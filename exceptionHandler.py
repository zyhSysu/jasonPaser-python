#!/usr/bin/env python

import sys

PARSER_SUCCESS = 0
PARSER_EMPTYDICT = 1
PARSER_SYNTAXERROR = 2
PARSER_EMPTYJASON = 3

class StatusHandler:

	def status_success(self):

		print "JasonPaser Success"


	def status_emptyDict(self):

		print "JasonPaser Exception: EmptyDict Exception"


	def status_syntaxError(self):

		print "JasonPaser Exception: SyntaxError Exception"


	def displayStatus(self, code):

		statusCase = {
		0: self.status_success,
		1: self.status_emptyDict,
		2: self.status_syntaxError
		}

		statusCase[code]()