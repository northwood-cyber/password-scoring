#!/bin/sh/python3

import string
import re
import math
#from decimal import Decimal




top = open('top1000pass.txt','r').read().strip().split()

# wordlist for linux system - built in
wordlist = [line.lower().replace('\'','') for line in open('/usr/share/dict/american-english').read().strip().split()]



def getBaseScore(testpass):
		
	basescore = 0
	
	# password length
	passlen = len(testpass)
	
	#print('\n' + password + ',' + str(plen))
	
	
	chars = 0
	
	if containsNumbers(testpass):
		chars += 10
		
	if containsLetters(testpass):
		chars += 26 * checkCase(testpass)
	
	if containsSymbols(testpass):
		chars += 32
	
	
	entrophy = passlen * (math.log10(chars) / math.log10(2))
	

	#return basescore
	return entrophy
	
#--





'''
checkTop()

testpass : password to check

Check if the current password is present in
the Top 1000 Common Passwords list.

'''
def checkTopPasswords(testpass):
	#top = {...} # set of top 1000 common passwords
	
	#top = open('top1000pass.txt','r').read().strip().split()
	
	#for x in range(0,len(wordlist)):
	#	wordlist[x] = wordlist[x].lower()
	
	global top
	
	if set(top).intersection(set([testpass])):
		#print("Password in top 1000") # True/False - password in top 1000
		return True
	
	return False

# -- End --


# dictionary
'''
checkDictionary()

testpass : password to check

Check if the current password contains any
Dictionary Words.

'''
def dictionaryCheck(testpass):
	
	global wordlist
	
	temp = ''	
	
	for x in range(len(testpass)+1,3,-1):
	
		for start in range(len(testpass)+1-x,-1,-1):
			temp = testpass[start:start+x]
			#print(temp.lower())
			
			if temp.lower() in wordlist:
				return temp
				
				## check length of found dictionary word
				## minus points based on length of found word
				## compared to length of password ???
			
		#--
		
	#--
	
	return None

# -- End --


# leet speak

'''
checkLeetSpeak()

testpass : password to check

Check if the current password contains any Leet Speak
characters, convert to letters, and check for Dictionary words.

'''
def leetSpeakCheck(testpass):
	
	leet = {'0':'o','1':'l','2':'z','3':'e','4':'a','5':'s','6':'b','7':'t','8':'b','9':'g','@':'a','$':'s'}
	
	passlist = list(testpass)
	
	for x in range(0,len(testpass)):		
		
		if (testpass[x] in leet):
			passlist[x] = leet.get(passlist[x])
		#--
		
	#--
	
	changed = "".join(passlist)
	
	'''
	if dictionaryCheck(changed):
		#print("LEET Speak found!")
		#print("Changed password: " + changed)	
		return True
	
	else:
		return False
	'''
	
	return dictionaryCheck(changed)
	
# -- End --


# contains numbers

'''
containsNumbers()

testpass : password to check

Check if the current password contains numbers

'''
def containsNumbers(testpass):

	if any(x.isdigit() for x in testpass):
		return True
	else:
		return False



	'''
	count = 0
	
	numbers = set(string.digits)
	
	for pos in range(0,len(testpass)-1):
		if testpass[pos] in numbers:
			count += 1
		#--
	#--
	
	if count > 1:
		print("Password contains numbers")
	elif count == 1:
		print("Password only contains one number")
	else:
		print("Password does not contain numbers!")
	'''

# -- End --

# contains letters

'''
containsLetters()

testpass : password to check

Check if the current password contains letters.

'''
def containsLetters(testpass):


	if any(x.isalpha() for x in testpass):
		return True
	else:
		return False


	'''
	count = 0
	
	letters = set(string.ascii_letters)
	
	for pos in range(0,len(testpass)-1):
		if testpass[pos] in letters:
			count += 1
		#--
	#--
	
	if count > 1:
		print("Password contains letters")
	elif count == 1:
		print("Password only contains one letter")
	else:
		print("Password does not contain letters!")
	'''
		
# -- End --

# contains symbols

'''
containsSymbols()

testpass : password to check

Check if the current password contains symbols.

'''
def containsSymbols(testpass):
	
	regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
	
	if not regex.search(testpass) == None:
		#print("S")
		return True
	else:
		#print("no S")
		return False
	
	'''
	count = 0

	alphanum = set(string.digits + string.ascii_letters)
	
	for pos in range(0,len(testpass)-1):
		if testpass[pos] not in alphanum:
			count += 1
		#--
	#--
	
	if count > 1:
		print("Password contains symbols")
	elif count == 1:
		print("Password only contains one symbol")
	else:
		print("Password does not contain symbols!")
	'''
	
