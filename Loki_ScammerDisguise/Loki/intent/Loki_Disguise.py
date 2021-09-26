#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Disguise

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Disguise = True
userDefinedDICT = {"asVerb": ["施詐", "面交", "誆稱", "喬裝", "僭行"], "公安": ["警員", "員警", "警局", "警察", "廠長", "地主", "後線"], "綽號": ["客服", "真跡", "銀聯卡"], "郵局": ["公安局", "常春藤", "機房", "中國信託", "中信銀行", "玉山銀行", "花旗銀行", "兆豐銀行", "義大醫院", "警察局", "車行", "電信局", "署立醫院"], "食品": [""]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Disguise:
        print("[Disguise] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["fakeid"] = []
    if utterance == "佯裝[中華電信]人員之詐術":
        resultDICT["fakeid"].append(args[0]+"人員")

    if utterance == "佯裝[其][友人]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "佯裝[其]為[女性]算命師":
        resultDICT["fakeid"].append(args[1] + "算命師")

    if utterance == "佯裝[大陸]地區[公安]":
        resultDICT["fakeid"].append("{}地區{}".format(args[0], args[1]))

    if utterance == "佯裝[大陸]地區[公安]人員":
        resultDICT["fakeid"].append("{}地區{}".format(args[0], args[1]))

    if utterance == "佯裝[客人]之[侯湘芹]等人對賭":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝[旅行社]業者":
        resultDICT["fakeid"].append(args[0] + "業者")

    if utterance == "佯裝[檢警]執法人員":
        resultDICT["fakeid"].append(args[0] + "執法人員")

    if utterance == "佯裝[正常][交易]":
        resultDICT["fakeid"].append("".join(args))

    if utterance == "佯裝[江昇][平]之[親友]":
        resultDICT["fakeid"].append(args[2])

    if utterance == "佯裝[真正][執票人]欲兌領[該]票款":
        resultDICT["fakeid"].append(args[1])

    if utterance == "佯裝[網路]賣家名義":
        resultDICT["fakeid"].append(args[0] + "賣家")

    if utterance == "佯裝[被害人]熟識之人":
        resultDICT["fakeid"].append(args[0] + "熟人")

    if utterance == "佯裝[謝怡雯][友人][張圳生]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "佯裝[賣家]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝[賣家]刊登":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝[賣家]刊登販售[鞋子][一雙]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝[重殘]而申請保險理賠":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝[雅虎網站]拍賣之賣家":
        resultDICT["fakeid"].append(args[0] + "賣家")

    if utterance == "佯裝[鞋子][廠商]及[國泰][世華銀行][林專員]":
        resultDICT["fakeid"].append("".join(args))

    if utterance == "佯裝係[張吳麗玲]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝係[張吳麗玲]之[南山][人壽][女性][保險員]":
        # write your code here
        pass

    if utterance == "佯裝係[甲○○][上]開[帳戶]之[合法][使用權人]":
        # write your code here
        pass

    if utterance == "佯裝兆豐銀行[主任]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝公司[會計]或[職員]取信被害人":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝公安之後線":
        resultDICT["fakeid"].append("線人")

    if utterance == "佯裝圍觀群眾之[女子]":
        resultDICT["fakeid"].append("群眾")

    if utterance == "佯裝是電話[中]之[女子]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "佯裝欲出售[二手]運動手錶":
        # write your code here
        pass

    if utterance == "佯裝為[中國信託]客服[人員]":
        resultDICT["fakeid"].append("客服")

    if utterance == "佯裝為[中華電信]人員":
        resultDICT["fakeid"].append(args[0] + "人員")

    if utterance == "佯裝為[友人]借款":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝為[友人]行騙":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝為[同事][黃友芳]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝為[大陸]地區公安局[人員]":
        resultDICT["fakeid"].append("公安局" + args[1])

    if utterance == "佯裝為[常春藤]網站客服人員":
        resultDICT["fakeid"].append(args[0] + "客服")

    if utterance == "佯裝為[張小明]之[弟][媳]":
        resultDICT["fakeid"].append(args[1] + args[2])

    if utterance == "佯裝為[新北市][新店][中山]醫院":
        resultDICT["fakeid"].append("醫院")

    if utterance == "佯裝為[檢警人員]撥打":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝為[甲○○]之[友人]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "佯裝為[綽號]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝為[臺灣][台北]地方法院之[人員]":
        resultDICT["fakeid"].append(args[2])

    if utterance == "佯裝為[葉育紜][綽號]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "佯裝為[遠東][銀行]客服[人員]":
        resultDICT["fakeid"].append("客服")

    if utterance == "佯裝為[郵局]客服人員":
        resultDICT["fakeid"].append("客服")

    if utterance == "佯裝為[醫護]及[檢警人員]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝為其[友人]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝為其[友人][張嘉瑩]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝為其[夫妻][美國]友人[呂碧華]":
        resultDICT["fakeid"].append("友人")

    if utterance == "佯裝為大陸公部門":
        resultDICT["fakeid"].append("大陸公部門")

    if utterance == "佯裝為玉山銀行[行員]":
        resultDICT["fakeid"].append("銀行" + args[0])

    if utterance == "佯裝為花旗銀行[客服]":
        resultDICT["fakeid"].append("銀行" + args[0])

    if utterance == "佯裝為警察人員":
        resultDICT["fakeid"].append("警察")

    if utterance == "佯裝為醫院[掛號人員]":
        resultDICT["fakeid"].append("醫院" + args[0])

    if utterance == "佯裝為電話[中][女主角]或扮演[女主角]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "佯裝網站[人員]":
        resultDICT["fakeid"].append("網站" + args[0])

    if utterance == "佯裝網路[賣家]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝詐取保險金之詐術行為乙節":
        # write your code here
        pass

    if utterance == "佯裝該名[員工]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝該名[外]務":
        resultDICT["fakeid"].append(args[0] + "務")

    if utterance == "佯裝該名[外]務走向[丙○○]停車處":
        resultDICT["fakeid"].append(args[0] + "外")

    if utterance == "佯裝貸款經辦公司的[詐欺集團]人員":
        resultDICT["fakeid"].append(args[0] + "人員")

    if utterance == "佯裝進行[正常][交易]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "佯裝重殘欺騙法院指定之[鑑定人]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "佯裝雇主之":
        # write your code here
        pass

    if utterance == "佯裝電信局[人員]":
        resultDICT["fakeid"].append("電信局" + args[0])

    if utterance == "假冒[○○醫院]員工":
        resultDICT["fakeid"].append(args[0] + "員工")

    if utterance == "假冒[○○醫院]員工之[成年女性]":
        resultDICT["fakeid"].append(args[0] + "員工")

    if utterance == "假冒[丁○○]名義":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[上海市][楊浦]公安局[經濟]犯罪[調查科][張思偉][科長]":
        resultDICT["fakeid"].append(args[4] + args[5])

    if utterance == "假冒[丙○○]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[丙○○]向電信公司辦理停話":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[丙○○]申辦停話之[人]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[丙○○]等語":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[中國][電信]或[醫][保局人員]":
        resultDICT["fakeid"].append("".join([args[0], args[1]]))

    if utterance == "假冒[中國大陸][公安]隊員":
        resultDICT["fakeid"].append("".join(args))

    if utterance == "假冒[中國大陸]地區當地之[公安]人員":
        resultDICT["fakeid"].append("".join([args[0], args[1]]))

    if utterance == "假冒[中國大陸]法院職員":
        resultDICT["fakeid"].append("法院人員")

    if utterance == "假冒[中華電信][股份][有限]公司[人員]":
        resultDICT["fakeid"].append(args[3])

    if utterance == "假冒[中華電信]公司[服務人員]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒[中華電信]股份[有限]公司":
        resultDICT["fakeid"].append(inputSTR[2:])

    if utterance == "假冒[乙○○]之女":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[他人][名義]製作文書為[要]件":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[他人][證件][前]去開戶所得":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[代理人][李國鼎]盜領90萬元":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[伊][球友][蔡平輝]名義之人":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒[公務]人員":
        resultDICT["fakeid"].append(args[0] + "人員")

    if utterance == "假冒[公務員]之情形[可]指":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[公務員]之方式行騙":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[公務員]之方式進行詐騙":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[公務員]僭行職權":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[公務員]僭行職權之犯意聯絡":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[公務員]手段詐騙之損失":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[公務員]詐欺取財之犯意聯絡":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[公務員]詐欺部分":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[公務員]詐財":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[公務員]詐騙":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[公務員]詐騙告訴人":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[公務員]身分犯案":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[公務員]身分行使職權":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[公務員]部分":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[公安]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[公安][人員]雷鳴":
        resultDICT["fakeid"].append("".join(args))

    if utterance == "假冒[公安]人員丁[超]":
        resultDICT["fakeid"].append(args[0] + "人員")

    if utterance == "假冒[公安]人員受理報案":
        resultDICT["fakeid"].append(args[0] + "人員")

    if utterance == "假冒[公安]等職員":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[其][同事]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒[其]友人[劉鳳珠]":
        resultDICT["fakeid"].append("友人")

    if utterance == "假冒[其]友人[證凱][法師]":
        resultDICT["fakeid"].append("友人")

    if utterance == "假冒[劉玉珍][友人]向其借款":
        resultDICT["fakeid"].append("友人")

    if utterance == "假冒[友人]借款":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[友人]或[親人]之名義":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[司法][事務官]之[甲○○]":
        resultDICT["fakeid"].append("".join([args[0], args[1]]))

    if utterance == "假冒[司法][人員]詐欺":
        resultDICT["fakeid"].append("".join([args[0], args[1]]))

    if utterance == "假冒[司法]人員的部分":
        resultDICT["fakeid"].append(args[0] + "人員")

    if utterance == "假冒[司法]人員詐欺之集團":
        resultDICT["fakeid"].append(args[0] + "人員")

    if utterance == "假冒[司法]人員詐欺集團":
        resultDICT["fakeid"].append(args[0] + "人員")

    if utterance == "假冒[司法]人員詐財案例":
        resultDICT["fakeid"].append(args[0] + "人員")

    if utterance == "假冒[名義]之[人]之[帳戶]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[吳金泉]車行老闆":
        resultDICT["fakeid"].append("老闆")

    if utterance == "假冒[國泰世華]銀行[人員]":
        resultDICT["fakeid"].append("銀行" + args[-1])

    if utterance == "假冒[基隆]署立醫院[人員]":
        resultDICT["fakeid"].append("醫院" + args[-1])

    if utterance == "假冒[基隆]長庚醫院[人員]":
        resultDICT["fakeid"].append("醫院" + args[-1])

    if utterance == "假冒[報案中心]的公安":
        resultDICT["fakeid"].append("公安")

    if utterance == "假冒[大眾玫瑰][唱片]服務人員":
        resultDICT["fakeid"].append("服務人員")

    if utterance == "假冒[大陸][公安][人員][雷鳴]的就是[我]":
        resultDICT["fakeid"].append(args[1] + args[2])

    if utterance == "假冒[大陸][公安]人員":
        resultDICT["fakeid"].append(args[1] + "人員")

    if utterance == "假冒[大陸][公安]名義詐騙":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒[大陸][公安]單位":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒[大陸][公安]接完電話":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒[大陸][公安]接聽":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒[大陸][公安]行騙":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒[大陸][地區社][服局]客服人員":
        resultDICT["fakeid"].append(inputSTR[2:])

    if utterance == "假冒[大陸]公安":
        resultDICT["fakeid"].append("公安")

    if utterance == "假冒[大陸]公安局公安[人員]":
        resultDICT["fakeid"].append("公安")

    if utterance == "假冒[大陸]地區[一一０][指揮中心]值班[員警]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[大陸]地區[中]級[人民]法院客服人員":
        resultDICT["fakeid"].append("法院人員")

    if utterance == "假冒[大陸]地區[公安]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[大陸]地區[公安][人員]之[第二線]":
        resultDICT["fakeid"].append(args[1] + args[2])

    if utterance == "假冒[大陸]地區[公安]之工作":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[大陸]地區[公安]人員":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[大陸]地區[公安]隊員":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[大陸]地區[郵政]或[中國][工商][銀行]之[行員]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[大陸]地區[郵政局]客服人員":
        resultDICT["fakeid"].append(args[1] + "客服")

    if utterance == "假冒[大陸]地區[電信]或[醫][保局人員]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[大陸]地區公安局之[公安]人員":
        resultDICT["fakeid"].append(args[-1] + "人員")

    if utterance == "假冒[大陸]法院[公證處][主任]":
        resultDICT["fakeid"].append("".join(args[-2:]))

    if utterance == "假冒[大陸]醫療[保險局]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[天津]公安局的[詐騙集團]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[字跡]而躲避鑑定為由":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[宋毓俊]朋友":
        resultDICT["fakeid"].append("朋友")

    if utterance == "假冒[張小明]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[政府][機關]或[公務員]名義為之":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[政府]機關或[公務員]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[新北]市政府[某]分局[員警]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[新北]市政府[警察局][金融]犯罪[調查科][科長]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[新竹市][員警]去電[賴秋雄]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒[新竹縣]警局":
        resultDICT["fakeid"].append("警局")

    if utterance == "假冒[曾明章][表哥][林天旺]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒[朋友身分]之方法":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[東森]購物人員":
        resultDICT["fakeid"].append("服務人員")

    if utterance == "假冒[東森]購物廠家":
        resultDICT["fakeid"].append("廠家")

    if utterance == "假冒[東森]購物服務人員":
        resultDICT["fakeid"].append("服務人員")

    if utterance == "假冒[林素春][女兒]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒[業務員]及郵局客服人員":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢察官]之[吳承恩]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢察官]之三線機手":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢察官]之名義詐騙":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢察官]之方式為之":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢察官]助理":
        resultDICT["fakeid"].append("助理")

    if utterance == "假冒[檢察官]助理之[陳○穎]":
        resultDICT["fakeid"].append("助理")

    if utterance == "假冒[檢察官]及[護士]行騙之方式":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢察官]向[乙○○]取款":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢察官]執行職權並傳真":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢察官]或其他[公務員]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢察官]或其他[公務員]之名義":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢察官]施行詐騙":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢察官]的[男生]打電話過來":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢察官]等司法[人員]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢警]或[親友]或[網購人員]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢警]等[公務員]身分":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢警]誆以涉案":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[檢警人員]謊稱":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[法官]或[檢察官]身份":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[渠胞][弟]佯稱":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[特定][機構]之[人頭][電話]":
        resultDICT["fakeid"].append("".join(args[-2:]))

    if utterance == "假冒[真實]之[持卡人]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[管區]警員":
        resultDICT["fakeid"].append("警員")

    if utterance == "假冒[網路][賣家]及[銀行][行員]":
        resultDICT["fakeid"].append("".join(args[0:2]))

    if utterance == "假冒[網路][賣家]客服[人員]":
        resultDICT["fakeid"].append("客服" + args[-1])

    if utterance == "假冒[網路]客服[人員]":
        resultDICT["fakeid"].append("客服" + args[-1])

    if utterance == "假冒[臺北][地方][法院][檢察署][檢察官]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[臺北][地方][法院]之[歹徒]來電":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[臺北][慈濟]醫院[新店]分院[護士]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[臺北]○○[醫院○○]分院[護士]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[臺北]地方[法院]人員":
        resultDICT["fakeid"].append(args[-1] + "人員")

    if utterance == "假冒[臺北]地檢署[高小明]檢察官":
        resultDICT["fakeid"].append("檢察官")

    if utterance == "假冒[臺北]市政府[警察局][人員]及[檢察官]":
        resultDICT["fakeid"].append(args[1] + args[2])

    if utterance == "假冒[董月滿]之[人]詐欺[之前]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒[蔡政宜]的[名義]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[蕭小明][朋友][鍾明達]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒[被害人]名義打電話報案":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[親友]借款之手法":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[許][中][順友人]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒[調查局][人員]或[律師]等身分":
        resultDICT["fakeid"].append(args[0] + args[1])

    if utterance == "假冒[證件][前]去開立之人頭帳戶":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[警員]及[檢察官]辦案":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[警員]名義":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[警員]身分[四處]向人行騙":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[警員]身分向人行騙":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[警官]向[熊寄辰]偽稱":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[警察][身分]撥打電話予[江佳勳]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[護士]之女生":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[護士]打電話給[妳]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[護士]打電話過來":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[護士]的女生打電話過來":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[護士]與假冒[檢察官]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[身分]之電話詐騙犯罪型態":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[身分]取信於被害人":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[身分者]施詐要求面交及匯款":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒[速][易購]拍賣網客服人員":
        resultDICT["fakeid"].append("客服")

    if utterance == "假冒[郵政局]客服人員接聽":
        resultDICT["fakeid"].append("客服")

    if utterance == "假冒[醫院]護理師":
        resultDICT["fakeid"].append("護理師")

    if utterance == "假冒[金融][監管局]之主任":
        resultDICT["fakeid"].append("主任")

    if utterance == "假冒[金融][監管局]人員之[第三線]":
        resultDICT["fakeid"].append("線人")

    if utterance == "假冒[銀行][人員]之[機房]成員":
        resultDICT["fakeid"].append(args[-1] + "人員")

    if utterance == "假冒[銀行][專員]之[陳○穎]":
        resultDICT["fakeid"].append(args[0] + args[1])

    if utterance == "假冒[銀行]專員":
        resultDICT["fakeid"].append(args[0] + "專員")

    if utterance == "假冒[鍾鎔聲]之[專科][同學][李坤晉]":
        resultDICT["fakeid"].append(args[-2])

    if utterance == "假冒[長輩]之[孫女]或[好友]":
        resultDICT["fakeid"].append(args[-2])

    if utterance == "假冒[電信][警察]以電話聯絡[葉一郎]":
        resultDICT["fakeid"].append(args[0] + args[1])

    if utterance == "假冒[電信公司]客服人員或[醫][保局人員]":
        resultDICT["fakeid"].append(args[0] + "客服人員")

    if utterance == "假冒[電話][費]催繳人員":
        resultDICT["fakeid"].append("催繳人員")

    if utterance == "假冒[電話]行銷人員":
        resultDICT["fakeid"].append("行銷人員")

    if utterance == "假冒[高小明][檢察官]致電[賴秋雄]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒[高雄][長庚醫院]掛號人員":
        resultDICT["fakeid"].append("掛號人員")

    if utterance == "假冒[龍立銘]公司[臺南][營業處]之員工[劉景松]":
        resultDICT["fakeid"].append("員工")

    if utterance == "假冒[龍立銘]公司[臺南][營業處]之經理[劉景松]":
        resultDICT["fakeid"].append("經理")

    if utterance == "假冒不知情之[陳聖文]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒中信銀行[服務人員]":
        resultDICT["fakeid"].append("銀行" + args[0])

    if utterance == "假冒中國大陸公安":
        resultDICT["fakeid"].append("公安")

    if utterance == "假冒之公安局[地址]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒之專員等頭銜":
        resultDICT["fakeid"].append("專員")

    if utterance == "假冒代理人[李國鼎]":
        resultDICT["fakeid"].append("代理人")

    if utterance == "假冒代辦貸款[業者]之要求":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒係[中國大陸]地區[上海市][楊浦]公安局[公安][顧國慶]":
        resultDICT["fakeid"].append(args[-2])

    if utterance == "假冒係[親友]需借款":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒係[調查局]之[政風]專員":
        resultDICT["fakeid"].append("專員")

    if utterance == "假冒係[電信公司]客服人員誆稱":
        resultDICT["fakeid"].append("客服")

    if utterance == "假冒偵辦[刑案]之[公務員]或[金融][機構][人員]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒公務員名義":
        resultDICT["fakeid"].append("公務員")

    if utterance == "假冒具備施工[設備]及[能力]而締約之[情形]":
        # write your code here
        pass

    if utterance == "假冒友人[希奎]之名義":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒司法[機關]的[你們]就[會]做":
        resultDICT["fakeid"].append("司法" + args[0])

    if utterance == "假冒司法[機關]的[你們]就不做":
        resultDICT["fakeid"].append("司法" + args[0])

    if utterance == "假冒司法[警察]":
        resultDICT["fakeid"].append("司法" + args[0])

    if utterance == "假冒司法機關名義":
        resultDICT["fakeid"].append("司法機關")

    if utterance == "假冒各種[身分]以話術詐欺":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒同事[黃秀雯]":
        resultDICT["fakeid"].append("同事")

    if utterance == "假冒名義之本人":
        # write your code here
        pass

    if utterance == "假冒告訴人[甲○○]":
        # write your code here
        pass

    if utterance == "假冒告訴人[蔣琨峰]之[妻][舅][吳志銘]":
        resultDICT["fakeid"].append(args[1] + args[2])

    if utterance == "假冒大陸[秘書]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒失智之[女子]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒張小明[弟弟]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒拍賣網站[服務人員]及[銀行][人員]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒松[富]隆公司之員工":
        resultDICT["fakeid"].append("公司員工")

    if utterance == "假冒檢察官或警察":
        resultDICT["fakeid"].append("檢察官")

    if utterance == "假冒為[中華電信][股份][有限]公司":
        resultDICT["fakeid"].append("".join(args) + "公司")

    if utterance == "假冒為[健保局]客服[人員]":
        resultDICT["fakeid"].append("客服" + args[-1])

    if utterance == "假冒為[嘉義市][警察局]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒為[地主][張秀芬]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒為[大陸]地區[杭州][男子]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒為[大陸]地區公安局[公安]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒為[林佑翰]去臨櫃取款等語":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒為[檢察官]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒為購物[網站]客服[人員]":
        resultDICT["fakeid"].append("客服" + args[-1])

    if utterance == "假冒玉山銀行[人員]":
        resultDICT["fakeid"].append("銀行" + args[0])

    if utterance == "假冒王國憲代理人之名":
        resultDICT["fakeid"].append("代理人")

    if utterance == "假冒義大醫院[人員]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒被害人[謝清河]之[球友][蔡平輝]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "假冒警員之名義":
        resultDICT["fakeid"].append("警員")

    if utterance == "假冒警察或檢察官":
        resultDICT["fakeid"].append("警員")

    if utterance == "假冒貸款[代辦公司]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假冒身分去電向[黃桂花]訛稱[友人]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假冒醫保局人員":
        resultDICT["fakeid"].append("醫保局人員")

    if utterance == "假冒里民[王能貴]":
        resultDICT["fakeid"].append("里民")

    if utterance == "假裝[其]為[系爭][建物][所有][人]之過程":
        # write your code here
        pass

    if utterance == "假裝[網路]銷售人員":
        resultDICT["fakeid"].append("銷售人員")

    if utterance == "假裝一線的110報案系統[總機]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假裝係[甲○○]之[友人]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "假裝大陸[公安]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假裝成[公安]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假裝是[家屬]去談":
        resultDICT["fakeid"].append(args[0])

    if utterance == "假裝白牌計程車":
        resultDICT["fakeid"].append("白牌計程車")

    if utterance == "偽裝[大陸]地區公安局[人員]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "偽裝[業務]人員":
        resultDICT["fakeid"].append(args[0] + "人員")

    if utterance == "偽裝[銀行][內][應][可]協助[順利]貸款":
        resultDICT["fakeid"].append(args[0] + "內應")

    if utterance == "偽裝○○公司廠長":
        resultDICT["fakeid"].append("廠長")

    if utterance == "偽裝成○○公司":
        resultDICT["fakeid"].append("公司")

    if utterance == "偽裝成代辦[信用貸款][公司]":
        resultDICT["fakeid"].append("".join(args))

    if utterance == "偽裝為[大陸]地區[公部門]致電":
        resultDICT["fakeid"].append(args[1])

    if utterance == "偽裝為[網路商][家人員]":
        resultDICT["fakeid"].append("".join(args))

    if utterance == "偽裝為工作[正常]且[政商關係][良好]之[人]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "冒充[不同][人員][陸續]撥打電話":
        resultDICT["fakeid"].append(args[1])

    if utterance == "冒充[丙○○]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[丙○○]給[中華電信]掛失[電話]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[交通][警察]取締違規":
        resultDICT["fakeid"].append(args[0] + args[1])

    if utterance == "冒充[公務員]僭行職權":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[公務員]又行使[公務員]職權":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[公務員]名義":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[公務員]或其他[人員]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[公務員]為之":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[公務員]而行使[其]職權":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[公務員]而行使[其]職權者":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[公務員]職務[上]的事項":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[公務員]身分":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[其][友人]向其詐騙[後]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "冒充[其]為有[權]持卡之[人]":
        resultDICT["fakeid"].append(args[2])

    if utterance == "冒充[其]等為有權持卡之[人]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "冒充[其女兒]向其詐騙[後]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[剛剛]坐[我][隔壁]的那個人":
        resultDICT["fakeid"].append("熟人")

    if utterance == "冒充[友人]央求借款等方式":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[外國][公務員]而行使[其]職權者":
        resultDICT["fakeid"].append(args[1])

    if utterance == "冒充[政府][機關]及[公務員]名義":
        resultDICT["fakeid"].append(args[1])

    if utterance == "冒充[新北]市政府[警察局][警員]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "冒充[新北市]聯合醫院護士":
        resultDICT["fakeid"].append("護理師")

    if utterance == "冒充[新品]之事實":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[新品]出售之事實":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[施工能力]而締約":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[林基豐]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[林基豐]之名義":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[林泯諒]跟[你][談話]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[某][名人]之[真跡][作品]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "冒充[檢察][署]或[法院][調查官]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "冒充[盧仲和]之[女兒]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "冒充[聲請人]所售":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[良品]以資矇騙[王星宇][夫婦]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[警員]身分詐財":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[警察]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[警察]及[財產][公證人]之名義等":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[身分]行有公權力[外]觀之行為":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[銀聯卡][真正]本[人]輸入密碼":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充[銀聯卡]帳戶[真正]本[人]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充之[公務員]職務[上]之權力":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充之[官職]為[要]件":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充係[中華電信]包商":
        resultDICT["fakeid"].append(args[0] + "廠商")

    if utterance == "冒充係[乙○○]之[外甥女][李美玲]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "冒充俗稱[第一線]人員":
        resultDICT["fakeid"].append(args[0] + "人員")

    if utterance == "冒充健保局[人員]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充司法[警察]":
        resultDICT["fakeid"].append("司法" + args[0])

    if utterance == "冒充是[丙○○]的[朋友][宋淑貞]":
        resultDICT["fakeid"].append(args[1])

    if utterance == "冒充是[乙○○]的[外甥]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "冒充本[人]":
        resultDICT["fakeid"].append("本" + args[0])

    if utterance == "冒充本[人]提領[現金][贓款]之犯行":
        resultDICT["fakeid"].append("本" + args[0])

    if utterance == "冒充本人提領[現金]":
        resultDICT["fakeid"].append("本人")

    if utterance == "冒充本人查詢[餘額]":
        resultDICT["fakeid"].append("本人")

    if utterance == "冒充為[司法][警察]與[林翠芬]連繫":
        resultDICT["fakeid"].append(args[0] + args[1])

    if utterance == "冒充為[告訴人]本人":
        resultDICT["fakeid"].append("本人")

    if utterance == "冒充為[張秀芬]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充為[曾國雄]之[女兒]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "冒充為[被害人][曾國雄]之[女兒]":
        resultDICT["fakeid"].append(args[-1])

    if utterance == "冒充為地主[張秀芬]之憑據":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充為醫院[護理人員]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "冒充警察[人員]":
        resultDICT["fakeid"].append("警察" + args[0])

    if utterance == "冒充郵局[人員]":
        resultDICT["fakeid"].append("郵局" +  args[0])

    if utterance == "冒充醫院[人員]":
        resultDICT["fakeid"].append("醫院" + args[0])

    if utterance == "冒充銀行[人員]":
        resultDICT["fakeid"].append("銀行" + args[0])

    if utterance == "冒充Ｃａｌｌ客秘書":
        resultDICT["fakeid"].append("秘書")

    if utterance == "喬裝[警員][隊長]謊稱":
        resultDICT["fakeid"].append(args[0] + args[1])

    if utterance == "喬裝[賭客]":
        resultDICT["fakeid"].append(args[0])

    if utterance == "喬裝[賭客]之[陳義方]":
        resultDICT["fakeid"].append(args[0])

    return resultDICT