# This program is used to assign tasks to users and to keep track of those tasks

#=====importing libraries===========
# import the datetime function from datetime to get today's date later in the pogram
from datetime import datetime

#====Defining Functions====
# defining the function to register a new user
def reg_user():
# if the user is not 'admin' a message is displayed telling them they can't add a new user	
	if usrname != "admin":
		print("Sorry, only \"admin\" can register new users!")
	else:
# if the current user is admin ask for the username of the new user
		print("\nLet's add a new user:\n")
		new_usrname = input("Please enter a username: ")
		
# if the new username is already taken by a registered user, display an error and reprompt
		while True:
			if new_usrname in users:
				new_usrname = input("That username already exists. Please try another: ")
			else:
				break
		
# if the new username is unique, ask for a password and a confirmation
		while True:
			new_paswrd = input("Please enter a password: ")
			new_paswrd_confirm = input("Please confirm the password: ")
# if the passwords match write the new username and password to "user.txt"
			if new_paswrd == new_paswrd_confirm:
				with open("user.txt", "a") as user_txt:
					user_txt.write(f"\n{new_usrname}, {new_paswrd}")
				break
# if the passwords do not match, print an error and reprompt			
			else:
				print("Sorry, the passwords do not match. Please try again.\n")
 
# defining the function to add a new task
def add_task():
	print("\nLet's add a new task\n")
# prompt for a username to which the task should be assigned	
	while True:			
		usr_add_task = input("To which username should the task be assigned? ")
# if the username is registered break the loop and continue with the function		
		if usr_add_task in users:
			break
# if not, an error message is desplayed and the user is prompted again
		else:
			print("Please enter a valid username.")

# ask for a title, description and due date for the task
	task_titel = input("What is the title of the task? ")
	task_descript = input("Please give a complete description of the task:\n").replace(",", "")
	task_due_date = input("When is the task due for completion? ")
# get today's date
	today = datetime.today().strftime("%d %b %Y")		
# write all of the task details to "tasks.txt"	
	with open("tasks.txt", "a") as tasks_txt:
		tasks_txt.write(f"\n{usr_add_task}, {task_titel}, {task_descript}, {today}, {task_due_date}, No")

# defining the function to display all tasks
def view_all():
	print("_"*120 + "\n")
# open "tasks.txt" and cast each line to a list, splitting at every ", "
	with open("tasks.txt", "r") as tasks_txt:
		for line in tasks_txt:
			task = line.strip("\n").split(", ")
# print all of the task information in a user friendly manner
			print(
				f"{'Task:' :<20} {task[1]}"\
				f"\n{'Assigned to:' :<20} {task[0]}"\
				f"\n{'Date assigned:' :<20} {task[3]}"\
				f"\n{'Due date:' :<20} {task[4]}"\
				f"\n{'Task complete?' :<20} {task[5]}"\
				f"\nTask description:\n\t{task[2]}\n"\
			)
		print("_"*120)
			
# defining the function to view the current user's tasks
# the user will then have the option to mark a task as complete
# or edit the due date or reassigne the task to another user
def view_mine():
# make a list of users with tasks assigned by reading the first column in "tasks.txt"
	with open("tasks.txt", "r") as tasks_txt:
		tasked_users = []
		for line in tasks_txt:
			tasked_users.append(line.split(",")[0])
			
# if the current user is in the list of tasked users go on with the function logic
		if usrname in tasked_users:
			print("_"*120 + "\n")
			print("Your assigned tasks are:\n")		

# read through "tasks.txt" again and split the tasks into 2 lists
# one list containing the current user's tasks, and one containing all other tasks
			with open("tasks.txt", "r") as tasks_txt:
				my_tasks = []
				not_my_tasks = []
# initiate a counter for the number of tasks asigned to the user
				task_counter = 0
				for line in tasks_txt:
					task = line.strip("\n").split(", ")
# if a task belongs to the current user print out the task details along with the counter					
					if task[0] == usrname:
						task_counter += 1
						my_tasks.append(task)
						print(
							f"\t\033[1mTask {task_counter}\033[0m"\
							f"\n{'Task:' :<20} {task[1]}"\
							f"\n{'Assigned to:' :<20} {task[0]}"\
							f"\n{'Date assigned:' :<20} {task[3]}"\
							f"\n{'Due date:' :<20} {task[4]}"\
							f"\n{'Task complete?' :<20} {task[5]}"\
							f"\nTask description:\n\t{task[2]}\n"\
						)
# if the task does not belong to the user append it to "not_my_tasks"					
					else:
						not_my_tasks.append(task)	
				print("_"*120)
				
# ask the user if they want to edit a task, the tasks are selected using the counter	
				task_num = int(input("Which task number do you want to edit? If you do not want to edit a task enter \"-1\"\n:"))
# if the user enters "-1" they are taken back to the menu
				if (task_num != -1) and (task_num <= task_counter):
					
