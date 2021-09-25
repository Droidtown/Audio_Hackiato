#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 2.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""

from requests import post
from requests import codes
import math
try:
    from intent import Loki_Disguise
except:
    from .intent import Loki_Disguise


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = ""
LOKI_KEY = ""
# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "Connect failed."
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST, filterLIST=[]):
    resultDICT = {}
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # Disguise
                if lokiRst.getIntent(index, resultIndex) == "Disguise":
                    resultDICT = Loki_Disguise.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)


def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Loki Result => {}".format(resultDICT))
    return resultDICT

if __name__ == "__main__":
    # Disguise
    print("[TEST] Disguise")
    inputLIST = ['佯裝H','佯裝賣家','佯裝購車','佯裝重殘','假冒公安','假冒友人','假冒員警','假冒檢警','假冒法院','假冒行為','假冒親友','假冒警員','假冒警察','假冒身分','假裝不知','冒充新品','冒充本人','冒充行使','冒充警察','喬裝賭客','佯裝其友人','佯裝書記官','佯裝為綽號','佯裝雇主之','假冒丁○○','假冒丙○○','假冒之方式','假冒公務員','假冒其同事','假冒匯款人','假冒曾觀達','假冒檢察官','假冒食品罪','假冒食用油','假裝成公安','假裝檢察官','假裝算命師','假裝要查詢','冒充丙○○','冒充公務員','冒充林基豐','冒充被害人','喬裝之賭客','佯裝幫忙轉接','佯裝投資獲利','佯裝拍賣車輛','佯裝提領款項','佯裝支付貨款','佯裝正常交易','佯裝為其友人','佯裝為其同學','佯裝為其綽號','佯裝為書記官','佯裝網站人員','佯裝網站賣家','佯裝網路賣家','佯裝該名員工','佯裝該名外務','佯裝賣家刊登','假冒公務人員','假冒公安人員','假冒友人借款','假冒司法人員','假冒司法警察','假冒各種身分','假冒大陸公安','假冒大陸秘書','假冒如附表一','假冒為檢察官','假冒管區警員','假冒警員名義','假冒銀行專員','假冒電信人員','假冒高中同學','假裝上課等語','假裝受理案件','假裝大陸公安','偽裝業務人員','冒充之公務員','冒充司法警察','冒充為張秀芬','冒充警察人員','冒充郵局人員','冒充醫院人員','冒充銀行人員','佯裝之虛擬身分','佯裝係張吳麗玲','佯裝公安之後線','佯裝旅行社業者','佯裝為友人借款','佯裝為友人行騙','佯裝為警察人員','佯裝電信局人員','假冒丁○○名義','假冒丙○○名義','假冒丙○○等語','假冒乙○○之女','假冒健保局人員','假冒公務員名義','假冒公務員詐財','假冒公務員詐騙','假冒公務員部分','假冒公安等職員','假冒同事黃秀雯','假冒名義之本人','假冒失智之女子','假冒宋毓俊朋友','假冒新竹縣警局','假冒林素春女兒','假冒楊聖貞弟弟','假冒檢察官云云','假冒檢察官助理','假冒檢察官名義','假冒檢察官詐騙','假冒渠胞弟佯稱','假冒許中順友人','假冒警員之名義','假冒護士之女生','假冒醫保局人員','假冒醫院護理師','假冒里民王能貴','假裝是家屬去談','假裝白牌計程車','偽裝成○○公司','冒充健保局人員','冒充公務員名義','冒充公務員為之','冒充公務員身分','冒充新品之事實','冒充聲請人所售','佯裝兆豐銀行主任','佯裝大陸地區公安','佯裝檢警執法人員','佯裝江昇平之親友','佯裝為同事黃友芳','佯裝為大陸公部門','佯裝為葉育紜綽號','佯裝網路賣家名義','佯裝進行正常交易','假冒○○醫院員工','假冒中國大陸公安','假冒中華電信人員','假冒之公安局地址','假冒之專員等頭銜','假冒代理人李國鼎','假冒係親友需借款','假冒公安人員丁超','假冒公安人員雷鳴','假冒其友人劉鳳珠','假冒其友人楊壽美','假冒司法人員詐欺','假冒司法機關名義','假冒告訴人甲○○','假冒大陸公安人員','假冒大陸公安單位','假冒大陸公安接聽','假冒大陸公安行騙','假冒大陸地區公安','假冒東森購物人員','假冒東森購物廠家','假冒檢察官或警察','假冒檢警人員謊稱','假冒檢警誆以涉案','假冒為地主張秀芬','假冒玉山銀行人員','假冒真實之持卡人','假冒網路客服人員','假冒義大醫院人員','假冒蔡政宜的名義','假冒警察或檢察官','假冒貸款代辦公司','假冒醫院醫護人員','假冒電話行銷人員','假裝網路銷售人員','偽裝○○公司廠長','冒充之官職為要件','冒充本人提領現金','冒充本人查詢餘額','冒充林基豐之名義','冒充為告訴人本人','冒充盧仲和之女兒','冒充警員身分詐財','喬裝警員隊長謊稱','喬裝賭客之陳義方','佯裝係康惠貞之友人','佯裝其為女性算命師','佯裝圍觀群眾之女子','佯裝失誤或表現不佳','佯裝是電話中之女子','佯裝為中華電信人員','佯裝為其友人張嘉瑩','佯裝為張小明之弟媳','佯裝為檢警人員撥打','佯裝為玉山銀行行員','佯裝為甲○○之友人','佯裝為花旗銀行客服','佯裝為趙美慧之友人','佯裝為郵局客服人員','佯裝為醫院掛號人員','佯裝為陳品棠之友人','佯裝為陳彥騰之客戶','佯裝被害人熟識之人','假冒不知情之陳聖文','假冒公務員僭行職權','假冒公務員詐欺部分','假冒公務員身分犯案','假冒其友人證凱法師','假冒友人希奎之名義','假冒司法人員的部分','假冒名義之人之帳戶','假冒吳金泉車行老闆','假冒報案中心的公安','假冒大橋公司之員工','假冒大陸醫療保險局','假冒朋友身分之方法','假冒檢察官之吳承恩','假冒檢察官施行詐騙','假冒為嘉義市警察局','假冒親友借款之手法','假冒護士打電話給妳','假冒護士打電話過來','假冒電話費催繳人員','假裝係甲○○之友人','偽裝為網路商家人員','冒充係中華電信包商','冒充俗稱第一線人員','冒充公務員僭行職權','冒充新品出售之事實','冒充施工能力而締約','冒充是乙○○的外甥','冒充林泯諒跟你談話','冒充為曾國雄之女兒','冒充為醫院護理人員','冒充Ｃａｌｌ客秘書','佯裝大陸地區公安人員','佯裝為醫護及檢警人員','佯裝謝怡雯友人張圳生','假冒中信銀行服務人員','假冒中國大陸公安隊員','假冒中國大陸法院職員','假冒中華電信客服人員','假冒公務員之情形可指','假冒公務員之方式行騙','假冒公務員詐騙告訴人','假冒公安人員受理報案','假冒友人或親人之名義','假冒司法人員詐欺集團','假冒司法人員詐財案例','假冒國泰世華銀行人員','假冒基隆署立醫院人員','假冒基隆長庚醫院人員','假冒大陸公安名義詐騙','假冒大陸公安接完電話','假冒大陸地區公安人員','假冒大陸地區公安隊員','假冒政府機關或公務員','假冒曾明章表哥林天旺','假冒東森購物服務人員','假冒松富隆公司之員工','假冒檢察官之三線機手','假冒檢察官之名義詐騙','假冒檢察官之方式為之','假冒檢察官打電話過來','假冒檢察官等司法人員','假冒檢警等公務員身分','假冒法官或檢察官身份','假冒為健保局客服人員','假冒王國憲代理人之名','假冒網路賣家客服人員','假冒臺北地方法院人員','假冒蕭小明朋友鍾明達','假冒警員及檢察官辦案','假冒警員身分向人行騙','假冒警官向熊寄辰偽稱','假冒護士與假冒檢察官','假冒身分取信於被害人','假冒金融監管局之主任','假冒銀行專員之陳○穎','假冒長輩之孫女或好友','冒充交通警察取締違規','冒充公務員或其他人員','冒充其友人向其詐騙後','冒充其女兒向其詐騙後','冒充其為有權持卡之人','冒充某名人之真跡作品','佯裝中華電信人員之詐術','佯裝欲出售二手運動手錶','佯裝為中國信託客服人員','佯裝為遠東銀行客服人員','佯裝重殘而申請保險理賠','佯裝雅虎網站拍賣之賣家','假冒丙○○申辦停話之人','假冒代辦貸款業者之要求','假冒係調查局之政風專員','假冒公務員身分行使職權','假冒劉玉珍友人向其借款','假冒司法事務官之甲○○','假冒司法人員詐欺之集團','假冒各種身分以話術詐欺','假冒大陸公安局公安人員','假冒大陸地區公安之工作','假冒大陸法院公證處主任','假冒字跡而躲避鑑定為由','假冒檢察官助理之陳○穎','假冒檢察官向乙○○取款','假冒檢察官或其他公務員','假冒為大陸地區杭州男子','假冒為購物網站客服人員','假冒特定機構之人頭電話','假冒網路賣家及銀行行員','假冒董月滿之人詐欺之前','假冒郵政局客服人員接聽','假冒銀行人員之機房成員','偽裝大陸地區公安局人員','偽裝成代辦信用貸款公司','冒充公務員而行使其職權','冒充公務員職務上的事項','冒充其等為有權持卡之人','冒充友人央求借款等方式','冒充新北市聯合醫院護士','冒充檢察署或法院調查官','冒充為地主張秀芬之憑據','冒充銀聯卡帳戶真正本人','佯裝客人之侯湘芹等人對賭','佯裝為大陸地區公安局人員','佯裝為常春藤網站客服人員','佯裝為新北市新店中山醫院','佯裝賣家刊登販售鞋子一雙','假冒中國電信或醫保局人員','假冒中華電信公司服務人員','假冒中華電信股份有限公司','假冒他人證件前去開戶所得','假冒伊球友蔡平輝名義之人','假冒公務員之方式進行詐騙','假冒公務員手段詐騙之損失','假冒司法機關的你們就不做','假冒司法機關的你們就會做','假冒大眾玫瑰唱片服務人員','假冒天津公安局的詐騙集團','假冒新北市政府某分局員警','假冒新竹市員警去電賴秋雄','假冒業務員及郵局客服人員','假冒檢察官執行職權並傳真','假冒檢警或親友或網購人員','假冒為大陸地區公安局公安','假冒被害人名義打電話報案','假冒警員身分四處向人行騙','假冒護士的女生打電話過來','假冒速易購拍賣網客服人員','假冒高雄長庚醫院掛號人員','假裝一線的110報案系統總機','偽裝為大陸地區公部門致電','冒充不同人員陸續撥打電話','冒充之公務員職務上之權力','冒充公務員而行使其職權者','冒充剛剛坐我隔壁的那個人','冒充政府機關及公務員名義','冒充政府機關或公務員名義','冒充新北市政府警察局警員','冒充是丙○○的朋友宋淑貞','冒充為被害人曾國雄之女兒','假冒代理人李國鼎盜領90萬元','佯裝為其夫妻美國友人呂碧華','佯裝真正執票人欲兌領該票款','假冒○○醫院員工之成年女性','假冒他人名義製作文書為要件','假冒係電信公司客服人員誆稱','假冒大陸地區社服局客服人員','假冒大陸地區郵政局客服人員','假冒檢察官及護士行騙之方式','假冒檢察官的男生打電話過來','假冒為中華電信股份有限公司','假冒為林佑翰去臨櫃取款等語','假冒臺北地方法院之歹徒來電','假冒臺北地檢署高小明檢察官','假冒調查局人員或律師等身分','假冒證件前去開立之人頭帳戶','假冒身分之電話詐騙犯罪型態','假冒金融監管局人員之第三線','假冒鍾鎔聲之專科同學李坤晉','假冒高小明檢察官致電賴秋雄','偽裝銀行內應可協助順利貸款','冒充不同公務員陸續撥打電話','冒充係乙○○之外甥女李美玲','冒充公務員又行使公務員職權','冒充本人提領現金贓款之犯行','冒充為司法警察與林翠芬連繫','冒充良品以資矇騙王星宇夫婦','冒充銀聯卡真正本人輸入密碼','佯裝公司會計或職員取信被害人','佯裝為臺灣台北地方法院之人員','佯裝詐取保險金之詐術行為乙節','佯裝該名外務走向丙○○停車處','佯裝重殘欺騙法院指定之鑑定人','假冒丙○○向電信公司辦理停話','假冒中華電信股份有限公司人員','假冒公務員僭行職權之犯意聯絡','假冒公務員詐欺取財之犯意聯絡','假冒告訴人蔣琨峰之妻舅吳志銘','假冒大陸公安人員雷鳴的就是我','假冒大陸地區公安人員之第二線','假冒大陸地區公安局之公安人員','假冒大陸地區電信或醫保局人員','假冒政府機關或公務員名義為之','假冒檢察官或其他公務員之名義','假冒臺北○○醫院○○分院護士','假冒臺北地方法院檢察署檢察官','假冒臺北慈濟醫院新店分院護士','假冒被害人謝清河之球友蔡平輝','假冒警察身分撥打電話予江佳勳','假冒身分去電向黃桂花訛稱友人','假冒身分者施詐要求面交及匯款','假冒電信警察以電話聯絡葉一郎','假裝其為系爭建物所有人之過程','冒充丙○○給中華電信掛失電話','冒充外國公務員而行使其職權者','冒充警察及財產公證人之名義等','冒充身分行有公權力外觀之行為','佯裝為電話中女主角或扮演女主角','佯裝貸款經辦公司的詐欺集團人員','假冒中國大陸地區當地之公安人員','假冒拍賣網站服務人員及銀行人員','佯裝鞋子廠商及國泰世華銀行林專員','假冒大陸地區中級人民法院客服人員','假冒臺北市政府警察局人員及檢察官','假冒電信公司客服人員或醫保局人員','偽裝為工作正常且政商關係良好之人','佯裝係張吳麗玲之南山人壽女性保險員','佯裝係甲○○上開帳戶之合法使用權人','假冒偵辦刑案之公務員或金融機構人員','假冒具備施工設備及能力而締約之情形','假冒大陸地區一一０指揮中心值班員警','假冒大陸地區郵政或中國工商銀行之行員','假冒龍立銘公司臺南營業處之員工劉景松','假冒龍立銘公司臺南營業處之經理劉景松','假冒新北市政府警察局金融犯罪調查科科長','假冒上海市楊浦公安局經濟犯罪調查科張思偉科長','假冒係中國大陸地區上海市楊浦公安局公安顧國慶']
    testLoki(inputLIST, ['Disguise'])
    print("")

    # 輸入其它句子試看看
    #inputLIST = ["輸入你的內容1", "輸入你的內容2"]
    #filterLIST = []
    #resultDICT = runLoki(inputLIST, filterLIST)
    #print("Result => {}".format(resultDICT))