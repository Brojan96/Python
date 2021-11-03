import os
from datetime import datetime

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
