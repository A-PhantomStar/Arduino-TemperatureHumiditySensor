import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from time import strftime, localtime
import serial, threading, csv

arduino = serial.Serial('COM6', 9600) #Initializes the conection with the arduino and the Serial.

def getTempHum(): #This function is made to get the data from the arduino (serial).
    valueTemp = arduino.readline()
    decoded_data = str(valueTemp[0:(len(valueTemp)-2)].decode('utf-8')) #Decodes the recived data
    split_data = decoded_data.split("x") #Split the data in two
    temp = split_data[0] 
    hum = split_data[1] 
    return temp, hum

def updateData(): #This function updates the data on the interface and creates and stores data on a csv file.
    upTemp = getTempHum()[0]
    upHum = getTempHum()[1]
    currTime = strftime("%H:%M:%S", localtime())
    currDate = strftime("%D", localtime())
    label_txt1.configure(text=upTemp+"°") #Update the data to the label_txt1.
    label_txt2.configure(text=upHum+"%") #Update the data to the label_txt2.
    with open('dataFile.csv', mode='a', newline="", encoding="UTF8") as dataFile: #Here it create a csv file or updates an existing file with the same name.
        writeData = csv.writer(dataFile)
        writeData.writerow([upTemp,upHum,currTime,currDate])#Start writing the rows with the data.
    threading.Timer(interval=2, function = updateData, args=None).start()
    
    '''
    So, this is how we made the program have the values of temperature and humidity to continue updating. Using the library threading.
    When start() is called, it starts a new thread that will run independently of the main thread of execution.
    This new thread will waits for 2 secons and then execute the updateData() function.
    Meanwhile, the main thread continues to have the window open.
    '''
    app.update() #This updates the interface and shows the changes made before.

def on_closing(): #This function creates a messagebox when triying to close the window.
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        app.destroy()

#Window is created
app = ctk.CTk()
app.geometry("600x300")
app.title("Data structures project")
app.resizable(False,False) #This makes the window not resizable.

#Create a frame for temperature display
frame1 = ctk.CTkFrame(app, width=400, height=200)
frame1.pack(side=ctk.LEFT, padx=20, pady=20, fill=ctk.BOTH, expand=True)

#Create a label for temperature text
label1 = ctk.CTkLabel(frame1, text="Temperature", font=("Helvetica", 18))
label1.pack(padx=20, pady=10)

#Create a label for temperature readings
label_txt1 = ctk.CTkLabel(frame1, font=("Helvetica", 20))
label_txt1.pack(padx=20, pady=10)

#Create a frame for humidity display
frame2 = ctk.CTkFrame(app, width=400, height=200)
frame2.pack(side=ctk.RIGHT, padx=20, pady=20, fill=ctk.BOTH, expand=True)

#Create a label for humidity text
label2 = ctk.CTkLabel(frame2, text="Humidity", font=("Helvetica", 18))
label2.pack(padx=20, pady=10)

#Create a label for humidity readings
label_txt2 = ctk.CTkLabel(frame2, font=("Helvetica", 20))
label_txt2.pack(padx=20, pady=10)

#Create an image object
image1 = ctk.CTkImage(light_image = Image.open("Temp2.png"), size=(180, 170))
label2 = ctk.CTkLabel(frame1, image=image1, text="")
label2.pack(padx=20, pady=20)

#Create an image object
image2 = ctk.CTkImage(light_image = Image.open("Humid.png"), size=(170, 155))
label_image2 = ctk.CTkLabel(frame2, image=image2, text="")
label_image2.pack(padx=20, pady=20)

updateData()#After the interface is loaded, we call the updateData function, which will continue to update the interface until we close the program.
app.protocol("WM_DELETE_WINDOW", on_closing) #Calls function to ask of the user wants to exit the program
app.mainloop()
arduino.close() #Close the conection with arduino, its out of the main loop because we are pretty much never using it.