import os
import time
import re
#import curses
#from datetime import datetime

"""
TODO: 
- manage user interactions
	- Abfrage Pfad
	- Abfrage subdirectories
	- Abfrage Datumsformat 
	- Show changes 
	- Sicherheitsfrage
- Progress Bar
- Kommandozeilen Argumente
"""
yes = ["yes", "ye", "y", "", " "]

def renaming(path, subdirectories, dateformat, showchanges) :
	#if renaming == renaming(None, None, None, None): #this is stupid
	#	userinteraction(path, subdirectories, dateformat, showchanges)

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
	if showchanges:
		print()

	for root,file in filelist:
		modificationTime = time.strftime(dateformat, time.localtime(os.path.getmtime(os.path.join(root, file))))
		if modificationTime == file[:11]:
			continue
		baseName = file
		if re.match(r"^(\d{4}-\d{2}-\d{2}_.*)$", file):
			baseName = baseName[11:]
		if showchanges:
			print(os.path.join(root, file) + "\t=>\t" + os.path.join(root, modificationTime + baseName))
		nameList.append((os.path.join(root, file), os.path.join(root, modificationTime + baseName)))
	
	if len(nameList) == 0:
		print("All files already have already been renamed with their modification dates.")
		return 1

	if showchanges:
		if not input("\nDo you want to accept the changes above? [y]\n>").lower().strip() in yes:
			print("Aborting... no changes were made.")
			return -1
	
	for oldName,newName in nameList:
		os.rename(oldName, newName)
	print("Done.")
			
renaming("/home/brojan/Documents/Test", True, '%Y-%m-%d_', True)

def userinteraction(path, subdirectories, dateformat, showchanges):
	path = input("Where is the base directory located? [y]\n>").lower().strip()
	if os.name == "dos":
		path = path.replace("\\", "\\\\")
	if input("Should subdirectories be included? [y]\n>").lower().strip() in yes:
		subdirectories = True
	else:
		subdirectories = False

	dateformat = input("Which format would you like to use?\n1. YYYY-MM-DD \n2.DD-MM-YYYY\n3.YYYY-DD-MM [1]\n>").lower().strip()
	if dateformat == 1:
		dateformat = "%Y-%m-%d"
	elif dateformat == 2:
		dateformat = "%d-%m-%Y"
	else:
		dateformat = "%Y-%d-%m"

	if input("Do you want to review the changes before the program executes? [y]\n>").lower().strip() in yes:
		showchanges = True
	else:
		showchanges = False

"""
 	- Abfrage Pfad
	- Abfrage subdirectories
	- Abfrage Datumsformat 
	- Show changes 
	- Sicherheitsfrage
"""
"""
os.path.isfile

os.path.join(root,file)
os.rename()

def options() :
	location = input ('Please name the directory in which the files, which should be renamed, are located: \n>')
	def subdirectories_answer() : 
		global subdirectories
		subdirectories = input('Should the script also include the subdirectories? Please answer "yes" or "no". [y]\n>').lower().strip()
		if(subdirectories == "yes" or subdirectories == 'y' or subdirectories == ''):
			subdirectories = 'yes'
		elif(subdirectories == "no" or subdirectories == 'n'):
			subdirectories = 'no'
		else:
			return subdirectories_answer()
	subdirectories_answer()     
	if subdirectories == 'no' :
		filelist = []
		for file in os.listdir(location) :
			if os.path.isfile(os.path.join(location, file)):
				filelist.append(file)
		print(filelist)
	elif subdirectories == 'yes' :
		filelist = []
		pathlist = []
		for root, dirs, files in os.walk(location):
			print(root)
			for file in files:
				filelist.append(file)
				pathlist.append(os.path.join(root,file))
	def itemcount():
		itemamount = input(str(len(filelist)) + ' Items will be renamed. Want to see the list of files? [n]\n>').lower().strip()
		if itemamount == 'yes' or itemamount == 'y':
			print(filelist)
			print(pathlist)
		elif itemamount == 'no' or itemamount == '':
			print()
		else :
			return itemcount()
	itemcount()
	def final_question() :
		final = input('The files will now be renamed. Continue? Please answer "yes" or "no". [y]\n>')
		if final == 'yes' or final == 'y' or final == '':
			print('success')
		elif final == 'no' or final == 'n' : 
			quit
			print('The script was ended.')
		else :
			return final_question()
	final_question()
	if subdirectories == 'yes' :
		for path in pathlist :
			os.rename(path, str(datetime.fromtimestamp(os.stat(path).st_ctime))[0:10]+' '+path)
	elif subdirectories == 'no' :
		for path in pathlist :
			os.rename(path, str(datetime.fromtimestamp(os.stat(path).st_ctime))[0:10]+' '+path)
options()
"""