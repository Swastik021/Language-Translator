from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from idlelib.tooltip import Hovertip
from googletrans import Translator
import pyperclip as pc
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile

root = Tk()
root.title("Translator")
root.geometry("1090x400")
root.config(bg='#20325B')

def open_file():
    file = askopenfile(mode ='r', filetypes =[('Text File', '*.txt'),("All Files", "*.*")])
    content = file.read()
    inputBox.insert(1.0,content)

def openfile(e):
    filename = askopenfile(mode ='r', filetypes =[('Text File', '*.txt'),("All Files", "*.*")])
    contents = filename.read()
    inputBox.insert(1.0,contents)
    
def translate():
    det_lang = inputBox.get("1.0","end")
    cl =ch_language.get()
    resultBox.config(state = NORMAL)

    if det_lang == '':
        messagebox.showerror("Missing","Please enter any text")
    else:
        resultBox.delete(1.0,'end')
        trans = Translator()
        output=trans.translate(det_lang, dest = cl)
        resultBox.insert('end',output.text)
        resultBox.config(state = DISABLED)
def copytext():
    resulttext = resultBox.get("1.0","end")
    pc.copy(resulttext)
    messagebox.showinfo("Successful","Text copied in clipboard! ")
    
def clear():
    resultBox.config(state = NORMAL)
    inputBox.delete(1.0,'end')
    resultBox.delete(1.0,'end')
    resultBox.config(state = DISABLED)

a=StringVar()
lang=ttk.Combobox(root,textvariable = a, width=25, font=('Times New Roman',14,'bold'))
lang['values']=('Auto Detect',)
lang.place(x=10,y=85)
lang.current(0)

b=StringVar()
ch_language=ttk.Combobox(root,textvariable = b,width=25,font=('Times New Roman',14,'bold'))
ch_language['values']=('Afrikaans','Albanian','Amharic','Arabic','Armenian','Azerbaijani',
                       'Basque','Belarusian','Bengali','Bosnian','Bulgarian','Catalan',
                       'Cebuano','Chichewa','Chinese (simplified)','Chinese (traditional)',
                       'Corsican','Croatian','Czech','Danish','Dutch','English','Esperanto',
                       'Estonian','Filipino','Finnish','French','Frisian','Galician','Georgian',
                       'German','Greek','Gujarati','Haitian creole','Hausa','Hawaiian','Hebrew',
                       'Hebrew','Hindi','Hmong','Hungarian','Icelandic','Igbo','Indonesian',
                       'Irish','Italian','Japanese','Javanese','Kannada','Kazakh','Khmer',
                       'Korean','Kurdish (kurmanji)','Kyrgyz','Lao','Latin','Latvian','Lithuanian',
                       'Luxembourgish','Macedonian','Malagasy','Malay','Malayalam','Maltese',
                       'Maori','Marathi','Mongolian','Myanmar (burmese)','Nepali','Norwegian',
                       'Odia','Pashto','Persian','Polish','Portuguese','Punjabi','Romanian',
                       'Russian','Samoan','Scots Gaelic','Serbian','Sesotho','Shona','Sindhi',
                       'Sinhala','Slovak','Slovenian','Somali','Spanish','Sundanese','Swahili',
                       'Swedish','Tajik','Tamil','Telugu','Thai','Turkish','Ukrainian','Urdu',
                       'Uyghur','Uzbek','Vietnamese','Welsh','Xhosa','Yiddish','Yoruba','Zulu')

ch_language.place(x=600,y=85)
ch_language.current(0)

i1mg = Image.open('Translator1.png')
i1mg = i1mg.resize((70, 70), Image.LANCZOS)
i1mg = ImageTk.PhotoImage(i1mg)

logo = Label(root, image= i1mg,bd=0)
logo.image=i1mg
logo.place(x = 330, y = 4)

titleLabel = Label(root,text = "Language Translator",font=('Times New Roman',35,'bold'),fg="cornflowerblue" ,bg='#20325B')
titleLabel.place(x=395, y=10)

inputBox=Text(root,width=68,height=15,font=('Ariel',10,'bold'))
inputBox.place(x=10,y=120)

resultBox=Text(root,width=68,height=15,font=('Ariel',10,'bold'))
resultBox.place(x=600,y=120)

clearBtn=Button(root,text="Clear",width=10,font=('Ariel',10,'bold'),bd = 5,command = clear)
clearBtn.place(x=500,y=320)

translateBtn=Button(root,text="Translate",width=10,font=('Ariel',10,'bold'),bd = 5,command = translate,fg='blue')
translateBtn.place(x=500,y=220)

copyBtn=Button(root,text="Copy",width=10,cursor= "hand2",font=('Ariel',10,'bold'),bd = 5,command = copytext,bg='yellow',fg='blue')
copyBtn.place(x=890,y=80)

openfileBtn=Button(root,text="Open File ",width=10,cursor= "hand2",font=('Ariel',10,'bold'),bd = 5,command = open_file,fg='blue',bg='Yellow')
openfileBtn.place(x=300,y=80)
mytip = Hovertip(openfileBtn,'Ctrl + O')

root.bind('<Control-o>', openfile)
mainloop()
