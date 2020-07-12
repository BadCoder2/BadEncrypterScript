from cryptography.fernet import Fernet #main encryptor
import sys #general tools + read flags
import base64 #"encryption"
Arg = sys.argv #arguments = the function to get arguments
i = 0 #setting up
if sys.version_info[0] !=3: #Python3 required
	raise NotImplementedError("Required features of Python 3 not found. Please run this with python 3 (user@localhost: python3 PythonCrypts.py)") #enforce

PyCrypt = '' #error handling if text encryption is hit before PyCrypt is defined, specifically when using help function


if len(Arg) >= 2: #if there are 2 or more arguments, A, else, B
	flag = Arg[1] #the flag is the second argument (first being this file)
	if len(Arg) >= 3:
		flag2 = Arg[2]
		print('2 flags found! Image encryption activated...')
		print('Note: source images are NOT deleted when encrypted. Do it yourself (with better deletion tools)')
		with open(flag2, "rb") as image:
			read = image.read()
			b64 = base64.b64encode(read)
		with open("b64uenc.txt","wb") as text:
			text.write(b64)
			print("Unencoded added to b64uenc.txt (located in the same directory.)")
		key = Fernet.generate_key()
		print("The key for the encoded version will be printed next. DON'T LOSE THIS KEY.")
		print(key)
		f = Fernet(key)
		b64e = f.encrypt(b64)
		with open ("b64enc.txt","wb") as text:
			text.write(b64e)
			print("Encoded added to b64enc.txt (located in the same directory.)")

	else:
	
		print("1 flag found. This is the first step!") #say there is a flag
		print('DEBUG::: FLAG =',flag)
		PyCrypt = 'crypt' #mark the modifier to say there is a flag
else:	
	while i < 4:
		PyCrypt = input("No flag found. Input Y to continue with basically no encryption, D to decrypt an image or text, or N to stop. If you wish to get help, input H.") #say there is no flag
		if PyCrypt == 'Y': #if they still want to go on
			print("No encryption selected. Moving on...") #say "ok"
			PyCrypt = 'skip' #mark the modifier to say no encryption
			break #leave loop
		elif PyCrypt == 'N': #if they don't want to go on
			raise InterruptedError("ENDED") #end it
		elif PyCrypt == 'H':
			print("Help has been activated.")
			print("For NO encryption, please rerun with NO flags and input Y at the prompt.")
			print("For standard text encryption, rerun with 1 flag (anything)")
			print("For image encryption, run with 2 flags (user@localhost:python3 PythonCrypts.py [anything] [image file name/path]")
		elif PyCrypt == 'D':
			raise ModuleNotFoundError('!!!!!!!!!!!!!!!!!!!!!!!!!!WORK IN PROGRESS!!!!!!!!!!!!!!!!!!!!!!!!!!')
		else: #if they said something else
			print("Unknown response. Trying again...") #tell them
			i += 1 #increment
		if i == 3:
			raise TimeoutError("No answer given.")
#-----------------------------------------------------------TEXT ENCRYPTION-----------------------------------------------------------------------------#
if PyCrypt == "crypt":
	print('DEBUG:::',PyCrypt,' expected crypt')
	print('Selected: Encrypt')
elif PyCrypt == "skip":
	print('DEBUG:::',PyCrypt,' expected skip')
