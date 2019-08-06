# -*- coding: utf-8 -*-#

import re,os,time,urllib,sys,urllib2

from bs4 import BeautifulSoup 

from sqlalchemy import *


dbname = "may5-6"
dbexists = False
if os.path.exists(os.getcwd() + os.sep + "data" + os.sep + dbname + ".db"):
		dbexists = True
db = create_engine('sqlite:///data/%s.db' % dbname)

con = db.connect()

metadata = MetaData(db)

tweet_reply_table = Table('replytweets',
		metadata,
		Column('tweet_id', String(20), unique = True, primary_key=True), 
		Column('user_id', String(20)), 
		Column('username', String(20)), 
		Column('text', String(140)),
		Column('root_tweet_id',String(20)),		   
		Column('root_tweet_username',String(32)),		 
		keep_existing=True)

roottweets = Table('roottweets', metadata, autoload=True)

if not tweet_reply_table.exists():
	tweet_reply_table.create()


def insertData(conn,table,tweet,root_name,root_tweet):
		
	try:
		ins = table.insert(prefixes=['OR IGNORE']).values(
			tweet_id = tweet[2],
			username = tweet[0],
			text = tweet[1],
			root_tweet_id = root_tweet,
			root_tweet_username = root_name
			)
		print conn.execute(ins)

	except Exception as e:
		print(str(e))
		return False

	return True


def getReplies(username,tweet_id,opener): 
	url = "https://mobile.twitter.com/%s/status/%s" % ( username, tweet_id)
	print url
	try: 
		filein = opener.open(url)
		return filein.read()
	except Exception as e:
		print e
		return False

def parseReplies(urltext,user):
	urltext = urltext.replace("timeline replies", "timeline_replies")
	soup = BeautifulSoup(urltext.replace("timeline replies", "timeline_replies"))

	usernames = []
	# for i in tcs:
	x = soup.find_all(class_ ="username")
	for j in x: usernames.append(j.text.strip()[1:])


	tweets = []
	# for i in tcs:
	
	x = soup.find_all("div", class_ ="dir-ltr")
	for j in x: 
		tweets.append(j.text.strip())

	tweetids = []
	x = soup.find_all(class_="tweet-text")
	for j in x: tweetids.append(j['data-id'].strip())

	if len(usernames) == len(tweets) == len(tweetids):
		replies = []
		tweetlist = zip(usernames,tweets,tweetids)
		for i in tweetlist:
			if i[0] == user:
				pass
			elif user in i[1]:
				replies.append(i)		
		return replies
	else:
		print "bad"
		return []



#******************************
# BUILD THE OPENER
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'OII-DSR-2014-BG/1.0')]

#******************************
# Get the root tweets to iterate through
# First get completed tweet IDs 
result = con.execute(select([tweet_reply_table.c.root_tweet_id]))
tweetdonelist = set([])

for row in result: 
	tweetdonelist.add(row["root_tweet_id"])

print len(tweetdonelist)


# Second get the cursor for the table 
topresults = select([roottweets.c.username,roottweets.c.tweet_id])
result = con.execute(topresults)

topcount = 0
topcount2 = 0

try: 
    for row in result:
    	topcount += 1
	

    	if row["tweet_id"] in tweetdonelist or topcount < 299:
    		continue
    	else:
    		tweetdonelist.add(row["tweet_id"])


    	if topcount > 350:
    		break
    	print row["username"],row["tweet_id"]

    	replylist = getReplies(row["username"],row["tweet_id"],opener)
    	if replylist:
    		pass
    	else:
    		print "uh oh"
    		continue

    	for i in parseReplies(replylist,row["username"]):
    		insertData(con,tweet_reply_table,i,row["username"],row["tweet_id"])
		
    	time.sleep(.5)

    	if topcount %100 == 0:
    		print "Working on tweet #%s, from %s" % (topcount, row["username"])

    	topcount2 += 1

except Exception as e:
	  print e


print topcount2

