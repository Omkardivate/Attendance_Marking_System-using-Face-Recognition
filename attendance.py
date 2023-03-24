import tkinter as tk
from tkinter import ttk
import cv2, os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
from tkinter import messagebox

window = tk.Tk()

window.title("Attendance System")

window.configure(background = 'white')
window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)

x_cord = 75
y_cord = 20
checker = 0


# ATTENDANCE MANAGEMENT SYSTEM
app_name = tk.Label(
	window, text = "ATTENDANCE MANAGEMENT SYSTEM", bg = "navy", fg = "white", height = 2,
	font = ('Ariel', 35, 'bold')
)
app_name.pack(fill = tk.BOTH)

# GESCOE
college_name = tk.Label(
	window, text = "GESCOE", bg = "cyan", fg = "black", height = 2, font = ('Ariel', 25, 'bold')
)
college_name.pack(fill = tk.BOTH)

frame1 = tk.Frame(window, background = "white")
frame1.pack(fill = tk.BOTH)

# Notification lable & msg
lbl3 = tk.Label(
	frame1, text = "Notification: ", bg = "white", fg = "darkblue",height = 1, padx = 5, pady = 5,
	font = ('Ariel', 25, ' bold ')
)
lbl3.grid(row = 0, column = 0)

notification = tk.Label(
	frame1, text = "", bg = "white", fg = "green", height = 1, activebackground = "white",
	font = ('Ariel', 20, ' bold ')
)
notification.grid(row = 0, column = 1)

separator1 = ttk.Separator(window, orient = "horizontal")
separator1.pack(fill = "x")

frame2 = tk.Frame(window, background = "white")
frame2.pack(fill = tk.BOTH)

# College ID & input
lbl = tk.Label(
	frame2, text = "Enter College ID", height = 1, bg = "white", padx = 5, pady = 5,
	font = ('Ariel', 22, ' bold ')
)
lbl.grid(row = 0, column = 0)


txt = tk.Entry(frame2, bg = "white", fg = "blue",font = ('Ariel', 20, ' bold '))
txt.grid(row = 0, column = 1)

# First Name & input
lbl2 = tk.Label(
	frame2, text = "First Name", bg = "white", height = 1, padx = 5, pady = 5,
	font = ('Ariel', 22, ' bold ')
)
lbl2.grid(row = 1, column = 0)

txt2 = tk.Entry(frame2, bg = "white", fg = "blue", font = ('Ariel', 20, ' bold '))
txt2.grid(row = 1, column = 1)

# Last Name & input
lbl22 = tk.Label(
	frame2, text = "Last Name", bg = "white", height = 1, padx = 5, pady = 5,
	font = ('Ariel', 22, ' bold ')
)
lbl22.grid(row = 2, column = 0)

txt22 = tk.Entry(frame2, bg = "white", fg = "blue", font = ('Ariel', 20, ' bold '))
txt22.grid(row = 2, column = 1)

separator2 = ttk.Separator(window, orient = "horizontal")
separator2.pack(fill = "x")

frame3 = tk.Frame(window, background = "white")
frame3.pack(fill = tk.BOTH)

# Step1 label
lbl4 = tk.Label(
	frame3, text = "STEP 1", fg = "white", bg = "green", height = 1, font = ('Ariel', 20, ' bold '), padx = 5, pady = 5,
)
lbl4.grid(row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)

# Step2 label
lbl5 = tk.Label(
	frame3, text = "STEP 2", fg = "white", bg = "green", height = 1, font = ('Ariel', 20, ' bold '), padx = 5, pady = 5,
)
lbl5.grid(row = 0, column = 1, sticky = "nsew", padx = 5, pady = 5)

# Step3 label
lbl6 = tk.Label(
	frame3, text = "STEP 3", fg = "white", bg = "green", height = 1, font = ('Ariel', 20, ' bold '), padx = 5, pady = 5,
)
lbl6.grid(row = 0, column = 2, sticky = "nsew", padx = 5, pady = 5)


# Attendance label & msg
lbl3 = tk.Label(
	window, text = "ATTENDANCE", width = 20, fg = "white", bg = "gray", height = 1,
	font = ('Ariel', 25, ' bold ')
)
lbl3.pack(fill = tk.BOTH)

