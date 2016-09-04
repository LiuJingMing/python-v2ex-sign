#!/usr/bin/python
#coding:utf-8
import requests,re
V2EX_HOST = "https://www.v2ex.com"
class v2ex:
    s=requests.Session()
    def login(self):
        loginpage = self.s.get("%s/signin" % V2EX_HOST).text
        payload={
            re.findall('type="text" class="sl" name="([a-f0-9]{64,64})"', loginpage)[0]:self.u,
            re.findall('type="password" class="sl" name="([a-f0-9]{64,64})"', loginpage)[0]:self.p,
            "next":"/",
            "once":re.findall('value="(\d+)" name="once"',loginpage)[0]
            }
        signin=self.s.post("%s/signin" % V2EX_HOST,data=payload,headers={'Referer': '%s/signin' % V2EX_HOST})
        if signin.text.find("signout")==-1:
            print self.u+" 登录失败！"
        else:
            print self.u+" 登录成功！"
            self.sign()
    def sign(self):
        if self.s.get("%s/mission/daily" % V2EX_HOST).text.find("fa-ok-sign")!=-1:
            print self.u+" 已领取过奖励!"
        else:
            try:
                daily=re.findall('(/mission/daily/redeem\?once=\d+)',self.s.get("%s/mission/daily" % V2EX_HOST).text)[0]
                a=self.s.get( V2EX_HOST + daily,headers={"Referer":"%s/mission/daily" % V2EX_HOST})
                print self.u+" 签到成功！"
            except:
                print self.u+" 签到失败！"
    def __init__(self,u,p):
        self.u=u
        self.p=p
        self.login()
v2ex("username","password")
