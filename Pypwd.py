#A password generator in Python...Coded by Mcoury(python-scripter)
#import the necessary modules:
import base64
from Crypto.Hash import SHA512
import random
import pyperclip

print('+++Pypwd is a password generator in Python...Coded by Mcoury(python-scripter)+++')
print()
print()
print('Secure passwords must be strings of random characters, but humans are bad at generating random things...')
print()
print('''However, truly random strings are tricky to remember and impossible to reproduce.
Lose that precious txt file and you're out of luck!...''')
print()
print('''So I made this tool to solve the above problem,
all you have to remember is a short password (could be a name like smith),
a key a seed and 2 special characters(those are optional),
and 2 numbers(the borders of the slice the script will make)...''')
print()


plainpass=input('Please enter a password you can easily remember...')
prompt_key=input('Enter (y)es to use a multiplication key, or enter anything else if you wish to skip...').lower()
if prompt_key=='y': #A multiplication key will give potential attackers one more problem, but since it's not absolutely necessary, the user might want to skip selecting one
	mult_key=int(input('Please enter a number...'))
else:
	mult_key=1
newpass=plainpass*mult_key

def hashing():
	'''Use SHA512 to hash our password'''
	global hashedpass
	h=SHA512.new()
	bytepass=str.encode(newpass)
	h.update(bytepass)
	hashedpass=h.hexdigest()
	base64_encode()

def base64_encode():
	'''Encode the resulting hashed pass in base644 to increase length and complexity'''
	global b64_4
	bytehashedpass=str.encode(hashedpass)
	b64_1=base64.b64encode(bytehashedpass)
	b64_2=base64.b64encode(b64_1)
	b64_3=base64.b64encode(b64_2)
	b64_4=base64.b64encode(b64_3)
	select_range()

def select_range():
	'''Select a slice of the huge final base64 string '''
	global decoded_list
	print('The final base64 string is',len(b64_4),'characters long')
	print()
	print('''Now we must take a slice of that base64 string...
remember that strong passwords are at least 20 chars''')
	x=int(input('''Select the starting point of the slice, 
it must be lower than the length of the final b64 string...'''))
	y=int(input('''Select the ending point of the slice,
it must be lower than the length of the final b64 string...'''))
	chosen_slice=b64_4[x:y]
	decoded_slice=chosen_slice.decode()
	decoded_list=list(decoded_slice)
	symbol_insertion()

def symbol_insertion():
	'''give the user the choice to insert a couple special characters into the pass'''
	check=input('To insert special chracters to the final string enter (y)es, enter anything else to skip...').lower()
	if check == 'y':
		mlist=[]
		seed=int(input('Please enter the random seed...'))
		random.seed(seed)
		for i in range(30):
			choice=random.randint(10,len(decoded_list)-1)
			mlist.append(choice)
		first_symbol=input('Please enter the first symbol...')
		second_symbol=input('Please enter the 2nd symbol...')
		decoded_list.insert(mlist[4],first_symbol)
		decoded_list.insert(mlist[len(mlist)-5],second_symbol)
		finalresult=''.join(decoded_list)
		print('Your pass is', finalresult, 'and it\'s',len(finalresult),'characters long...' )
		ask=input('''Enter (y)es to copy the resulting password to clipboard, or anything else to skip...
Be advised that some apps can monitor system clipboard and even archive its contents...''').lower()
		if ask=='y':
			pyperclip.copy(finalresult)
			print('Your pass has been copied to system clipboard...')
		else:
			pass
	else:
		finalresult=''.join(decoded_list)
		print('Your pass is', finalresult, 'and it\'s',len(finalresult),'characters long...' )
		ask=input('''Enter (y)es to copy the resulting password to clipboard, or anything else to skip...
Be advised that some apps can monitor system clipboard and even archive its contents...''').lower()
		if ask=='y':
			pyperclip.copy(finalresult)
			print('Your pass has been copied to system clipboard...')
		else:
			pass

hashing()