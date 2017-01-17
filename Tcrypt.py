# -*- coding:utf8 -*-
#!/usr/bin/python
import crypt   #导入crypt模块
import time
start_time = time.time()   #计时器
src="ubuntu:$6$gOUenfjr$aHEraR/pVULmyniCeKFxU/aBp5QxmMtiwwlaRnmekWkiVmCeOXjxC0ueS4v9iIMXvKqfTozXnHP6Bn2JppWAk/:17165:0:99999:7:::"   #从/etc/shadow所得
username=src.split(":",1)[0]     #以冒号分割，分成两部分，得到一个列表，取第一部分
print username
lst=src.split(":",2)[1]      #以冒号分割，分成两部分，得到一个列表，取第二部分即加密之后的密码字符串
print lst
start_index=lst.find("$")    #找到第一个“$”出现的索引
finish_index=lst.rfind("$")  #找到最后一个“$”出现的索引
salt=lst[start_index:finish_index+1]    #两个$之间的为盐
dic=["a",'b','c', 'd', 'admin', 'c','123456']    #字典
print salt
for word in dic:
    if crypt.crypt(word,salt) == lst:
        print "I find it:" + word
        print "The username is:"+username
        break
else:
    print "serching is failed"    #这里用到了for else.如果是以break退出的，说明找到了密码，则不会执行else.如果没有找到密码，遍历结束后执行else语句（只执行一次，若写在for里面，则每次遍历一个元素执行一次else）。
print time.time()-start_time
