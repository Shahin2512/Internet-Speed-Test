from tkinter import *
import speedtest

def speedcheck():
    sp_test = speedtest.Speedtest()
    sp_test.get_servers()
    down = str(round(sp_test.download() / (10**6),3)) + " Mbps "
    up = str(round(sp_test.upload() / (10**6),3)) + " Mbps "
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title(" Internet Speed Test ")
sp.geometry("500x600")
sp.config(bg="Black")


lab = Label(sp, text=" Internet Speed Test ", font=(" Times New Roman ", 20 , "bold"), bg="Black", fg="White")
lab.place(x=60, y=40, height=50 , width=380)

lab_down = Label(sp, text=" 00 ", font=(" Times New Roman ", 20 , "bold"), bg="White", fg="Black")
lab_down.place(x=60, y=130 , height=50 , width=380)

lab = Label(sp, text=" Download Speed ", font=(" Times New Roman ", 17 , "bold"), bg="Grey", fg="White")
lab.place(x=60, y=200 , height=50 , width=380)

lab_up = Label(sp, text=" 00 ", font=(" Times New Roman ", 20 , "bold"), bg="White", fg="Black")
lab_up.place(x=60, y=290 , height=50 , width=380)

lab = Label(sp, text=" Upload Speed ", font=(" Times New Roman ", 17 , "bold"), bg="Grey", fg="White")
lab.place(x=60, y=360 , height=50 , width=380)



button = Button(sp, text=" Check Speed ", font=(" Times New Roman ", 20 , "bold"), bg="White", fg="Black" , relief=RAISED , command=speedcheck)
button.place(x=60, y=500 , height=50 , width=380)
sp.mainloop()