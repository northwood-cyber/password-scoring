#!/bin/sh/python3

# --- IMPORTS ---

import argparse
import sys
import subprocess
import time
from decimal import Decimal
from tqdm import tqdm

#import pass_scoring
#from score_class import Score

import password_score

# --- METHODS ---

def scorePasswords(passfile,outputfile,customlist=None):

	customSet = None

	if customlist:
		customSet = [line.lower().replace('\'','') for line in customlist.read().strip().split()]
	
	#print(customSet)
	passwords = passfile.read().strip().split()
	
	#print(passwords)
	
	#pscore = Score()
	
	for password in tqdm(passwords):
	
		score = 0
	
		#print(password)
		
		#score = pass_scoring.getScore(password,customlist)
		
		score = password_score.getScore(password)
		
		# if using custom wordlist,
		# check if password contains any word from custom list
		# remove percentage of score from password if found
		if customSet:
			for word in customSet:
				#print(word)
				if word in password:
					percentlen = (len(word) / len(password))
					score -= percentlen * score
					score = password_score.checkRange(score)	# <-- check score in range 0 - 100
		
		
		#print("SCORE " + str(score))
		
		TWOPLACES = Decimal(10) ** -2
		decimal_score = Decimal(score).quantize(TWOPLACES)
		
		outputfile.write(password + ',' + str(decimal_score) + '\n')
		
		#print("")
		#print("")
		
	#--
	
	# time taken to complete
	#print("Process Time:")
	#print(time.process_time() - start_time)
	
	# tqdm provides timing
	
	# TESTING
	# Open password score output file
	print('[*] Open output file? (Y/N)')
	answer = input()
	if (answer.upper() == 'Y'):
		command = 'gnome-terminal -- gedit ' + outputfile.name
		subprocess.call(command,shell=True)
	
	
	
# -- End --



# --- MAIN ---

if __name__ == '__main__':

	start_time = time.process_time()
	
	parser = argparse.ArgumentParser(description='Calculate password strength & complexity score.')
	
	parser.add_argument('-p','--passwords',help='Password file for scoring',required=True)
	parser.add_argument('-o','--outputfile',help='Scoring output file',default='password_scores.txt',required=False)
	parser.add_argument('-w','--wordlist',help='Custom wordlist',required=False)
	
	args = parser.parse_args()
	
	# --- Open Files ---
	# open file containing passwords to score
	try:
		passwords = open(args.passwords,'r')
	except Exception as e:
		print('\n[*] Error opening passwords file...')
		print(e)
		sys.exit()
	
	#print(passwords)
	
	# open output file
	# default file = password_scores.txt
	output = open(args.outputfile,'w+')
	
	custom_list = None
	
	if args.wordlist:
		print(args.wordlist)
		#print(type(args.wordlist))
		try:
			custom_list = open(args.wordlist,'r')
			# score passwords using custom list
			#scorePasswords(passwords,output,custom_list)
		except Exception as e:
			print(e)
			print('\n[*] Error opening custom wordlist...')
			#print('[*] Do you wish to continue without the custom wordlist? (Y/N)')
			#answer = input()
			#if not (answer.upper() == 'Y'):
			sys.exit()
	#else:
		#scorePasswords(passwords,output)
	
	
	# --- Call Score Method ---
	
	'''
	try:
		scorePasswords(passwords,output,custom_list)
	except Exception as e:
		scorePasswords(passwords,output)
	'''
	
	if custom_list:
		scorePasswords(passwords,output,custom_list)
	else:
		scorePasswords(passwords,output)
	
	# --- Close Files ---
	
	passwords.close()
	output.close()
	
	if custom_list:
		custom_list.close()
	
	
	
