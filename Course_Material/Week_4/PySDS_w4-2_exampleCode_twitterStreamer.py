# -*- coding: utf-8 -*-
import time
import smtplib
import sys
import tweepy
import json

class CustomStreamListener(tweepy.StreamListener):

    def __init__ (self,limit=100,outfile="fileout.dat",counter=10):
        self.count = 0
        self.limit = limit
        self.counter = counter
        self.fileout = open(outfile,'a')
        
    def on_error(self, status_code):
        print ('Encountered error with status code:', status_code)
        return True # Don't kill the stream

    def on_timeout(self):
        print('Timeout...')
        time.sleep(1)
        return True # Don't kill the stream

    def on_data(self, data):
        self.count += 1
        if self.count % self.counter == 0:
            print("Processing Tweet: %s" % self.count)
        if self.count == self.limit:
            self.fileout.close()
            return False
        else:
            self.fileout.write(data.strip() + "\n")

def send_email(test=True, text = "",pw=""):

    if pw == "":
        print("Did not include a password")
        return False
    gmail_user = "bernie.hogan@gmail.com"
    gmail_pwd = pw # Use your own password! - see https://security.google.com/settings/security/apppasswords
    FROM = "bernie.hogan@gmail.com"
    if test:
        TO = ["bernie.hogan@oii.ox.ac.uk"]
    SUBJECT = "Help, the stream is broken!"
    TEXT = "The stream produced an error. Please return to the server and check it out. %s" % text
    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    print(message)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")



def main(argv):
    TWEETFILE = "Tweet_Output.dat"

    keys = json.loads(open("twitter_keys.json").read())

    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'],keys['CONSUMER_SECRET'])
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_TOKEN_SECRET'])

    api = tweepy.API(auth)

    if api:
        print("Successfully Authenticated")
    else:
        print("Problems with authentication")

    # Notice that this instantiates the stream listener but it does not start it. 
    streaming_api = tweepy.streaming.Stream(auth, 
                    CustomStreamListener(limit=10,outfile=TWEETFILE,counter=2), 
                    timeout=60)
    
    # This is the filter we use; filters on twitter can be very complex. 
    TWEET_FILTER = ["Trump"]
    
    # This starts the stream listener. 
    try:
        streaming_api.filter(follow=None, track=TWEET_FILTER)
    except Exception as e:
        send_email(text = "We received the following error that stopped the program: %s" % e)        

if __name__ == "__main__":
    main(sys.argv)
#    keys = json.loads(open("twitter_keys.json").read())


