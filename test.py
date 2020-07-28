import wave
#import pyaudio
import winsound as ws
import tkinter
import sys
import time
import tkinter.messagebox as tkm
from tkinter import ttk
from voice2 import talkVOICEROID2
from voiceroid2_1 import talkVOICEROID2_1
from voiceroid2_2 import talkVOICEROID2_2
from voiceroid2_3 import talkVOICEROID2_3
from voiceroid2_4 import talkVOICEROID2_4


#global setnumber
setnumber = 0

root=tkinter.Tk()
root.geometry("1920x1080")
root.title(u"aoi talk")
kotonoha=tkinter.PhotoImage(file="C:/Users/takumi/Desktop/kototalk/aoi09.png")
canvas=tkinter.Canvas(bg="white",width=475,height=750)
canvas.place(x=1300,y=250)
canvas.create_image(0,0, image=kotonoha, anchor=tkinter.NW)

#キャラの確認をする
def change():
    comboExample['calues'] = []

#文章の処理行う

def addlist(text, voiceroid):
    # print(voiceroid)
    mysay="you: "+ text
    # print(mysay)
    listbox.insert(tkinter.END,mysay)
    chat = voiceroid + ": " + talk(text)
    voice = voiceroid + "＞" + talk(text)
    # chat = "Aoi: " + talk(text)
    #if 0<=int(text):
    #    aoivoice=int(text)
    Entry1.delete(0, tkinter.END)
    addRep(chat, voice)
    #addRep(aoi)

# def chatCut(aoi):
#     # aoi=chat
#     addRep(chat)

def addRep(chat, voice):
    listbox.insert(tkinter.END, chat)
    global setnumber
    setnumber+=1
    #ボイス処理
    # voiceroid=aoi[5:]
    voiceroid = voice + "っ"
    word=len(voiceroid)
    destime=round(word/7+0.1,1)
    #destime=round(word/7+1.1,1)
    #デスクトップ上で喋らせない場合以下のコメントアウトを付ける
    talkVOICEROID2(voiceroid)
    time.sleep(destime)
    print(destime)
    #-----------zzz  
    talkVOICEROID2_1(voiceroid)
    time.sleep(0.3)
    talkVOICEROID2_2(voiceroid,setnumber)
    time.sleep(0.2)
    talkVOICEROID2_3(voiceroid)
    time.sleep(0.2)
    talkVOICEROID2_4(voiceroid)

def talk(say):
    if say == 'end':
        return ('ではまた')
    else:
        return (say)

static=tkinter.Label(text=u"葵ちゃんに話しかけてね！")
static.pack()

comboExample = ttk.Combobox(root, 
                            values=["-",
                            "紲星あかり", "結月ゆかり", "琴葉 葵", "琴葉 茜",
                            ],

                            postcommand=change)
comboExample.pack()
# comboExample.grid(column=0, row=1)

Entry1=tkinter.Entry(width=50)
Entry1.insert(tkinter.END,u"こんにちは")
Entry1.pack()

button=tkinter.Button(text=u"送信", width=50,command=lambda: addlist(Entry1.get(),comboExample.get()))
# button=tkinter.Button(text=u"送信", width=50,command=lambda: addlist(Entry1.get(),comboExample.get()))
button.pack()

listbox=tkinter.Listbox(width=55,height=15)
listbox.pack()

root.mainloop()