#--

# phone

def checkPhoneNumber(testpass):
	
	digitCount = 0
	
	digits = set(string.digits)
	
	if len(testpass) == 11:
		for d in testpass:
			#print(testpass[d])
			if d in digits:
				digitCount += 1
			else:
				digitCount = 0
	
	#print(digitCount)
	
	if digitCount == 11:
		#print("Potential phone number!")
		return True
	else:
		return False


# -- End --


'''
checkStart()

testpass : password to check

Check if the current password begins with an
uppercase letter.

'''
def checkStartLetter(testpass):
	
	firstchar = testpass[0]
	
	upper = set(string.ascii_uppercase)
	
	if firstchar in upper:
			#print("Password starts with Uppercase Letter")
			return True
	else:
		return False
	
# -- End --

'''
checkEnd()

testpass : password to check

Check if the current password ends with a
Number or Symbol.

'''
def checkEndNumber(testpass):

	lastchar = testpass[len(testpass)-1]
	
	numbers = set(string.digits)
	letters = set(string.ascii_letters)
	
	#if lastchar in numbers:
	#	print("Password ends with Number")
	#elif lastchar not in letters:
	#	print("Password ends with Symbol")
	
	if (lastchar in numbers):
		return True
	else:
		return False
	
# -- End --

def checkEndSymbol(testpass):
	
	lastchar = testpass[len(testpass)-1]
	numbers = set(string.digits)
	letters = set(string.ascii_letters)
	
	if (lastchar not in numbers) and (lastchar not in letters):
		return True
	else:
		return False
#--

'''
checkCase()

testpass : password to check

Check if the current password contains both
upper and lower case letters.

'''
def checkCase(testpass):
	
	# check for lower/upper case letters
	
	complexity = 0
	
	lower = False
	upper = False

	
	if any(x.isupper() for x in testpass):
		complexity += 1
	
	if any(x.islower() for x in testpass):	
		complexity += 1	
	
	return complexity
	
# -- End --		



'''
checkRepeat()

testpass : password to check

Check if the current password contains any repeated
characters, of 3 or more iterations.

e.g. 5555, ppp

'''
def checkRepeatChar(testpass):
	
	rcount = 0
	
	for i in range(0,len(testpass)):
		
		try:
			char1 = testpass[i]
			char2 = testpass[i+1]
		
			#print(char1)
			#print(char2)
			
			if (char1 == char2):
				if (rcount == 0):
					rcount += 2
				else:
					rcount += 1
			else:
				
				if (rcount >= 3):
					return True
				#--
			
				rcount = 0
			#--
			
			
			if (i + 1) ==  len(testpass):
				if (rcount >= 3):
					return True
				#--
			#--
			
			
		except:
			if (rcount >= 3):
				return True
			#--
	#--
	
	# no repeated characters
	return False
	

# -- End --


'''
checkSequence()

testpass : password to check

Check if the current password contains any alphanumerical
sequences, of length 3 or more.

e.g. 456, abcdefg

'''
def checkSequence(testpass):

	seqcount = 0

	for pos in range(0,len(testpass)):
	
		try:
			#print(testpass[pos])
			#print(testpass[pos+1])
		
			char1 = ord(testpass[pos])
			char2 = ord(testpass[pos + 1])
		
			if (char2 == (char1 + 1)):
				if (seqcount == 0):
					seqcount += 2
				else:
					seqcount += 1
			else:
			
				if seqcount >= 3:
					return True
				#--
				
				seqcount = 0
			#--
		except:
			if seqcount >= 3:
				return True
			#--	
		
	#--
	
	for pos in range(0,len(testpass)):
	
		try:
			#print(testpass[pos])
			#print(testpass[pos+1])
		
			char1 = ord(testpass[pos])
			char2 = ord(testpass[pos + 1])
		
			if (char2 == (char1 - 1)):
				if (seqcount == 0):
					seqcount += 2
				else:
					seqcount += 1
			else:
			
				if seqcount >= 3:
					return True
				#--
				
				seqcount = 0
			#--
		except:
			if seqcount >= 3:
				return True
			#--	
		
	#--
	
	# no sequence found
	return False

# -- End --



