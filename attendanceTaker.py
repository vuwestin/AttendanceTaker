from tkinter import *

class Student:
	def __init__(self,firstName, lastName, email, prof, sectionNum):
		self.firstName = firstName
		self.lastName = lastName
		self.email = email
		self.prof = prof
		self.sectionNum = sectionNum
		self.daysPresent = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		#30 sessions total

	def addDay(self, week,day):
		self.daysPresent[((week-1) * 2 - 1) + day] = 1

class classDatabase:
	def __init__(self, courseName, leaderName, dayAndTimeOfSession, numSessions):
		self.courseName = courseName
		self.leaderName = leaderName
		self.dayAndTimeOfSession = dayAndTimeOfSession
		self.numSessions = numSessions
		self.dataBase = []

	def addStudent(self, student):
		self.dataBase.append(student)

	def containsStudent(self, student):
		if student in self.dataBase:
			return True
		return False

	def printAllStudents(self):
		for x in self.dataBase:
			print(x.daysPresent)


	def deleteStudent(self, studentName):
		for x in self.dataBase:
			if x.studentName == studentName:
				self.dataBase.remove(x)

	def saveDatabase(self):
		f = open("attendance.txt", "w+")
		for x in self.dataBase:
			writeStr = x.firstName + "," + x.lastName + "	" + x.email + "	" + x.prof + "	" + x.sectionNum + "	" + str(len(x.daysPresent)) + "	" + str(len(x.daysPresent)) + "	"
			for j in x.daysPresent:
				writeStr = writeStr + str(j) + ","
			writeStr = str(writeStr) + "\n"
			f.write(str(writeStr))
		f.close()

	def readDatabase(self, fileName):
		f = open(fileName, "r")
		lines = f.readlines()
		for x in lines:
			studentList = x.split("	") #split by tabs
			newStud = Student(studentList[0], studentList[1], studentList[2],
				studentList[3], studentList[4])
			daysList = studentList[6].split(",") #split by commas
			for i in range(0,30):
				newStud.daysPresent[i] = int(daysList[i])
			self.dataBase.append(newStud)

			



def main():
	db = classDatabase("dummy", "dummy1", "dummy2", "dummy3")
	# w = Student("Westin", "Vu", "vuwee", "pee", "poo")
	# #db.addStudent(w)
	# w.addDay(1,2)
	# db.readDatabase("attendance.txt")
	# db.printAllStudents()
	m = Tk(className = ' Attendance Taker')
	panel = Frame(m)
	panel.pack()
	button1 = Button(panel, text = "yeeyeeyee", bg = "red", fg = "red")
	#label1 = Label(panel, bg = "green", fg = "black")
	#label1.pack()
	weekEntry = Entry(panel, width = 5)
	weekEntry.pack()
	button1.pack()

	#m.title('Attendance Taker')
	m.mainloop()









if __name__ == "__main__":
	main()