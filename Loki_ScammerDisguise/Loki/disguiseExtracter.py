#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import os
import re

from LawsWatch import runLoki

def judgeReader(judgeFILE):
    '''
    讀入判決書檔案
    回傳判決書內容主文
    '''
    judgeDICT = json.load(open(judgeFILE, encoding="utf-8").read())
    return judgeDICT["judgement"].replace("\r\n", "").replace("　", "").replace(" ", "")

def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = {}
    for i in range(0, len(inputLIST)-20, 20):
        tmpDICT = runLoki(inputLIST[i:i+20], filterLIST)
        if tmpDICT == {}:
            pass
        else:
            if "fakeid" in tmpDICT.keys():
                for f in tmpDICT["fakeid"]:
                    if f == "":
                        pass
                    elif f in resultDICT.keys():
                        resultDICT[f] = resultDICT[f] + 1
                    else:
                        resultDICT[f] = 1
    return resultDICT


if __name__ == "__main__":
    testSTR = """
    上列被告因妨害風化案件，業經偵查終結，認為宜聲請以簡易判
    決處刑，茲將犯罪事實及證據並所犯法條分敘如下：
        犯罪事實
    一、甲○○ ○ ○ ○ 可預見將自己所使用之行動電話門號出賣
    或交付予他人使用，將可能使色情應召站利用該門號做為媒
    介女子與他人性交易以營利使用，仍基於幫助不詳應召站集
    團使女子與他人為性交行為而媒介以營利之犯意，於民國10
    8年7月8日前某日，在不詳地點，申辦行動電話門號0000000
    000號（下稱本案門號），於不詳時、地，以不詳之代價，
    提供本案門號SIM卡予真實姓名年籍不詳之應召站集團成員
    ，幫助該成員所屬之應召集團，利用該行動電話門號經營應
    召站之用。嗣該應召集團成年成員基於意圖使女子與他人為
    性交行為而媒介以營利之犯意，將本案門號連同性交易訊息
    刊登於捷克論壇網站上，使不特定人得於閱覽後以本案開門
    號聯繫應召集團成員，續由該成員媒介應召女子邱翠娥與不
    特定人為性交易。後於108年7月8日下午4時50分前某時，為
    警佯裝客人，以電話撥打本案門號與應召集團成員議定性交
    易之時、地及代價後，於同日下午4時50分許，在新北市○
    ○區○○路000巷00弄0號2樓2號房欲從事性交易，經員警表
    明身分後，因而查悉上情。""".replace("\r\n", "").replace("　", "").replace(" ", "")
    resultDICT = getLokiResult(testSTR)


    targetDIR = "臺灣苗栗地方法院"
    resultDICT = {}
    judgeFileLIST = [f for f in os.listdir(targetDIR) if not f.startswith(".")]
    for j in judgeFileLIST:
        print("Processing:{}".format(j))
        judgmentSTR = judgeReader("{}/{}".format(targetDIR, j))
        tmpDICT = getLokiResult(judgmentSTR)
        for fk in tmpDICT.keys():
            if fk in resultDICT.keys():
                resultDICT[fk] = resultDICT[fk] + tmpDICT[fk]
            else:
                resultDICT[fk] = 1
        if resultDICT != {}:
            print("Result:", resultDICT)
    with open("{}.json".format(targetDIR), mode="w", encoding="utf-8") as f:
        json.dump(resultDICT, f, ensure_ascii=False)
