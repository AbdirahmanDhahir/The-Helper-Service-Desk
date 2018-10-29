#quick functions for:
#1. print hello
#2. ask for name
#3. choice a problem
#----------------Global Variables--------------------------------
#name
#email
#address
#----------------Dictionarys---------------------------------------
problem_choice = {
	'option 1': 'The screen is frozen',
	'option 2': 'computer is slow',
	'option 3': 'strange noises',
}
location_choice = {
	'option 1': 'Marketing',
	'option 2': 'Sales',
	'option 3': 'Human Resource',
	'option 4': 'Accounting',
	'option 5': 'CEO',
}
critical_level = {
	'level 1': 'ok',
	'level 2': 'bad',
	'level 3': 'very bad',
	'level 4': 'immediate help',
}

def intro():
	print "Hello user, welcome to your help desk."
	print "We will ask you a few personal questions about your self."
	
def user_name():
	print "Please enter your name."
	# global allows you to reference a varible from outside the funcation 
	global name
	# once you define the global varibale you can ask for a equal the name and recall it anywhere in the code. 
	name = raw_input("> ")
	
def user_email():
	print "Please enter your email address."
	global email
	email = raw_input("> ")
	
def user_location():
	print "From the list below, Please section your department."
	for key,value in location_choice.items():
		print(key,value)
	global location
	location = raw_input("> ")
	
def issue_level():
	print "Please select from the list below how critical is your problem."
	for key,value in critical_level.items():
		print(key,value)
	global level
	level = raw_input("> ")
	
	
def problem_selection():
	print "Please select the number referring to your problem."
	#for python to display the options in the dictory we most select
	#the key and vlaue. for example option 1 is a 'key' and the 'value' is screen frozen
	#so to print this we tell python for key and value in the dictory above	
	#the important thing is to use 'items()' and then print both.
	for key,value in problem_choice.items():
		print(key, value)
	global problem
	problem = raw_input("> ")
	
def result():
print "Blow is summry of the issue you are having."
global name
global email
global location
global level 
global problem
	
	
def start():
	intro()
	user_name()
	user_email()
	user_location()
	issue_level()
	problem_selection()
	result()
	
	
start()

