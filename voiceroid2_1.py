# -*- coding: utf-8 -*-
import pywinauto

def search_child_byclassname_1(class_name, uiaElementInfo, target_all = False):
    target = []
    # 全ての子要素検索
    for childElement in uiaElementInfo.children():


        #一覧確認－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
        #print(childElement)
        #print(' 3 \n')

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

def search_child_byname_1(name, uiaElementInfo):
    # 全ての子要素検索
    for childElement in uiaElementInfo.children():

        #一覧確認－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
        #print(childElement)
        #print(' 2 \n')


        # Nameの一致確認
        if childElement.name == name:
            return childElement
    # 無かったらFalse
    return False

def talkVOICEROID2_1(speakPhrase):
    # デスクトップのエレメント
    parentUIAElement = pywinauto.uia_element_info.UIAElementInfo()

    #一覧確認－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
    #print(parentUIAElement)
    #print(' 1 \n')

    # voiceroidを捜索する
    voiceroid2 = search_child_byname_1("VOICEROID2",parentUIAElement)
    # *がついている場合
    if voiceroid2 == False:
        voiceroid2 = search_child_byname_1("VOICEROID2*",parentUIAElement)

    #ここから変更
    # テキスト要素のElementInfoを取得
    TextEditViewEle = search_child_byclassname_1("TextEditView",voiceroid2)
    textBoxEle = search_child_byclassname_1("TextBox",TextEditViewEle)

    # コントロール取得
    textBoxEditControl = pywinauto.controls.uia_controls.EditWrapper(textBoxEle)

    # テキスト登録
    textBoxEditControl.set_edit_text(speakPhrase)


    # ボタン取得
    buttonsEle = search_child_byclassname_1("Button",TextEditViewEle,target_all = True)
    # 再生ボタンを探す
    playButtonEle = ""
    for buttonEle in buttonsEle:
        # テキストブロックを捜索
        #print(buttonEle)
        #print('\n')
        textBlockEle = search_child_byclassname_1("TextBlock",buttonEle)
        if textBlockEle.name == "音声保存":
            playButtonEle = buttonEle
            break

    # ボタンコントロール取得
    playButtonControl = pywinauto.controls.uia_controls.ButtonWrapper(playButtonEle)

    # 再生ボタン押下
    playButtonControl.click()

