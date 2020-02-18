#3回目
# -*- coding: utf-8 -*-
import pywinauto

def search_child_byclassname_3(class_name, uiaElementInfo, target_all = False):
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

def search_child_byname_3(name, uiaElementInfo):
    # 全ての子要素検索
    for childElement in uiaElementInfo.children():
        # Nameの一致確認
        if childElement.name == name:
            return childElement
    # 無かったらFalse
    return False

def talkVOICEROID2_3(speakPhrase):
    # デスクトップのエレメント
    parentUIAElement = pywinauto.uia_element_info.UIAElementInfo()
    # voiceroidを捜索する
    voiceroid2 = search_child_byname_3("VOICEROID2",parentUIAElement)
    # *がついている場合
    if voiceroid2 == False:
        voiceroid2 = search_child_byname_3("VOICEROID2*",parentUIAElement)

    #ここから変更
    # 1つ目の名前を付けて保存 要素のElementInfoを取得
    saveEle = search_child_byclassname_3("#32770",voiceroid2)
    
    #2つ目の名前を付けて保存 (はい or いいえ) 要素のElementInfoを取得
    resaveEle = search_child_byclassname_3("#32770",saveEle)
    
    # 2つ目の中のハンドル内を格納する (YES ボタン取得)
    yessEle = search_child_byclassname_3("Button",resaveEle,target_all = True)
    # はいボタンを探す
    playyesEle = ""
    for yesEle in yessEle:
        # 1つ目の引数に今いるハンドル、2つ目の引数に前の保存ハンドル
        # 今いるところの中にあるnameはいを探す
        a=search_child_byclassname_3("#32770",saveEle)
        if yesEle.name=="はい(Y)":
            playyesEle=yesEle
            break

    # ボタンコントロール取得
    playButtonControl = pywinauto.controls.uia_controls.ButtonWrapper(playyesEle)

    # 再生ボタン押下
    playButtonControl.click()