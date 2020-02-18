#2回目
# -*- coding: utf-8 -*-
import pywinauto

def search_child_byclassname_2(class_name, uiaElementInfo, target_all = False):
    target = []
    # 全ての子要素検索
    for childElement in uiaElementInfo.children():
        # ClassNameの一致確認

        if childElement.class_name == class_name:
            if target_all == False:
                return childElement
            else:
                target.append(childElement)
    if target_all == False:
        # 無かったらFalse
        return False
    else:
        return target

def search_child_byname_2(name, uiaElementInfo):
    # 全ての子要素検索
    for childElement in uiaElementInfo.children():
        # Nameの一致確認
        if childElement.name == name:
            return childElement
    # 無かったらFalse
    return False

def talkVOICEROID2_2(speakPhrase,num):

    #setnumber="sample" + str(num) + ".wav"
    setnumber=str(num) + ".wav"
    print(setnumber)
    # デスクトップのエレメント
    parentUIAElement = pywinauto.uia_element_info.UIAElementInfo()
    # voiceroidを捜索する
    voiceroid2 = search_child_byname_2("VOICEROID2",parentUIAElement)
    # *がついている場合
    if voiceroid2 == False:
        voiceroid2 = search_child_byname_2("VOICEROID2*",parentUIAElement)

    #ここから変更
    # 名前を付けて保存　要素のElementInfoを取得
    saveEle = search_child_byclassname_2("#32770",voiceroid2)
 
    #名前編集
    win = search_child_byclassname_2("DUIViewWndClassName",saveEle)

    winwin = search_child_byclassname_2("AppControlHost",win)

    filewin = search_child_byclassname_2("Edit",winwin)

    #print(filewin)

    textBoxEditControl = pywinauto.controls.uia_controls.EditWrapper(filewin)
    textBoxEditControl.set_edit_text(setnumber)
    


    playsaveEle = search_child_byclassname_2("Button",saveEle,target_all = False)

    # ボタンコントロール取得
    playButtonControl = pywinauto.controls.uia_controls.ButtonWrapper(playsaveEle)

    # 再生ボタン押下
    playButtonControl.click()