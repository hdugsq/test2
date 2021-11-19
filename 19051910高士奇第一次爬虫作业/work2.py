import requests
from bs4 import BeautifulSoup
import csv,codecs
import re
headers = {
'cookie': 'l=v; _uuid=91B7ECCB-3883-3426-2585-82142272DF5014467infoc; buvid3=82A72ADA-5153-415C-B20C-2B0490F69AA9148798infoc; blackside_state=1; rpdid=|(J~R)u)mJk)0J\'uYkl)~))|R; fingerprint=063061b9f20a5a6e42b73b9425331922; buvid_fp=82A72ADA-5153-415C-B20C-2B0490F69AA9148798infoc; buvid_fp_plain=2363EA36-AF09-442B-827A-0C8264BCEA4B13446infoc; sid=6vubsw6u; DedeUserID=484751573; DedeUserID__ckMd5=e90e884ac77c06ae; SESSDATA=52a790d7%2C1642860004%2C26713*71; bili_jct=7cdc493da20846b2bafbe82ca23fa168; CURRENT_BLACKGAP=1; LIVE_BUVID=AUTO3316277366809070; CURRENT_QUALITY=80; video_page_version=v_old_home_11; CURRENT_FNVAL=976; bp_t_offset_484751573=589154545332888945; innersign=0; bsource=search_baidu; PVID=3; bp_video_offset_484751573=589204448561373642',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.6241 SLBChan/30',
'accept': 'application/json, text/plain, */*'
}
lie=0 #用于排名
f = open("bili.csv", "w",encoding='utf-8',newline='')#指定编码方式为utf-8，写入时不出现空行
writer = csv.writer(f)
writer.writerow(['排名', '名称', '追番人数'])
for j in range(1,173):#仅是页数变化，用for控制
    res = requests.get('https://api.bilibili.com/pgc/season/index/result?season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page='+str(j)+'&season_type=1&pagesize=20&type=1',headers=headers)
    res.encoding = 'utf-8'
    data = res.text
    an=re.findall("\"title\":\".*?\"",data) #re匹配（最小匹配）。
    num=re.findall("\"order\":\".*?\"",data) 
    for i in range(len(an)):
        lie=lie+1
        writer.writerow([lie,an[i][9:-1],num[i][9:-1]])
print("ok")
f.close()