# if the user inputs a task number and the task has not bee completed, they are taken to the "mark_menu"					
					if my_tasks[task_num-1][5] == "No":
						while True:
							mark_menu = input(
								f"\nYou have selected task {task_num}."\
								f"\n{'m' :<5} - Mark as complete"\
								f"\n{'et' :<5} - Edit task\n:"
							)

# if the user inputs "m" the current task is marked as complete
							if mark_menu == "m":
								my_tasks[task_num-1][5] = "Yes"
								print("Task marked as complete!")
								break
# if the user inputs "et" they are taken to the "edit_menu"
							elif mark_menu == "et":
								while True:
									edit_menu = input(
										"\nWhich would you like to edit?"\
										f"\n{'u' :<5} - Assign task to another user"\
										f"\n{'d' :<5} - Change the due date\n:"
									)
# if the user selects "u" from the edit menu they can reasign the task to a different user
									if edit_menu == "u":
										while True:	
											et_user = input("To Which user do you want to assign the task?\n:")
# if the username exists, reasign the task, otherwise print an error								
											if et_user in users:
												my_tasks[task_num-1][0] = et_user
												print("Task reassigned!")
												break
											else:
												print("Sorry, that user does not exist.")
										break
# if they select "d" they can change the due date of the task							
									elif edit_menu == "d":
										my_tasks[task_num-1][3] = input("What is the new due date of the task?\n:")
										print("Date updated!")
										break								
# if the user inputs something invalid at the mark or edit menu a error is displayed
									else:
										print("Sorry, that's not a valid option. Please try again.")
								break
							else:
								print("Sorry, that's not a valid option. Please try again.")
# if the selected task has already been completed a message is displayed
					else:
						print("That task has already been completed and cannot be edited.")
						view_mine()			
				elif task_num == -1:
					print("Returning to menu")				
				else:
					print("Sorry, that is not a valid task number.")
					view_mine()
# if the user has no tasks assigned a message is displayed
		else:
			print("You have no assigned tasks")
	
# write the task file with any changes that have been made by the user	
	with open("tasks.txt", "w") as tasks_txt:
# create an empty string to store all tasks
		all_tasks = ""

# iterate over the user tasks and append the first 4 fields seperated by commas
		for line in my_tasks:
			for i in range(0,5):
				all_tasks += f"{line[i]}, "
# append the last field and a newline character
			all_tasks += f"{line[5]}\n"
# do the same thing over the non-user tasks
		for line in not_my_tasks:
			for i in range(0,5):
				all_tasks += f"{line[i]}, "
			all_tasks += f"{line[5]}\n"
		
# strip the newline character from the end of the string and write it to "tasks.txt"		
		tasks_txt.write(all_tasks.strip("\n"))

# define the function to generate reports
def generate_reports():
# open "tasks.txt" to get information about the tasks
	with open("tasks.txt", "r") as tasks_txt:
# initiate variables for the total numebr of tasks, the pending tasks, and the overdue tasks
		num_tasks = 0
		num_pending_tasks = 0
		num_overdue_tasks = 0
# get today's date		
		today  =  datetime.today()
		
# for each line in tasks, add one to the total tasks		
		for line in tasks_txt: 
			num_tasks += 1
			task = line.strip("\n").split(", ")
# if the task is not completed, add one to the pending tasks			
			if task[5] == "No":
				num_pending_tasks += 1
# if the task is pending and today is later than the due date, add one to overdue tasks				
				if datetime.strptime(task[3], "%d %b %Y") < today:
					num_overdue_tasks += 1

# writing the details about the tasks to "task_overview.txt"	
	with open("task_overview.txt", "w") as task_overview_txt:
		task_overview_txt.write(
			f"\n{'Total number of tasks:' :<40} {num_tasks}"\
# the completed tasks are the total tasks minus the pending tasks			
			f"\n{'Number of completed tasks:' :<40} {num_tasks - num_pending_tasks}"\
			f"\n{'Number of pending tasks:' :<40} {num_pending_tasks}"\
			f"\n{'Number of pending tasks overdue:' :<40} {num_overdue_tasks}\n"\
# the % of pending tasks is the pending tasks divided by total tasks			
			f"\n{'Percentage of tasks still pending' :<40} {round(num_pending_tasks/num_tasks*100)}%"\
# the % of overdue tasks is the overdue tasks divided by total tasks
			f"\n{'Percentage of tasks overdue:' :<40} {round(num_overdue_tasks/num_tasks*100)}%\n"
		)
	
# writing the details about the users to "user_overview.txt"	
	user_overview_txt = open("user_overview.txt","w")
# read "user.txt" to get data on the users
	with open("user.txt", "r") as user_txt:
# initiate the number of users at 0		
		num_users = 0
		
# iterate over the file and reset the number of user tasks, pending user tasks and overdue tasks to 0
# add one to the total number of users		
		for line in user_txt:
			num_user_tasks = 0
			usr_pending_tasks = 0
			usr_overdue_tasks = 0
			num_users += 1