message2 = ttk.Treeview(window)
message2['columns'] = ('College ID', 'First Name', 'Last Name', 'Date', 'Time')
message2.pack(fill = tk.BOTH)

message2.column("#0", width = 0, stretch = tk.NO)
message2.column("College ID", anchor = tk.CENTER)
message2.column("First Name", anchor = tk.CENTER)
message2.column("Last Name", anchor = tk.CENTER)
message2.column("Date", anchor = tk.CENTER)
message2.column("Time", anchor = tk.CENTER)

message2.heading("#0", text = "", anchor = tk.CENTER)
message2.heading("College ID", text = "College ID", anchor = tk.CENTER)
message2.heading("First Name", text = "First Name", anchor = tk.CENTER)
message2.heading("Last Name", text = "Last Name", anchor = tk.CENTER)
message2.heading("Date", text = "Date", anchor = tk.CENTER)
message2.heading("Time", text = "Time", anchor = tk.CENTER)


def clear1():
	txt.delete(0, 'end')
	res = ""
	notification.configure(text = res)


def clear2():
	txt2.delete(0, 'end')
	txt22.delete(0, 'end')
	res = ""
	notification.configure(text = res)


def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		pass
	
	try:
		import unicodedata
		unicodedata.numeric(s)
		return True
	except (TypeError, ValueError):
		pass
	
	return False


def TakeImages():
	Id = (txt.get())
	name = (txt2.get())
	lname = (txt22.get())
	if not Id:
		res = "Please enter Id"
		notification.configure(text = res)
		MsgBox = tk.messagebox.askquestion(
			"Warning", "Please enter roll number properly , press yes if you understood", icon = 'warning'
		)
		if MsgBox == 'no':
			tk.messagebox.showinfo('Your need', 'Please go through the readme file properly')
	elif not name and lname:
		res = "Please enter Name"
		notification.configure(text = res)
		MsgBox = tk.messagebox.askquestion(
			"Warning", "Please enter your name properly , press yes if you understood", icon = 'warning'
		)
		if MsgBox == 'no':
			tk.messagebox.showinfo('Your need', 'Please go through the readme file properly')
	
	elif (is_number(Id) and name.isalpha() and lname.isalpha()):
		cam = cv2.VideoCapture(0)
		harcascadePath = "haarcascade_frontalface_default.xml"
		detector = cv2.CascadeClassifier(harcascadePath)
		sampleNum = 0
		while (True):
			ret, img = cam.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			faces = detector.detectMultiScale(gray, 1.3, 5)
			for (x, y, w, h) in faces:
				cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
				# incrementing sample number
				sampleNum = sampleNum + 1
				# saving the captured face in the dataset folder TrainingImage
				cv2.imwrite(
					"TrainingImage/" + name + " " + lname + "." + Id + '.' + str(sampleNum) + ".jpg",
					gray[y:y + h, x:x + w]
				)
				# display the frame
				cv2.imshow('frame', img)
			# wait for 20 miliseconds
			if cv2.waitKey(20) & 0xFF == ord('c'):
				break
			# break if the sample number is morethan 20
			elif sampleNum > 20:
				break
		cam.release()
		cv2.destroyAllWindows()
		res = "Images Saved for ID : " + Id + " Name : " + name + " " + lname
		row = [Id, name, lname]
		# fill data in students.csv
		with open('StudentDetails/StudentDetails.csv', 'a+') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(row)
		csvFile.close()
		notification.configure(text = res)
	else:
		if (is_number(Id)):
			res = "Enter Alphabetical Name"
			notification.configure(text = res)
		if name.isalpha() and lname.isalpha():
			res = "Enter Numeric Id"
			notification.configure(text = res)


def TrainImages():
	recognizer = cv2.face_LBPHFaceRecognizer.create()
	faces, Id = getImagesAndLabels("TrainingImage")
	recognizer.train(faces, np.array(Id))
	recognizer.save("TrainingImageLabel/Trainner.yml")
	res = "Image Trained"
	clear1()
	clear2()
	notification.configure(text = res)
	tk.messagebox.showinfo('Completed', 'Your model has been trained successfully!!')


