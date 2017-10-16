#==================================================#
#SNAPSHOTHELPER.PY	                               #
#DIRECTORY/FILE SYSTEM SNAPSHOT PROGRAM		       #
#BY TENDAI PRINCE DZONGA                           #
#==================================================#

import os, pickle, difflib, sys, pprint


def createSnapshot(directory, filename):
	cumulative_directories = []
	cumulative_files = []

	for root, dirs, files in os.walk(directory):
		cumulative_directories = cumulative_directories + dirs
		cumulative_files = cumulative_files + files

	try:
		output = open(filename, 'wb')
		pickle.dump(cumulative_directories, output, -1)
		pickle.dump(cumulative_files, output, -1)
		output.close()
	except:
		print "Problems encountered trying to save snapshot file!"

	raw_input("Press [Enter] to continue...")
	return

def listSnapshots(extension):
	snaplist = []
	filelist = os.listdir(os.curdir)
	for item in filelist:
		if item.endswith(extension) != -1:
			snaplist.append(item)
	print '''
	Snapshot list:
	========================
	'''
	printList(snaplist)

	raw_input("Press [Enter] to continue...")

def compareSnapshots(snapfile1, snapfile2):

	try:
		pk1_file = open(snapfile1, 'rb')
		dirs1 = pickle.load(pk1_file)
		files1 = pickle.load(pk1_file)
		pk1_file.close()

		pk2_file = open(snapfile2, 'rb')
		dirs2 = pickle.load(pk2_file)
		files2 = pickle.load(pk2_file)
		pk2_file.close()
	except:
		print "Problems encountered accessing snapshot files!"
		raw_input("\n\nPress [Enter] to continue...")
		return 

	result_dirs = list(difflib.unified_diff(dirs1, dirs2))
	result_files = list(difflib.unified_diff(files1, files2))

	added_dirs = []
	removed_dirs = []
	added_files = []
	removed_files = []

	for result in result_files:
		if result.endswith("\n") == -1:
			if result.startswith("+"):
				resultadd = result.strip('+')
				added_files.append(resultadd)
			elif result.startswith("_"):
				resultsubtract = result.strip('-')
				removed_files.append(resultsubtract)

	for result in result_dirs:
		if result.endswith("\n") == -1:
			if result.startswith("+"):
				resultadd = result.strip('+')
				added_dirs.append(resultadd)
			elif result.startswith("-"):
				resultsubtract = result.strip('-')
				removed_dirs.append(resultsubtract)

	print "\n\nAdded Directories:\n"
	printList(added_dirs)
	print "\n\nAdded Files:\n"
	printList(added_files)
	print "\n\nRemoved Directories:\n"
	printList(removed_dirs)
	print "\n\nRemoved Files:\n"
	printList(removed_files)
	raw_input("\n\nPress [Enter] to continue...")


def showHelp():
	os.system('clear')
	print '''
	DIRECTORY/ FILE SNAPSHOT TOOL
	========================================
	Welcome to the directory/file snapshot tool. This tool
	allows you to create snapshots of a directory/file tree,
	list the snapshots you have created in the current directory,
	and compare two snapshots, listing any directories and files
	added or deleted between the first snapshot and the second.

	To run the program follow the following procedure:
	1.	Create a snapshot
	2.	List snapshot files
	3.	Compare snapshots
	4.	Help (this screen)
	5. 	Exit

	'''
	raw_input("Press [Enter] to continue...")

def invalidChoice():
	sys.stderr.write("INVALID CHOICE, TRY AGAIN")
	raw_input("\n\nPress [Enter] to continue...")
	return 

def printList(list):
	full_list = ""
	index_num = 1

	if len(list) > 20:
		for item in list:
			print "\t\t" + item
			if (index_num)%3 == 0:
				print "\n"
			index_num  = index_num + 1
	else:
		for item in list:
			print "\t" + item



