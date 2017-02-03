# -*- coding: UTF-8 -*-
import json
import codecs
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt

user_id = "me"
# Token facebook
access_token = "YOUR TOKEN HERE"

def getDataFromFb(url):
	r = requests.get(url)
	data = json.loads(r.content.decode('utf8'))

	return data

def getFacebookFeeds(user_id,access_token,num_feeds):
	base = "https://graph.facebook.com/v2.8"
	node = "/%s/feed" % user_id
	fields = "/?fields=message,link,created_time,type,name,id,comments.limit(0).summary(true),shares,reactions.limit(0).summary(true),from"
	parameters = "&limit=%s&access_token=%s" % (num_feeds, access_token)
	
	url = base + node + fields + parameters
	data = getDataFromFb(url)

	return data

if __name__ == '__main__':
	feeds = getFacebookFeeds(user_id,access_token,50)
	has_next_page = True
	#f = codecs.open('wordcloud.txt','w',encoding='utf8')
	t = json.dumps(feeds, ensure_ascii=False)

	info = json.loads(t)
	strC = u""
	for test in info['data']:
		if 'message' in test:
			strC = strC + test['message']
	

	#info = json.loads(t)

	wordcloud = WordCloud(width=1600,height=800).generate(strC)

	# Display the generated image:
	plt.figure(figsize=(20,10), facecolor='k')
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.tight_layout(pad=0)
	plt.show()
	