'''
checkPattern()

testpass : password to check

Check if the current password contains any repeated
patterns.

e.g. qweqwe, passpass, 4545

'''
def checkPattern(testpass):
	
	temp = ''
	
	halflen = int(len(testpass) / 2)
	
	for x in range(2,halflen+1):
	
		for start in range(0,len(testpass)+1-x):
			check = testpass[start:start+x]
			#print("Check: " + check)
			
			against = testpass[start+x:start+(x*2)]
			#print("Against: " + against)
			
			if (check == against):
				#print("Pattern Found: " + check + against)
				return True
				break
			#--
		#--
		
	#--
	
	return False
	
		
		
	
# -- End --


'''
checkKeyboard()

testpass : password to check

Check if the current password contains any keyboard
sequences, of length 4 or more.

e.g. qwerty, asdf

'''
def checkKeyboard(testpass):

	keyboard = [
		['q','w','e','r','t','y','u','i','o','p'],
		['a','s','d','f','g','h','j','k','l'],
		['z','x','c','v','b','n','m']
	]

	keycount = 0

	for pos in range(0,len(testpass)):
	
		try:	
			char1 = testpass[pos]
			char2 = testpass[pos+1]
		
			#print(char1)
			#print(char2)
		
			for x in range(0,3): # for each row
				for y in range(len(keyboard[x])-1): # for each key in row
					
					if char1 == keyboard[x][y]:
						
						if (char2 == keyboard[x][y+1]):						
							if (keycount == 0):
								keycount += 2
							else:
								keycount += 1
						else:
						
							if (keycount >= 4):
								return True
								
							keycount = 0
						#--
			
					#--
					
				#--
			
			#--
		
		except:
			if (keycount >= 4):
				return True

	#--
	
	# no keyboard sequence
	return False

# -- End --


def checkRange(score):
	
	## limit score to between 0 - 100
	if score > 100:
		score = 100
	elif score < 0:
		score = 0
	
	return score





#########################
## -- Main Function -- ##
#########################

def getScore(password):
	
	current_pass = password
	
	score = 0
	
	## -- Check Top 1000 Passwords -- ##
	
	if checkTopPasswords(current_pass):
		#print("Top 1000")
		return  score # common password => very weak!
	
	
	## -- Dictionary Checks -- ##
	
	
	# Base Score for Password
	score = getBaseScore(current_pass)
	
	#print("BASE SCORE " + str(score))
	'''
	if not dictionaryCheck(current_pass): # no dictionary word(s) found
		if leetSpeakCheck(current_pass):
			#print("LEET Dictionary Word -10")
			# score minus points
			score -= 20
	else:
		#print("Dictionary Word -10")
		# found dictionary work
		score -= 20
	'''
	
	dictionaryword = dictionaryCheck(current_pass)
	
	leetword = leetSpeakCheck(current_pass)
	
	if not dictionaryword == None: ## dictionary word found...
			
		if (not leetword == None) and (len(leetword) > len(dictionaryword)):
			
			minus = (len(leetword) / len(current_pass))
			score -= minus * score
			
		else:
			## remove points for dictionary word
			minus = (len(dictionaryword) / len(current_pass))
			
			score -= minus * score
		
		
	
	## -- Complexity -- ##	
	
	
	# add other checks...
	
	if checkStartLetter(current_pass):
		#print("Start with Capital -5")
		score -= score * 0.05
	
	if checkPhoneNumber(current_pass):
		# password may be phone number
		score -= score * 0.05
		
	if checkEndNumber(current_pass):
		#print("End with Number -5")
		score -= score * 0.05
		
	if checkEndSymbol(current_pass):
		#print("End with Symbol -5")
		score -= score * 0.05
	
	## -- Repeats/Patterns/Sequences -- ##
	
	if checkRepeatChar(current_pass):
		#print("Repeat -5")
		score -= score * 0.10
	
	if checkSequence(current_pass):
		#print("Sequence -5")
		score -= score * 0.10
	
	if checkPattern(current_pass):
		#print("Pattern -5")
		score -= score * 0.10
	
	if checkKeyboard(current_pass):
		#print("Keyboard Sequence -5")
		score -= score * 0.10
	
	# check score in range 0 - 100
	score = checkRange(score)
	
	#TWOPLACES = Decimal(10) ** -2 
	
	#return Decimal(score).quantize(TWOPLACES)
	
	return score
	
	
	
	
	
	
	
	
#--
