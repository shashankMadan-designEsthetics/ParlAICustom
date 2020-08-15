import praw

carReddits = open("car_reddits.txt","r")
carRedditsTest = open("car_reddit_test.txt","r")

allCarTopics = carReddits.read()
allCarTopics = allCarTopics.split(',')

allCarTestTopics = carRedditsTest.read()
allCarTestTopics = allCarTestTopics.split(',')

cartxt = open("cars.txt","w")
cartxtTest = open("cars_test.txt","w")

reddit = praw.Reddit(client_id='Y16r7ELPIvFfWw',client_secret='Qk8TokLSbFYwvUlwlm2J4kQtmAc',user_agent='my user agent')

cars = []
carstest = []

for topic in allCarTopics:
	for submission in reddit.subreddit(topic).comments(limit=None):
		cartxt.writelines(submission.body)

for topic in allCarTestTopics:
	for submission in reddit.subreddit(topic).comments(limit=None):
		cartxtTest.writelines(submission.body)

cartxt.close()
cartxtTest.close()
exit()

with open('train.txt', newline='\n') as read:
        for line in read:
            data = list(line)
            print('run exp teacher', data[0])