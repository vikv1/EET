from re import X
from types import LambdaType
from googletrans import Translator
import tkinter as tk
import threading


from tkinter import *
 
root = Tk()
root.geometry("500x500")
root.title("Easy English Translator")


language_list = [
  "English",
  "Español",
  "French",
  "Deutsch",
  "Chinese (Simplified)",
  "Chinese (Traditional)",
  "Hindi",
  "Arabic",
  "Russian",
  "Bengali",
  "Portuguese",
  "Telugu",
  "Finnish",
  "Hungarian",
  "Italian",
  "Japanese",
  "Korean",
  "Norwegian",
  "Romanian",
  "Slovenian",
  "Urdu",
  "Latin",
  "Swahili",
  "Thai",
  "Ukrainian",
  "Vietnamese",
  "Yiddish",
  "Danish",
  "Belarusian",
  "Afrikaans",
  "Catalan",
  "Filipino"
]

language_list.sort()

variable = StringVar(root)
variable.set(language_list[0]) # default value


def Translate(event = None):
    Output.delete(1.0, END)
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    translator = Translator()
    selected_lang = variable.get() # selected_lang is the language user has chosen in drop down
    input = translator.detect(INPUT)
    input_lang = input.lang
    print(input_lang)

    if(selected_lang == "Chinese (Simplified)"):
      translation = translator.translate(INPUT, dest = "zh-CN")
    elif(selected_lang == "Chinese (Traditional)"):
      translation = translator.translate(INPUT, dest = "zh-TW")
    elif(selected_lang == "Portuguese"):
      translation = translator.translate(INPUT, dest = "pt")
    elif(selected_lang == "Filipino"):
      translation = translator.translate(INPUT, dest = "tl")
    else:
      translation = translator.translate(INPUT, src = input_lang, dest = selected_lang[:2])
    
    Output.insert(END, translation.text + '\n')
    Output.insert(END, "Pronounciation: " + translation.pronunciation)
    

    print(translation.text)
     

root.bind('<Return>', Translate)


l = Label(text = "Enter your phrase below, then choose the desired target language.")

inputtxt = Text(root, height = 10,
                width = 25,
                bg = "light cyan",
                font = ('Helvatical bold', 20))
 
Output = Text(root, height = 10,
              width = 25,
              bg = "light yellow",
              font = ('Helvatical bold', 20))
 
Display = Button(root, height = 2,
                 width = 20,
                 text = "Translate",
                 command = lambda:Translate
                ())

LangSelect = OptionMenu(root, variable, *language_list)

Credit = Label(text = "By Vikrant Verma")



l.pack()
inputtxt.pack()
LangSelect.pack()
Display.pack()
Output.pack()
Credit.pack(side = tk.BOTTOM)

mainloop()
