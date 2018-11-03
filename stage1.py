#quick functions for:
#1. print hello
#2. ask for name
#3. choice a problem
#----------database---------------------------------------
#creating a dictionary forum to send to the data basestring

database = {}
#--------------printing dictionaries------------------------
def print_dictionary(dicts):
	for key, value in dicts.items():
		print key, ": ", value
	
#----------------ticket number --------------------------------
import random

value = random.randint(1, 100)
print (value, "Your Ticket Number!")
#----------------Dictionarys---------------------------------------
import collections
problem_choice_noorder = {
	'option 1': 'The screen is frozen',
	'option 2': 'computer is slow',
	'option 3': 'strange noises',
}
problem_choice = collections.OrderedDict(sorted(problem_choice_noorder.items()))

location_choice_noorder = {
	'option 1': 'Marketing',
	'option 2': 'Sales',
	'option 3': 'Human Resource',
	'option 4': 'Accounting',
	'option 5': 'CEO',
}
location_choice = collections.OrderedDict(sorted(location_choice_noorder.items()))
critical_level_noorder = {
	'level 1': 'ok',
	'level 2': 'bad',
	'level 3': 'very bad',
	'level 4': 'immediate help',
}
critical_level = collections.OrderedDict(sorted(critical_level_noorder.items()))

def intro():
	print "Hello user, welcome to your help desk."
	print "We will ask you a few personal questions about your self."

print "-"*50
def user_name():
	print "Please enter your name."
	# global allows you to reference a varible from outside the funcation 
	global name
	# once you define the global varibale you can ask for a equal the name and recall it anywhere in the code. 
	name = raw_input("> ")
	#adding user name to our dictory form to send to the database
	#to do this 
	#dictory_name[new key to instert] = new value for the key 
	# check below
	database["name"] = name 
	
	print "-"*50	

def user_email():
	print "Please enter your email address."
	global email
	email = raw_input("> ")
	database["email"] = email
	print "-"*50	

def user_location():
	print "From the list below, Please section your department."
	print("DEBUG TEST")
	print_dictionary(location_choice)
	global location
	location = raw_input("> ")
	database["location"] = location
	
	print "-"*50	

def issue_level():
	print "Please select from the list below how critical is your problem."
	print_dictionary(critical_level)
	global level
	level = raw_input("> ")
	database["level"] = level
		
	print"-"*50	

def problem_selection():
	print "Please select the number referring to your problem."
	#for python to display the options in the dictory we most select
	#the key and vlaue. for example option 1 is a 'key' and the 'value' is screen frozen
	#so to print this we tell python for key and value in the dictory above	
	#the important thing is to use 'items and then print both.
	print_dictionary(problem_choice)
	global problem
	problem = raw_input("> ")
	database["problem"] = problem
	print "_"*50
	
def print_database():
	print "Below is the information you have entered, please check if its correct?"
	database_ordered = collections.OrderedDict(sorted(database.items()))
	print_dictionary(database_ordered)
	print "_"*50

def start():
	intro()
	user_name()
	user_email()
	user_location()
	issue_level()
	problem_selection()
	print_database()


	
	
	
start()

