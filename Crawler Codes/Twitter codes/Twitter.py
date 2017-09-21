import tweepy
import time
import datetime
from datetime import timedelta
#import simplejson
#coding=utf-8
consumer_key="JQiMmXTEzP4g64arY0TiBaR2E"
consumer_secret="HKtNMzeGLwqlMoiGY0h51lw68a3wfFPGizHfFupyI0RUi9YgGJ"
access_token="2966467018-KLWfDADI8M7g76TFefxjhCbxvbAblge46C7iWlG"
access_token_secret="fPIjBLkF5zOoiJEXPr9LrjOWibDaArdSh8mLrUUzFdiNZ"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

localdate = datetime.datetime.now()
backday =0
datelist =[]
while(backday<30):
    d = localdate - datetime.timedelta(days=backday)
    datelist.append(d.strftime("%Y-%m-%d"))
    backday=backday+1

def get_friendsid(userid):
    ids=[]
    for page in tweepy.Cursor(api.friends_ids,user_id=userid).pages():
        ids.extend(page)
        time.sleep(10)
    return ids

def get_alltweets(userid):
    tweets=[]
    for page in tweepy.Cursor(api.user_timeline,user_id=userid).pages():
        tweets.extend(page)
        time.sleep(60)
    return tweets

def firstfilefunc(frids):
    firstfile = open("firstfile.dat",'w')
    for fd in frids:
        firstfile.write(str(fd))
        list_time =[]
        searched_tweets = api.user_timeline(user_id=fd,include_rts=True,count=200)
        #searched_tweets =  get_alltweets(fd)
        print len(searched_tweets)
        for st in searched_tweets:
            list_time.append(str(st.created_at)[0:10])
        for lt in datelist:
            firstfile.write(","+str(list_time.count(lt)))
        firstfile.write("\n")
        #time.sleep(60)
    firstfile.close()
    return 0

def secfilefunc(friendidlist):
    secfile = open("secondfile.dat",'w')
    for i in range(len(friendidlist)):
        list_friends =[]
        ffriends =  get_friendsid(friendidlist[i])
        print len(ffriends)
        for fd in ffriends:
            list_friends.append(fd)
        for j in range(len(friendidlist)):
            if(j>i):
                if(friendidlist[j] in list_friends):
                    secfile.write(str(friendidlist[i])+" "+str(friendidlist[j])+" "+"1\n")
            else:
                    secfile.write(str(friendidlist[i])+" "+str(friendidlist[j])+" "+"0\n")
        time.sleep(60)
    secfile.close()
    return 0
         
