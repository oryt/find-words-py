#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright 2016 Oscar Ydrefelt
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

# A script that takes file name and a search word as argument and then the script will locate the
# word and then print out the line where the word is found together with line number and location 
# of the word on the line

# import sys that lets us use sys.argv to pass command line entries to the script
import sys
#Takes the three arguments that was passed together with the script and sets them to variables
var1, var2, var3  = sys.argv

def searchFind (fileName, wordToSearch):

# uses try to checks file and Prints error message if the file is not found
	try:
# uses the enumerate function to pair each line with a line number
# runs over the data and looks for search word and if found stores the line, position and word in variables
# pushes the variables to string and then prints it.   

		lineCount =  open(fileName)
		for num, line in enumerate(lineCount, 1):			
			if wordToSearch in line:			
				fullLine = line
				wordstr = str(line)
				wordpos =  wordstr.find(wordToSearch)
				linePos = num, wordpos, fullLine
				DD = str(linePos)
				print DD				
	except IOError:
		print 'Sorry, the file ' + fileName + 'does not exist.'

searchFind(var2, var3)
