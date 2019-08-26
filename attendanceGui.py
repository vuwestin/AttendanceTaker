from attendanceTaker import Student, classDatabase
import tkinter as tk

class attendanceGui(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)
		self.classDb = classDatabase("courseName", "leaderName", "dayAndTimeOfSession", "numSessions")
		#self.classDb.readDatabase("attendance.txt")
		self.currentWeek = 0
		self.currentDay = 0

		self.container = tk.Frame(self)
		self.title("Attendance Taker V.1")
		self.container.pack(side = "top", fill = "both", expand = True)
		self.container.grid_rowconfigure(0, weight = 1)
		self.container.grid_columnconfigure(0, weight = 1)

		self.frames = {}
		self.setupFrames()
		#assign widgets to the grid

		self.show_frame(StartPage)

	def setupFrames(self):
		for F in (StartPage, addStudentPage,attPage):

			frame = F(self.container,self)

			self.frames[F] = frame

			frame.grid(row = 0, column= 0, sticky = "nsew")

	def show_frame(self, controller):
		if controller == attPage:
			self.updateClassDb("attendance.txt")
		elif controller == addStudentPage:
			self.frames[addStudentPage].clearEntries()
		frame = self.frames[controller]
		frame.tkraise()
		# self.window = Tk()
		# self.window.geometry("350x200")
		# self.panel = Frame(self.window)
		# self.panel.pack()
		# self.window.mainloop()	
		#call mainloop in main function. duh

	def setDayAndWeek(self, week, day):
		if week.isdigit() == False or day.isdigit() == False: #checks for bad input
			invalidLabel = tk.Label(self.frames[StartPage], text = "Invalid Input")
			invalidLabel.grid(row = 3, column = 1)
		else:
			week = int(week)
			day = int(day)
			if (week > 0 and week < 16) and (week > 0 and week < 3):
				self.currentWeek = str(week)
				self.currentDay = str(day)
				self.show_frame(attPage)
		#make attPage

	def addStud(self, name, email, prof, sectionNum):
		self.classDb.addStudent(Student(name, email, prof, sectionNum))
		self.classDb.saveDatabase()
		self.show_frame(StartPage)
		#added students not showing in attpage

	def saveClassDb(self, checkBoxList):
		presentList = []
		for x in checkBoxList:
			#presentList is a list of tk.IntVar()
			if x.get():
				presentList.append(1)
			else:
				presentList.append(0)
		for x in range(0, len(presentList)):
			self.classDb.dataBase[x].addDay(int(self.currentWeek),int(self.currentDay), presentList[x])

		self.classDb.saveDatabase()
		self.show_frame(StartPage)

	def updateClassDb(self, filename):
		self.classDb.readDatabase(filename)
		#print("update")
		# container = tk.Frame(self)
		# container.pack(side = "top", fill = "both", expand = True)
		# container.grid_rowconfigure(0, weight = 1)
		# container.grid_columnconfigure(0, weight = 1)
		self.frames[attPage] = attPage(self.container,self)
		self.frames[attPage].grid(row = 0, column= 0, sticky = "nsew")

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = "Attendance Taker V 1.0")
		label.grid(row = 0, column = 0)

		weekLabel = tk.Label(self, text = "Week")
		weekLabel.grid(row = 1, column = 0)

		entry1 = tk.Entry(self,width = 5)
		entry1.grid(row = 1, column = 1)

		dayLabel = tk.Label(self, text = "Day (1 or 2)")
		dayLabel.grid(row = 2, column = 0)

		dayEntry = tk.Entry(self, width = 5)
		dayEntry.grid(row = 2, column = 1)

		button1 = tk.Button(self, text = "Continue", command = lambda: controller.setDayAndWeek(entry1.get(), dayEntry.get()))
		button1.grid(row = 3, column = 2)

		#add an addstudent button
		addButton = tk.Button(self,text = "Add Student", command = lambda: controller.show_frame(addStudentPage))
		addButton.grid(row = 3, column = 0)

		#button1.grid_forget()
		#grid_forget removes stuff

class addStudentPage(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self, parent)

		self.entryList = []
		addLabel = tk.Label(self, text = "Enter the name of the student to add")
		firstNameLabel = tk.Label(self, text = "First Name")
		lastNameLabel = tk.Label(self, text = "Last Name")
		emailLabel = tk.Label(self, text = "Email (without @csu.fullerton.edu)")
		profLabel = tk.Label(self, text = "Professor's Last Name")
		sectionNumLabel = tk.Label(self, text = "Class Section Number")

		firstNameEntry = tk.Entry(self, width = 10)
		self.entryList.append(firstNameEntry)
		lastNameEntry = tk.Entry(self, width = 10)
		self.entryList.append(lastNameEntry)
		emailEntry = tk.Entry(self, width = 15)
		self.entryList.append(emailEntry)
		profEntry = tk.Entry(self, width = 10)
		self.entryList.append(profEntry)
		sectionNumEntry = tk.Entry(self, width = 5)
		self.entryList.append(sectionNumEntry)
		

		backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame(StartPage))
		addButton = tk.Button(self, text = "Add", command = lambda: controller.addStud(lastNameEntry.get() + "," + firstNameEntry.get(), emailEntry.get(), profEntry.get(), sectionNumEntry.get()))

		addLabel.grid(row = 0, column = 0)
		firstNameLabel.grid(row = 1, column = 0)
		lastNameLabel.grid(row = 2, column = 0)
		emailLabel.grid(row = 3, column = 0)
		profLabel.grid(row = 4, column = 0)
		sectionNumLabel.grid(row = 5, column = 0)

		firstNameEntry.grid(row = 1, column = 1)
		lastNameEntry.grid(row = 2, column = 1)
		emailEntry.grid(row = 3, column = 1)
		profEntry.grid(row = 4, column = 1)
		sectionNumEntry.grid(row = 5, column = 1)

		backButton.grid(row = 6, column = 0)
		addButton.grid(row = 6, column = 1)

	def clearEntries(self):
		for entry in self.entryList:
			entry.delete(0,"end")


class attPage(tk.Frame):

	def __init__(self,parent,controller):
		#parent is a Frame, controller is an attendanceGui
		tk.Frame.__init__(self, parent)
		controller.classDb.readDatabase("attendance.txt")
		self.studentCounter = 0
		self.checkBoxArray = []
		for student in controller.classDb.dataBase:
			studLabel = tk.Label(self, text = (student.name))
			studLabel.grid(row = self.studentCounter, column = 0)


			self.checkBoxArray.append(tk.IntVar())

			hereCheckButton = tk.Checkbutton(self,text = "Here", variable = self.checkBoxArray[self.studentCounter])
			hereCheckButton.grid(row = self.studentCounter, column = 1)

			#self.checkBoxArray.append(hereCheckButton)
			self.studentCounter = self.studentCounter + 1

		#do this
		saveButton = tk.Button(self, text = "Save", command = lambda: controller.saveClassDb(self.checkBoxArray))
		backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame(StartPage))
		backButton.grid(row = self.studentCounter, column = 0)
		saveButton.grid(row = self.studentCounter, column = 3)
			#REDO THIS SO THAT ITS ONLY ONE CHECKBOX NEXT TO THE NAME FOR HERE
			#OR NOT
			#FIND OUT HOW TO TELL WHICH CHECKBOX GOT TICKED

def stringCount(string,c):
	count = 0
	for x in string:
		if c == x:
			count = count + 1
	return count

def main():
	p = attendanceGui()
	p.mainloop()

if __name__ == "__main__":
	main()
