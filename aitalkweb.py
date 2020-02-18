#from voice2 import talkVOICEROID2
from voiceroid2_1 import talkVOICEROID2_1
from voiceroid2_2 import talkVOICEROID2_2
from voiceroid2_3 import talkVOICEROID2_3
from voiceroid2_4 import talkVOICEROID2_4
import time


#文章の処理行う




def addlist(text):
    mysay="you: "+ text
    print(mysay)
    listbox.insert(tkinter.END,mysay)
    chat = "Aoi: " + talk(text)

    #if 0<=int(text):
    #    aoivoice=int(text)

    Entry1.delete(0, tkinter.END)
    chatCut(chat)
    #addRep(aoi)

def chatCut(chat):    
    aoi=chat
    addRep(aoi)

def addRep(aoi):
    listbox.insert(tkinter.END, aoi)
    #ボイス処理
    voiceroid=aoi[5:]
    voiceroid=voiceroid+"っ"
    word=len(voiceroid)
    destime=round(word/7+0.1,1)
    #destime=round(word/7+1.1,1)
    #デスクトップ上で喋らせない場合以下のコメントアウトを付ける
    #talkVOICEROID2(voiceroid)
    #time.sleep(destime)
    #print(destime)
    #-----------zzz
    talkVOICEROID2_1(voiceroid)
    time.sleep(0.3)
    talkVOICEROID2_2(voiceroid)
    time.sleep(0.2)
    talkVOICEROID2_3(voiceroid)
    time.sleep(0.2)
    talkVOICEROID2_4(voiceroid)
