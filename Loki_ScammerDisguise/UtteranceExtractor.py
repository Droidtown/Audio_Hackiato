#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from ArticutAPI import Articut
import json
import time
import os
import re
import unicodedata


if __name__ == "__main__":
    with open("account.info") as f:
        accountDICT = json.loads(f.read())

    articut = Articut(username=accountDICT["username"], apikey=accountDICT["apikey"])

    purgedPat = re.compile("</?[a-zA-Z]+?_?[a-zA-Z]*?>")

    key_tokenLIST = ["偽裝", "欺騙", "喬裝", "假裝", "裝成", "佯裝"]
    utteranceLIST = []

    fileLIST = os.listdir("./臺灣澎湖地方法院")
    for f in fileLIST:
        with open("./臺灣澎湖地方法院/{}".format(f)) as j:
            jdict = json.loads(j.read())

        text = jdict["judgement"].replace("\r\n", "").replace(" ", "")
        if any(k in text for k in key_tokenLIST):
            if len(text) >= 20000:
                for i in range(len(text)-1, 0, -1): #倒著推算第一個不是中文字符的東西 (通常就是標點符號了啦)
                    if not unicodedata.name(text[i]).startswith("CJK") and i < 20000:
                        text = text[:i] #很隨便地只取了 2 萬字以內的完整句子。2 萬字以上就…算了。這一段只是草草洗個資料而已，重點是下一步的 Loki
                        break 
                    else: 
                        pass
            else:
                pass

            resultDICT = articut.parse(text)
            while not isinstance(resultDICT, dict) or 'result_pos' not in resultDICT.keys():  
                print(f'Unable to get results for {f}, wait 30 seconds.')
                time.sleep(30)
                resultDICT = articut.parse(text)

            for r in resultDICT["result_pos"]:
                if len(r) == 1:  #標點符號
                    pass
                else:
                    sentence = re.sub(purgedPat, "", r)
                    if any(k in sentence for k in key_tokenLIST):
                        utteranceLIST.append(sentence)


    with open("CollectedUtterance.json", "w", encoding='utf8') as j:
        json.dump(utteranceLIST, j, ensure_ascii=False)