def getImagesAndLabels(path):
	imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
	
	faces = []
	
	Ids = []
	
	for imagePath in imagePaths:
		# loading the image and converting it to gray scale
		pilImage = Image.open(imagePath).convert('L')
		# Now we are converting the PIL image into numpy array
		imageNp = np.array(pilImage, 'uint8')
		# getting the Id from the image
		Id = int(os.path.split(imagePath)[-1].split(".")[1])
		# extract the face from the training image sample
		faces.append(imageNp)
		Ids.append(Id)
	return faces, Ids


def TrackImages():
	recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
	recognizer.read("TrainingImageLabel/Trainner.yml")
	harcascadePath = "haarcascade_frontalface_default.xml"
	faceCascade = cv2.CascadeClassifier(harcascadePath)
	df = pd.read_csv("StudentDetails/StudentDetails.csv")
	cam = cv2.VideoCapture(0)
	font = cv2.FONT_HERSHEY_SIMPLEX
	col_names = ['Id', 'FirstName', 'LastName', 'Date', 'Time']
	attendance = pd.DataFrame(columns = col_names)
	while True:
		ret, im = cam.read()
		gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(gray, 1.3, 5)
		for (x, y, w, h) in faces:
			cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
			Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
			if (conf < 50):
				ts = time.time()
				date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
				timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
				aa = df.loc[df['Id'] == Id]['FirstName'].values
				lname = df.loc[df['Id'] == Id]['LastName'].values
				tt = str(Id) + "-" + aa + " " + lname  # Giving label for frame
				attendance.loc[len(attendance)] = [Id, aa, lname, date, timeStamp]
			
			else:
				Id = 'Unknown'
				tt = str(Id)
			if (conf > 75):
				noOfFile = len(os.listdir("ImagesUnknown")) + 1
				cv2.imwrite("ImagesUnknown/Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
			cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
		attendance = attendance.drop_duplicates(subset = ['Id'], keep = 'first')
		cv2.imshow('im', im)
		if (cv2.waitKey(1) == ord('c')):
			break
	ts = time.time()
	date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
	timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
	Hour, Minute, Second = timeStamp.split(":")
	fileName = "Attendance/Attendance_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
	attendance.to_csv(fileName, index = False)  # create csv
	cam.release()
	cv2.destroyAllWindows()
	res = attendance
	iid = 1
	for x in attendance.values.tolist():
		message2.insert(
			parent = '', index = 'end', iid = iid, text = '',
			values = (x[0], x[1][0], x[2][0], x[3], x[4])
		)
		iid += 1
	#message2.configure(text = res)
	res = "Attendance Taken"
	notification.configure(text = res)
	tk.messagebox.showinfo('Completed', 'Congratulations ! Your attendance has been marked successfully for the day!!')


def quit_window():
	MsgBox = tk.messagebox.askquestion(
		'Exit Application', 'Are you sure you want to exit the application', icon = 'warning'
	)
	if MsgBox == 'yes':
		# tk.messagebox.showinfo("Greetings", "Thank You very much for using our software. Have a nice day ahead!!")
		window.destroy()


takeImg = tk.Button(
	frame3, text = "CAPTURE IMAGE", command = TakeImages, fg = "white", bg = "#00BFFF", width = 25, height = 1,
	activebackground = "darkblue", font = ('Ariel', 15, ' bold '), activeforeground = "white"
)
takeImg.grid(row = 1, column = 0, sticky = "nsew", padx = 5, pady = 5)

trainImg = tk.Button(
	frame3, text = "TRAIN MODEL", command = TrainImages, fg = "white", bg = "#00BFFF", width = 25, height = 1,
	activebackground = "darkblue", font = ('Ariel', 15, ' bold '), activeforeground = "white"
)
trainImg.grid(row = 1, column = 1, sticky = "nsew", padx = 5, pady = 5)

trackImg = tk.Button(
	frame3, text = "MARK ATTENDANCE", command = TrackImages, fg = "white", bg = "#00BFFF", width = 28, height = 1,
	activebackground = "darkblue", font = ('Ariel', 15, ' bold '), activeforeground = "white"
)
trackImg.grid(row = 1, column = 2, sticky = "nsew", padx = 5, pady = 5)

quitWindow = tk.Button(
	window, text = "QUIT", command = quit_window, fg = "white", bg = "red", width = 8, height = 2,
	activebackground = "pink", font = ('Ariel', 10, ' bold ')
)

window.mainloop()