# iterate over the list of tasks once for each user in the list of users 			
			gr_user = line.split(", ")[0]
			with open("tasks.txt", "r") as tasks_txt:
				for line in tasks_txt:
					task = line.strip("\n").split(", ")
# if a tasks exists for the user, add 1 to the number of user tasks					
					if gr_user == task[0]:
						num_user_tasks += 1
# if the task has not been completed, add 1 to the pending tasks						
						if task[5] == "No":
							usr_pending_tasks += 1
# if the task has not been completed and today is later tham the due date, add one to overdue tasks							
							if datetime.strptime(task[3], "%d %b %Y") < today:
								usr_overdue_tasks += 1
			
# write the details for the current user ("gr_user")			
			user_overview_txt.write(
				f"\n\t{gr_user}"\
				f"\n{'Number of tasks assigned to user:' :<50} {num_user_tasks}"\
				f"\n{'Percentage of total tasks assigned to user' :<50} {round(num_user_tasks/num_tasks*100)}%"
			)
# to avoid an error of dividing by 0, print NA if the user has no tasks assigned			
			if num_user_tasks == 0:
				user_overview_txt.write(
					f"\n{'Percentage of user tasks still pending:' :<50} #NA"\
					f"\n{'Percentage of user tasks overdue:' :<50} #NA\n"
				)
# otherwise calculate the percentages and write them
			else:
				user_overview_txt.write(
					f"\n{'Percentage of user tasks still pending' :<50} {round(usr_pending_tasks/num_user_tasks*100)}%"\
					f"\n{'Percentage of user tasks overdue:' :<50} {round(usr_overdue_tasks/num_user_tasks*100)}%\n"
				)
	print("Reports generated!")
# close the file when done with all users	
	user_overview_txt.close()

# defining the function to print out statistics
def get_statistics():
# read the user and task overview files	
	with open("user_overview.txt", "r") as user_overview_txt:
		user_overview = user_overview_txt.read()
		with open("task_overview.txt", "r") as task_overview_txt:
			task_overview = task_overview_txt.read()
# print the files, each with a header			
			print(
				"\033[1mUser overview:\033[0m"
				+ user_overview
				+ "\n\033[1mTask overview:\033[0m"
				+ task_overview
			)
										
#====Login Section====
# create empty lists to store the usernames and the usernames with their corisponding passwords
users = []
usrname_password = []

# a text file "user.txt" which contains all of the users currently on the system is opened
with open("user.txt", "r") as user_txt:
# iterating over this file each line is appended to the list containing both username and password
# the first word of each line is appended to the list "users"
		for line in user_txt:
			usrname_password.append(line.strip("\n"))
			users.append(line.split(", ")[0])

# a bool called "entering_details" is used to keep a while loop running
# while it is true the user is prompted to enter a username and a password		
entering_details = True
while entering_details:
	usrname = input("Username: ")
	paswrd = input("Password: ")	
	
# iterating over the list "usrname_password", a new list "pair" is created from each entery
# this "pair" list contains a username and its coresponding password	
	for line in usrname_password:
		pair = line.split(", ")
# if the username and password entered by the user both apear in the same "pair" list
# "entering_details" becomes false and we proceed to the menu section		
		if (usrname == pair[0]) and (paswrd == pair[1]):
			entering_details = False
# if the user did not enter a valid username and password pair an error is printed
# the user will again be asked for a username and password
	if entering_details:
			print("sorry, try again")

#====Menu Section====
# a while loop is used to display a menu to the user
# this menu will be displayed everytime a user either finishes a selected operation or makes an incorrect selection
# when "e" is selected it ends the loop and the program
# there is a hidden "statistic" menu item only available to "admin"
while True:
	print(
		"\n\nSelect one of the following Options below:"\
		f"\n{'r' :<5} - Registering a user"\
		f"\n{'a' :<5} - Adding a task"\
		f"\n{'va' :<5} - View all tasks"\
		f"\n{'vm' :<5} - View my task"
	)
		
# if current username is "admin" also display menu option "s - Statistics"
	if usrname == "admin":
		print(
			f"{'s' :<5} - Statistics"\
			f"\n{'gr' :<5} - Generate reports"
		)
	print(f"{'e' :<5} - Exit\n")

# the user's input gets saved as a variable "menu" which get's used to determine which section gets displayed next 
	menu = input(": ").lower()

#====Selection Section====	
# get the user's selection and call the relevant function
	if menu == "r":
		reg_user()
	elif menu == "a":
		add_task()
	elif menu == "va":
		view_all()				
	elif menu == "vm":
		view_mine()
# to select the generate reports or get statistics selection, the user must be admin
	elif (menu == "gr") and (usrname == "admin"):
		generate_reports()
	elif (menu == "s") and (usrname == "admin"):
		get_statistics()
	elif menu == "e":
		print('Goodbye!!!')
		exit()

# if the user does not make valid menu selection a error message is displaid
	else:
		print("You have made a wrong choice, Please Try again\n")