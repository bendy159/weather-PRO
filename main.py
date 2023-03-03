import tkinter
from tkinter import *
from tkinter import messagebox
import customtkinter
import os
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from pyowm.weatherapi25 import observation
from PIL import Image

n = 0
windbreaker = 0
coat_jacket = 0
suit_jacket_west = 0
shirt = 0
turtkeneck = 0
tshirt_sweatshirt = 0
trousers_jeans = 0
sweetpants_shorts = 0
thermal_underwear = 0
skirt_dress = 0
warm_jacket = 0
middle = 0
below = 0
up = 0
wear_windbreaker = 0
wear_coat_jacket = 0
wear_suit_jacket_west = 0
wear_shirt = 0
wear_turtkeneck = 0
wear_tshirt_sweatshirt = 0
wear_trousers_jeans = 0
wear_sweetpants_shorts = 0
wear_thermal_underwear = 0
wear_skirt_dress = 0
wear_warm_jacket = 0
wears = []
wears_fin = []


window=Tk()
window.title('Weather PRO')
window.geometry('360x640')

window.image = PhotoImage(file='firstBG.png')
bg_BG = Label(window, image=window.image)
bg_BG.grid(row=0, column=0)

def bg_change():
    window.destroy()



    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("360x640")
            self.minsize(360, 640)
            self.maxsize(360, 640)

            self.title("weather PRO")

            self.frame_1 = customtkinter.CTkFrame(self)
            self.frame_1.pack(pady=20, padx=10, fill="both")

            self.frame_2 = customtkinter.CTkFrame(self)
            self.frame_2.pack(pady=10, padx=60, fill="none")

            self.checkbox_1 = customtkinter.CTkCheckBox(master=self.frame_1, text="Windbreaker")
            self.checkbox_1.pack(pady=10, padx=0)
            self.checkbox_2 = customtkinter.CTkCheckBox(master=self.frame_1, text="Coat/Jacket")
            self.checkbox_2.pack(pady=10, padx=0)
            self.checkbox_3 = customtkinter.CTkCheckBox(master=self.frame_1, text="Suit jacket (vest)")
            self.checkbox_3.pack(pady=10, padx=0)
            self.checkbox_4 = customtkinter.CTkCheckBox(master=self.frame_1, text="Shirt")
            self.checkbox_4.pack(pady=10, padx=0)
            self.checkbox_5 = customtkinter.CTkCheckBox(master=self.frame_1, text="Turtkeneck")
            self.checkbox_5.pack(pady=10, padx=0)
            self.checkbox_6 = customtkinter.CTkCheckBox(master=self.frame_1, text="t-shirt/sweatshirt")
            self.checkbox_6.pack(pady=10, padx=0)
            self.checkbox_7 = customtkinter.CTkCheckBox(master=self.frame_1, text="trousers/jeans")
            self.checkbox_7.pack(pady=10, padx=0)
            self.checkbox_8 = customtkinter.CTkCheckBox(master=self.frame_1, text="sweatpants/shorts")
            self.checkbox_8.pack(pady=10, padx=0)
            self.checkbox_9 = customtkinter.CTkCheckBox(master=self.frame_1, text="thermal underwear")
            self.checkbox_9.pack(pady=10, padx=0)
            self.checkbox_10 = customtkinter.CTkCheckBox(master=self.frame_1, text="skirt/dress")
            self.checkbox_10.pack(pady=10, padx=0)
            self.checkbox_11 = customtkinter.CTkCheckBox(master=self.frame_1, text="warm jacket")
            self.checkbox_11.pack(pady=10, padx=0)

            self.button = customtkinter.CTkButton(master=self.frame_2, text="Confirm", command=self.button_event)
            self.button.pack(pady=10, padx=10)

        def button_event(self):
            if customtkinter.CTkCheckBox.get(self.checkbox_1) == 1:
                global windbreaker
                windbreaker = 1
            if customtkinter.CTkCheckBox.get(self.checkbox_2) == 1:
                global coat_jacket
                coat_jacket = 1
            if customtkinter.CTkCheckBox.get(self.checkbox_3) == 1:
                global  suit_jacket_west
                suit_jacket_west = 1
            if customtkinter.CTkCheckBox.get(self.checkbox_4) == 1:
                global  shirt
                shirt = 1
            if customtkinter.CTkCheckBox.get(self.checkbox_5) == 1:
                global turtkeneck
                turtkeneck = 1
            if customtkinter.CTkCheckBox.get(self.checkbox_6) == 1:
                global tshirt_sweatshirt
                tshirt_sweatshirt = 1
            if customtkinter.CTkCheckBox.get(self.checkbox_7) == 1:
                global trousers_jeans
                trousers_jeans = 1
            if customtkinter.CTkCheckBox.get(self.checkbox_8) == 1:
                global sweetpants_shorts
                sweetpants_shorts = 1
            if customtkinter.CTkCheckBox.get(self.checkbox_9) == 1:
                global thermal_underwear
                thermal_underwear = 1
            if customtkinter.CTkCheckBox.get(self.checkbox_10) == 1:
                global skirt_dress
                skirt_dress = 1
            if customtkinter.CTkCheckBox.get(self.checkbox_11) == 1:
                global warm_jacket
                warm_jacket = 1
            else:
                pass

            self.homepage()

        def homepage(self):
            self.frame_1.destroy()
            self.frame_2.destroy()
            self.geometry("360x640")
            self.minsize(360, 640)
            self.maxsize(360, 640)

            self.frame_1 = customtkinter.CTkFrame(self)
            self.frame_1.pack(pady=20, padx=10, fill="both")

            self.frame_2 = customtkinter.CTkFrame(self)
            self.frame_2.pack(pady=20, padx=10)

            self.entry = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Write your city")
            self.entry.pack(padx=10, pady=10, anchor=tkinter.CENTER)

            self.button = customtkinter.CTkButton(master=self.frame_2, text="Confirm", command=self.out)
            self.button.pack(padx=10, pady=10)


        def weather(self, arg):
            owm = OWM('b7ca9e58889c65158dfe9994fce5f839')
            mgr = owm.weather_manager()

            observation = mgr.weather_at_place(str(arg))
            w = observation.weather

            temp1 = w.temperature('celsius')
            global middle_temp
            middle_temp = temp1.get('temp')
            detail = w.detailed_status
            self.rain(detail)
            self.temp(middle_temp)

        def temp(self, arg_temp):
            if (10.0 < float(arg_temp) < 16.0) and (customtkinter.CTkCheckBox.get(self.checkbox_1) == 1 or
                                                    customtkinter.CTkCheckBox.get(self.checkbox_2) == 1 or
                                                    customtkinter.CTkCheckBox.get(self.checkbox_5) == 1 or
                                                    customtkinter.CTkCheckBox.get(self.checkbox_7) == 1):
                if customtkinter.CTkCheckBox.get(self.checkbox_1) == 1:
                    global wear_windbreaker
                    wear_windbreaker = 1
                if customtkinter.CTkCheckBox.get(self.checkbox_2):
                    global wear_coat_jacket
                    wear_coat_jacket = 1
                if customtkinter.CTkCheckBox.get(self.checkbox_5) == 1:
                    global wear_turtkeneck
                    wear_turtkeneck = 1
                if customtkinter.CTkCheckBox.get(self.checkbox_7) == 1:
                    global wear_trousers_jeans
                    wear_trousers_jeans = 1
                global middle
                middle = 1

            elif float(arg_temp) <= 10.0 and (customtkinter.CTkCheckBox.get(self.checkbox_11) == 1 or
                                             customtkinter.CTkCheckBox.get(self.checkbox_2) == 1 or
                                             customtkinter.CTkCheckBox.get(self.checkbox_9) == 1 or
                                             customtkinter.CTkCheckBox.get(self.checkbox_3) == 1 or
                                             customtkinter.CTkCheckBox.get(self.checkbox_7) == 1):
                if customtkinter.CTkCheckBox.get(self.checkbox_11) == 1:
                    global wear_warm_jacket
                    wear_warm_jacket = 1
                if customtkinter.CTkCheckBox.get(self.checkbox_2) == 1:
                    wear_coat_jacket = 1
                if customtkinter.CTkCheckBox.get(self.checkbox_9) == 1:
                    global wear_thermal_underwear
                    wear_thermal_underwear = 1
                if customtkinter.CTkCheckBox.get(self.checkbox_3) == 1:
                    wear_suit_jacket_west = 1
                if customtkinter.CTkCheckBox.get(self.checkbox_7) == 1:
                    wear_trousers_jeans = 1
                global below
                below = 1


            elif float(arg_temp) >= 16 and (customtkinter.CTkCheckBox.get(self.checkbox_10) == 1 or
                                            customtkinter.CTkCheckBox.get(self.checkbox_4) == 1 or
                                            customtkinter.CTkCheckBox.get(self.checkbox_6) == 1 or
                                            customtkinter.CTkCheckBox.get(self.checkbox_8) == 1):

                if customtkinter.CTkCheckBox.get(self.checkbox_10) == 1:
                    global wear_skirt_dress
                    wear_skirt_dress = 1
                if customtkinter.CTkCheckBox.get(self.checkbox_4) == 1:
                    global wear_shirt
                    wear_shirt = 1
                if customtkinter.CTkCheckBox.get(self.checkbox_6) == 1:
                    global wear_tshirt_sweatshirt
                    wear_tshirt_sweatshirt = 1
                if customtkinter.CTkCheckBox.get(self.checkbox_8) == 1:
                    global wear_sweetpants_shorts
                    wear_sweetpants_shorts = 1
                global up
                up = 1

        def rain(self, arg):
            if ('rain' in arg) and (customtkinter.CTkCheckBox.get(self.checkbox_1) == 1):
                if customtkinter.CTkCheckBox.get(self.checkbox_1) == 1:
                    wears.append("Windbreaker")

        def vychislit(self):
            if middle == 1:
                if wear_windbreaker == 1:
                    wears.append("Windbreaker")
                if wear_coat_jacket == 1:
                    wears.append("Coat/Jacket")
                if wear_turtkeneck == 1:
                    wears.append("Turtkeneck")
                if wear_trousers_jeans == 1:
                    wears.append("Trousers/Jeans")
            elif below == 1:
                if wear_warm_jacket == 1:
                    wears.append("Warm jacket")
                if wear_coat_jacket == 1:
                    wears.append("Coat/Jacket")
                if wear_thermal_underwear == 1:
                    wears.append("Thermal underwear")
                if wear_suit_jacket_west == 1:
                    wears.append("Suit jacket(west)")
                if wear_trousers_jeans == 1:
                    wears.append("Trousers/Jeans")
            elif up == 1:
                if wear_skirt_dress == 1:
                    wears.append("Skirt/Dress")
                if wear_shirt == 1:
                    wears.append("Shirt")
                if wear_tshirt_sweatshirt == 1:
                    wears.append("T-shirt/Sweatshirt")
                if wear_sweetpants_shorts == 1:
                    wears.append("Sweetpans/Shorts")



        def out(self):
            city = customtkinter.CTkEntry.get(self.entry)
            self.frame_1.destroy()
            self.frame_2.destroy()
            self.weather(city)
            self.vychislit()
            if len(wears) == 0:
                text = "Don't go outside"
            else:
                for i in wears:
                    global n
                    n+=1
                    wears_fin.append(str(n)+')'+i)
                text = "\n".join(wears_fin)
            self.geometry("360x640")
            self.minsize(360, 640)
            self.maxsize(360, 640)
            self.font = customtkinter.CTkFont(size=20)
            self.font_t = customtkinter.CTkFont(size=30)
            self.screen = customtkinter.CTkImage(dark_image=Image.open("Outwindow.jpg"), size=(360, 640))
            self.screen_label = customtkinter.CTkLabel(master=self, text="", image=self.screen)
            self.screen_label.grid(row=0, column=0)
            self.city_label = customtkinter.CTkLabel(master=self, text=city, fg_color='#e2ffeb',
                                                     font=self.font).place(x=150, y=15)
            self.temp_label = customtkinter.CTkLabel(master=self, text=str(middle_temp)+'°C', fg_color='white',
                                                     font=self.font_t).place(x=135, y=140)
            self.wear_label = customtkinter.CTkLabel(master=self, text=text, fg_color='#deeefe', font=self.font).place(x=95, y=350)

    app = App()
    app.mainloop()


btn1 = PhotoImage(file='Button1.png')
Button(window, image=btn1, highlightthickness=0, bd=0, command=bg_change).place(x=85,y=210)
id_button1 = Button(window, image=btn1, highlightthickness=0, bd=0)


window.mainloop()
