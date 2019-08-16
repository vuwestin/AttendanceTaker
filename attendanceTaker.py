from tkinter import *
from os import path

class Student:
	def __init__(self,name, email, prof, sectionNum):
		#self.firstName = firstName
		self.name = name
		self.email = email
		self.prof = prof
		self.sectionNum = sectionNum
		self.daysPresent = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		#30 sessions total

	def addDay(self, week,day, val):
		self.daysPresent[((week-1) * 2 - 1) + day] = val

class classDatabase:
	def __init__(self, courseName, leaderName, dayAndTimeOfSession, numSessions):
		self.courseName = courseName
		self.leaderName = leaderName
		self.dayAndTimeOfSession = dayAndTimeOfSession
		self.numSessions = numSessions
		self.dataBase = []
		#dataBase is a list of Students

	def addStudent(self, student):
		self.dataBase.append(student)

	def containsStudent(self, student):
		if student in self.dataBase:
			return True
		return False

	def printAllStudents(self):
		for x in self.dataBase:
			print(x.daysPresent)


	def deleteStudent(self, name):
		for x in self.dataBase:
			if (x.name == name):
				self.dataBase.remove(x)

	def saveDatabase(self):
		f = open("attendance.txt", "w+")
		for x in self.dataBase:
			writeStr = x.name + "," + x.email + "," + x.prof + "," + x.sectionNum + "," + str(len(x.daysPresent)) + "," + str(len(x.daysPresent)) + ","
			for j in x.daysPresent:
				writeStr = writeStr + str(j) + ","
			writeStr = str(writeStr) + "\n"
			f.write(str(writeStr))
		f.close()
		print("saves")

	def readDatabase(self, fileName):
		if path.exists(fileName):
			f = open(fileName, "r")
			lines = f.readlines()
			if len(lines) > 0:
				self.dataBase = [] #clear database
				for x in lines:
					studentList = x.split(",") #split by commas
					print(studentList)
					newStud = Student(studentList[0] + "," + studentList[1], studentList[2],
						studentList[3], studentList[4])
					#daysList = studentList[6].split(",") #split by commas
					for i in range(0,30): #FIX THIS
					#studentlist attendance is 7 to 36/37
					#new student objects attendance is from 0 to 30
						newStud.daysPresent[i] = int(studentList[i+7])
					self.dataBase.append(newStud)
			else:
				self.database = []
		else:
			self.database = []

			



#def main():
	# db = classDatabase("dummy", "dummy1", "dummy2", "dummy3")
	# # w = Student("Westin", "Vu", "vuwee", "pee", "poo")
	# # #db.addStudent(w)
	# # w.addDay(1,2)
	# # db.readDatabase("attendance.txt")
	# # db.printAllStudents()
	# m = Tk(className = ' Attendance Taker')
	# panel = Frame(m)
	# panel.pack()
	# button1 = Button(panel, text = "yeeyeeyee", bg = "red", fg = "red")
	# #label1 = Label(panel, bg = "green", fg = "black")
	# #label1.pack()
	# weekEntry = Entry(panel, width = 5)
	# weekEntry.pack()
	# button1.pack()

	# #m.title('Attendance Taker')
	# m.mainloop()









# if __name__ == "__main__":
# 	main()


