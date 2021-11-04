#!/usr/bin/env python

#this program creates a new file in current directory with encrypted letters - numbers and/or punctuation marks are not affected
#KEY:    ABCDEFGHIJKLMNOPQRSTUVWXYZ
#CIPHER: GHIJKLMNOPQRSTUVWXYZABCDEF
#Capitalization is removed for code brevity; future iterations could easily support capitalization by doubling cipher dictionary length


import sys,os,os.path

#instantiate input file as variable
infile = sys.argv[1]
infile_name = str(infile)

cipher = { 'a' : 'g', 	
	'b' : 'h',
	'c' : 'i',
	'd' : 'j',
	'e' : 'k',
	'f' : 'l',
	'g' : 'm',
	'h' : 'n',
	'i' : 'o',
	'j' : 'p',
	'k' : 'q',
	'l' : 'r',
	'm' : 's',	
	'n' : 't',
	'o' : 'u',
	'p' : 'v', 	
	'q' : 'w',
	'r' : 'x',
	's' : 'y',
	't' : 'z',
	'u' : 'a',
	'v' : 'b',
	'w' : 'c',
	'x' : 'd',
	'y' : 'e',
	'z' : 'f' }

#this block ensures the cipher has no duplicates
list_cipher = cipher.values()
for item in list_cipher:
	if list_cipher.count(item) != 1:
		print "possible problem with", item, " count is: ", cipher_key.count(item)

#instantiate list to hold encrypted characters
list = []

#interate through input file
x = open(infile, 'r+')
for line in x:
	for character in line:
		key = character.lower() #ensure all input is lowercase
		letter = cipher.get(key, character) #get encrypted value
		list.append (letter) #append encrypted letter to holding list

#join all encrypted letters within holding list into one string
finalstring = ''.join(list)

#create string to help rename output file per instructions
newfilename = "encrypted_" + infile_name 

#create new file in current directory with appropriate name
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, newfilename)
exportfile = open(final_directory, "w") #open file so we can write to it

#write string to file
exportfile.write(finalstring)

#close file
exportfile.close()




