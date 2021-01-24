from tkinter import *
from speedtest import Speedtest

def check_speed():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download/(10**6),2)
    upload_speed = round(upload/(10**6),2)
    down_label.config(text="Download Speed - "+ str(download_speed)+" Mbps")
    up_label.config(text="Upload Speed - "+ str(upload_speed)+" Mbps")

#check_speed()

root = Tk()
root.title("INTERNET SPEEDTEST")
root.geometry('300x400')
root.config(bg='black')
root.resizable(False,False)

canvas = Canvas(root, width = 300, height = 400,bg="black")      
canvas.pack()      
img = PhotoImage(file="pic.png")      
canvas.create_image(0,0,anchor=NW, image=img)

Button = Button(root,text="GET SPEED",width=10,command=check_speed)
Button.place(x=110,y=345)
down_label = Label(root,text="",width=25)
down_label.place(x=60,y=275)
up_label = Label(root,text="",width=25)
up_label.place(x=60,y=307)

root.mainloop()