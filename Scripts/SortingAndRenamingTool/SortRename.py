import os
import time
import re
from PythonToolbox import terminalProgressbar

"""
TODO: 
- import Progressbar from different location
- Kommandozeilen Argumente
- option to remove the date entirely
"""

yes = ["yes", "ye", "y", ""]
no = ["no", "n"]

def renaming(path, subdirectories, dateformat, showchanges) :
	filelist = []

	if subdirectories:
		for root, folders, files in os.walk(path):
			for file in files:
				filelist.append((root, file))

	else :
		for file in os.listdir(path):
			if os.path.isfile(os.path.join(path, file)) :
				filelist.append((path, file))

	nameList = []
	if showchanges: #this is here to create a blank line
		print()

	for root,file in filelist:
		modificationTime = time.strftime(dateformat, time.localtime(os.path.getmtime(os.path.join(root, file))))
		if modificationTime == file[:11]:
			continue
		baseName = file
		if re.match(r"^(\d{4}-\d{2}-\d{2}_.*)$", file):
			baseName = baseName[11:]
		elif re.match(r"^(\d{2}-\d{2}-\d{4}_.*)$", file): 
			baseName = baseName[11:]
		#elif re.match(r"^(\d{2}-\d{4}-\d{2}_.*)$", file): #probably obsolete
			#baseName = baseName[11:]
		if showchanges:
			print(os.path.join(root, file) + "\t=>\t" + os.path.join(root, modificationTime + baseName))
		nameList.append((os.path.join(root, file), os.path.join(root, modificationTime + baseName)))
	
	if len(nameList) == 0:
		print("All files already have already been renamed with their modification dates.")
		return 1

	if showchanges:
		fix = None
		while fix == None:
			answer = input("\nDo you want to accept the changes above? [y]\n>").lower().strip()
			if answer in no: #maybe modify this so only yes and no are possible and other inputs return the question
				print("Aborting... no changes were made.")
				return -1
			elif answer in yes:
				fix = 1
			else:
				print("\nInvalid input.")


	for oldName,newName in terminalProgressbar(nameList, "Renaming: ", 40):
		os.rename(oldName, newName)

	print("Done.")

def userinteraction(path, subdirectories, dateformat, showchanges):
	while path == None:
		answer = input("\nWhere is the base directory located? [Working directory]\n>").lower().strip() #should use working directory if not specified
		if answer == "":
			path = os.path.dirname(__file__) #working directory
		path = answer

	while subdirectories == None:
		answer = input("\nShould subdirectories be included? [y]\n>").lower().strip()
		if answer in yes:
			subdirectories = True
		elif answer in no:
			subdirectories = False
		else:
			print("\nInvalid input.")

	while dateformat == None:
		answer = input("\nWhich format would you like to use? [1]\n1. YYYY-MM-DD (ISO 8601 format)\n2. DD-MM-YYYY (European date format)\n3. MM-DD-YYYY (American date format)\n>").lower().strip()
		if answer == "1" or answer == "":
			dateformat = "%Y-%m-%d_"
		elif answer == "2":
			dateformat = "%d-%m-%Y_"
		elif answer == "3":
			dateformat = "%m-%d-%Y_"
		else:
			print("\nInvalid input.")

	while showchanges == None:
		answer = input("\nDo you want to review the changes before the program executes? [y]\n>").lower().strip() #maybe change american to anglo
		if answer in yes:
			showchanges = True
		elif answer in no:
			showchanges = False
		else:
			print("\nInvalid input.")

	renaming(path, subdirectories, dateformat, showchanges)

userinteraction('/home/brojan/Programming/test', 'n', '%d-%m-%Y_', 'y')