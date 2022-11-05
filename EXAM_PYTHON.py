from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("600x600")
firstname=StringVar()
lastname=StringVar()
gender=IntVar()
email=StringVar()
address=StringVar()
state=StringVar()
zip=IntVar()
creditc=StringVar()

Chekcbutton1=IntVar()
Chekcbutton2=IntVar()
Chekcbutton3=IntVar()
btnt=Checkbutton(root,text="TELEGU",variable=Chekcbutton1,onvalue=1,offvalue=0,height=2,width=10).grid(row=3,column=1)
btne=Checkbutton(root,text="ENGLISH",variable=Chekcbutton2,onvalue=1,offvalue=0,height=2,width=10).grid(row=3,column=2)
btnh=Checkbutton(root,text="HINDI",variable=Chekcbutton1,onvalue=1,offvalue=0,height=2,width=10).grid(row=3,column=3)
l=Label(root,text="")
def printselection():
    l.config(text=" you have selected"+gender.get())

r1=Radiobutton (root,text="male",variable=gender, command=printselection).grid(row=2,column=1)
r2=Radiobutton (root,text="female",variable=gender, command=printselection).grid(row=2,column=2)


name_entry=Entry(root,textvariable=firstname,font=('arial',10,'bold')).grid(row=0,column=1)
lastn_entry=Entry(root,textvariable=lastname,font=('arial',10,'bold')).grid(row=1,column=1)
email_entry=Entry(root,textvariable=email,font=('arial',10,'bold')).grid(row=4,column=1)
address_entry=Entry(root,textvariable=address,font=('arial',10,'bold')).grid(row=5,column=1)
state_entry=Entry(root,textvariable=state,font=('arial',10,'bold')).grid(row=6,column=1)
zip_entry=Entry(root,textvariable=zip,font=('arial',10,'bold')).grid(row=7,column=1)
credit_entry=Entry(root,textvariable=creditc,font=('arial',10,'bold')).grid(row=8,column=1)

le=Label(root,text="message boxes",font=50).grid(row=5,column=8)

l1=Label(root,text="First name",font=('arial',10,'bold')).grid(row=0,column=0)
l2=Label(root,text="Last Name",font=('arial',10,'bold')).grid(row=1,column=0)
l3=Label(root,text="Gender",font=('arial',10,'bold')).grid(row=2,column=0)
l4=Label(root,text="Languages ",font=('arial',10,'bold')).grid(row=3,column=0)
l5=Label(root,text="Email ",font=('arial',10,'bold')).grid(row=4,column=0)
l6=Label(root,text="address",font=('arial',10,'bold')).grid(row=5,column=0)
l7=Label(root,text="State",font=('arial',10,'bold')).grid(row=6,column=0)
l8=Label(root,text="zip ",font=('arial',10,'bold')).grid(row=7,column=0)
l9=Label(root,text="credit card type ",font=('arial',10,'bold')).grid(row=8,column=0)



def insert():
    print("BILLING RECORDS")
    fname=firstname.get()
    lastn=lastname.get()
    gender=gender.get()
    email=StringVar()
    add=address.get()
    st=state.get()
    zp=zip.get()
    credit=creditc.get()
    
    print("Name is : "+fname+lastn)
    print("gender is : "+gender)
    print(" email is :"+email)
    print("address is : "+add)
    print(" zip code is :"+zp)
    print("State is :"+st)
    print("credit card type is :"+credit)

    messagebox.showinfo("showinfo","information")
sub_btn=Button(root,text="insert",command=insert,activeforeground = "blue" ,activebackground ="pink",pady=10).grid(row=2,column=4) 

def delete():
    print("BILLING RECORDS")
    fname=firstname.set("")
    lastn=lastname.set("")
    genderr=gender.set("")
    
    add=address.set("")
    st=state.set("")
    zp=zip.set("")
    credit=creditc.set("")
    print("Name is : "+fname+lastn)
    print("gender is : "+genderr)
    print(" email is :"+email)
    print("address is : "+add)
    print(" zip code is :"+zp)
    print("State is :"+st)
    print("credit card type is :"+credit)
    
    messagebox.showwarning("showwarning","warning")
sub_btn2=Button(root,text="delete",command=delete,activeforeground = "blue" ,activebackground ="pink",pady=10).grid(row=4,column=4)  


 

def theme():
    print("")

sub_btn3=Button(root,text="theme",command=theme,activeforeground = "blue" ,activebackground ="pink",pady=10).grid(row=6,column=4)  
























root.mainloop()