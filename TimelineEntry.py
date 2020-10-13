# This program asks you a series of questions and returns a markdown file.
from datetime import date


class MikeChasesDay:
	def __init__(self):
		self.date = date.today()
		print("Today's date is: " + str(date))
	def printDate(self):
		print("Today's date is: " + str(date))