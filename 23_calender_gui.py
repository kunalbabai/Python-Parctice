import calendar
from tkinter import *

#function to show the calender for given year
def showCalender():
    try:
        #creating the object
        calender_gui = Tk()
        #for the text filled data
        year = int(year_field.get())
        calender_gui.config(background="")
        calender_gui.title(f"Calender For The Year - {year}")
        calender_gui.geometry("550x550")
        gui_content = calendar.calendar(year)
        calYear = Label(calender_gui,text=gui_content,font="Consolas 10 bold")
        calYear.grid(row=5,column=1,padx=20)

    except Exception as Ex:
        return Ex
def close():
   win = Tk()

   win.quit()
if __name__ == '__main__':
    try:
        new = Tk()
        new.config(background='grey')
        new.title("Calender")
        new.geometry("250x140")
        cal = Label(new,text="Calender",bg="RED",font=('times',28,'bold'))
        year = Label(new,text="Enter Year Here -", bg='dark grey')
        #input box
        year_field = Entry(new)
        button = Button(new,text=f"Show Calender {year_field}",fg='Black',bg='Yellow', command=showCalender)
        Exit = Button(new,text='Exit',fg='Black',bg='Yellow', command= close)
        #putting widgets in postion
        cal.grid(row=1,column=1)
        year.grid(row=2,column=1)
        year_field.grid(row=3,column=1)
        button.grid(row=4,column=1)
        Exit.grid(row=6,column=1)
        new.mainloop()
    except Exception as Ex:
        print(Ex)

