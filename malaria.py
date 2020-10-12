#!/usr/local/bin/python3
'''
Title: malaria.py
Date: 2020-10-11
Author: Linnea Olsson 

Description: 
    This program will appended protein descriptions from a blast file to the end of the fasta id line in. The program
        puts the output in a file designated by the user. 
    If there is no protein name indicated in the blast file (null), this fasta file will not be included in the output file. 

List of user defined functions (if any):

List of modules used that are not explained in the course material:
    sys - module for using system specific parameters and functions. In this case for getting command line parameters

Procedure:
    1. Create an empty dictionary.
    2. From a blast file, add id numbers as keys and hitDescriptions (protein description) as values into the dictionary. 
    3. Look for matching ids in the fasta file and the dictionary. 
    4. If a proper match (where the description is not null) is found, the hitDescription of that id in the dictionary is appended 
        to the fasta header line and written into an output file along with the corresponding DNA sequence from the fasta file. 

Usage:
    python3 malaria.py malaria.blastx.tab malaria.fna output.txt
'''

protDict = dict() #create empty dictionary
import sys #to be able to insert command line arguments (the files) into the code 

with open(sys.argv[1], 'r') as f: #opens the file to read it and names it 'f' (and don't have to close it, by using with open()). [1] will be blast file
    headers = f.readline() #headers are first line 
    for lines in f: #loops through the rest of the lines in f
        info = lines.split('\t') #split line by tabs and call the resulting list info
        protDict[info[0]] = info[9] # id is on column zero and the protein description is in column 9, save id as key and description as value

with open(sys.argv[2], 'r') as t: #opens and reads command line argument[2] the fasta file
    open(sys.argv[3], 'w').write("") #opens command line argument [3] the output file, and writes nothing "", making sure the with command always starts in an empty output.txt, in case you run it several times. 
    file = open(sys.argv[3], 'a') #opens the output file as "file" and appending information to it. to easily use this in the following loops
    for lines in t: #loops through lines in fasta file
        info = lines.split('\t') #lines are tab delimited, info is list of all objects in fasta file
        if ">" in info[0]: #info is a list, therefor looks for a '>' in the first object of the list
            info[3] = info[3].strip() #strip whitespace from list column in fastafile
            key = info[0][1:].strip() #id without '>' and removes the white space behind the id, and puts in 'key'
            name = protDict[key] #looks for id in dictionary and gets matching hitDescription 
            if name != "null": #if the id is not value 'null' in the dictionary, then:
                info.append(name) #append the hitDescription to info in fasta file
                file.write("\t".join(info) + "\n") #opens output file and joins objects in info with tab as delimiter and adds new line at the end. writes this in output file 
        else: #if line doesn't have a '>': 
            if name != "null": #and if hitDescrption isn't 'null':
                file.write(info[0]) #write object one in info, seq, as next line. since info is list, we define the seq as the first object 