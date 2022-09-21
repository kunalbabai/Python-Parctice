#importing the liabery
from email.mime import image
from re import X
import tkinter as tk
from PIL import Image, ImageTk
from pygame import mixer
mixer.init()
class music_palyer():
    try:
        def __init__(self):
            self.root = tk.Tk()
            self.root.title("Kunal_Music_Player_2022")
            self.root.geometry("1920x1080")
            self.root.configure(background='white')
             #adding label/ Text
            self.label = tk.Label(self.root,text="Welcome To Coder Music Player -",bg="Yellow",fg="black",font=22).place(x=50,y=20)
            #label accoring to the button operation
            self.label1 = tk.Label(self.root,text="Hey Coder! Lets Code & Play -----")
            self.label1.pack(side=tk.BOTTOM,fill=tk.X)
            #adding the function for button operation
            #golab pause variable craetion
            def play_song():
                # try:
                #     pause_music
                # except NameError:
                #     try:
                #         mixer.music.load(r"C:\Users\UDCIND\OneDrive - UDC\Smaple_Program_ML\Ring_Tone_Alarm\Husan - Ap Dhillon.mp3")
                #         mixer.music.play()
                #         self.label1['text']="Music Playing.........."
                #     except Exception as Ex:
                #         return Ex
                # else:
                #     mixer.music.unpause()
                try:
                    mixer.display.set_mode((200,100))
                    mixer.music.load(r'C:\Users\UDCIND\Downloads\Husan - Ap Dhillon.mp3')
                    mixer.music.play()
                    self.label1['text']="Music Playing.........."
                    while True:
                        pass
                except Exception as Ex:
                    return Ex
            def pause_song():
                try:
                    global pause_music
                    mixer.music.pause()
                    pause_music = True
                except Exception as Ex:
                    return Ex
            def stop_song():
                try:
                    mixer.music.stop()
                    self.label1['text']="Music Stop!!!!!"
                except Exception as Ex:
                    return Ex
            #adding phothos in the Tkinter
            self.image = ImageTk.PhotoImage(file = r'C:\Users\UDCIND\OneDrive - UDC\Smaple_Program_ML\maxresdefault.jpg')
            image = tk.Label(self.root,image=self.image,bg='white').place(x=50,y=92)
            #adding another image
            self.image2 = ImageTk.PhotoImage(file=r'C:\Users\UDCIND\OneDrive - UDC\Smaple_Program_ML\clef-1439137_1280.jpg')
            image1 = tk.Label(self.root,image=self.image2,height=250,width=979).place(x=438,y=75)
            #button adding 
            self.b1 = ImageTk.PhotoImage(file=r'C:\Users\UDCIND\OneDrive - UDC\Smaple_Program_ML\button\video.png')
            self.b2 = ImageTk.PhotoImage(file=r'C:\Users\UDCIND\OneDrive - UDC\Smaple_Program_ML\button\pause-button.png')
            self.b3 = ImageTk.PhotoImage(file=r'C:\Users\UDCIND\OneDrive - UDC\Smaple_Program_ML\button\stop-button.jpg')
            button_play = tk.Button(self.root,image=self.b1,height=65,width=67,bd=0,command=play_song).place(x=650,y=550)
            button_pause = tk.Button(self.root,image=self.b2,height=60,width=60,bd=0,command=pause_song).place(x=750,y=550)
            button_stop = tk.Button(self.root,image=self.b3,height=55,width=55,bd=0,command=stop_song).place(x=850,y=550)
    except Exception as Ex:
        print(Ex)
music = music_palyer()
music.root.mainloop()
