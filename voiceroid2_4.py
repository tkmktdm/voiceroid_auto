#4回目
# -*- coding: utf-8 -*-
import pywinauto

def search_child_byclassname_4(class_name, uiaElementInfo, target_all = False):
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

def search_child_byname_4(name, uiaElementInfo):
    # 全ての子要素検索
    for childElement in uiaElementInfo.children():
        # Nameの一致確認
        if childElement.name == name:
            return childElement
    # 無かったらFalse
    return False

def talkVOICEROID2_4(speakPhrase):
    # デスクトップのエレメント
    parentUIAElement = pywinauto.uia_element_info.UIAElementInfo()
    # voiceroidを捜索する
    voiceroid2 = search_child_byname_4("VOICEROID2",parentUIAElement)
    # *がついている場合
    if voiceroid2 == False:
        voiceroid2 = search_child_byname_4("VOICEROID2*",parentUIAElement)

    #ここから変更
    # 音声保存ウィンドウ (保存確認) 要素のElementInfoを取得
    wavEle = search_child_byclassname_4("Window",voiceroid2)
    # 情報ダイアログ 要素のElementInfoを取得
    infoEle = search_child_byclassname_4("#32770",wavEle)
    
    # YES　ボタン取得
    yessEle = search_child_byclassname_4("Button",infoEle,target_all = True)
    # はいボタンを探す
    playyesEle = ""
    for yesEle in yessEle:
        # テキストブロックを捜索

        w=search_child_byclassname_4("#32770",wavEle)
        if yesEle.name=="OK":
            playyesEle=yesEle
            break

    # ボタンコントロール取得
    playButtonControl = pywinauto.controls.uia_controls.ButtonWrapper(playyesEle)

    # 再生ボタン押下
    playButtonControl.click()