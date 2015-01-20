import praw

r = praw.Reddit(user_agent = "Reddit Bot by Lucas Hom")
#use this to login
r.login("insert_username","insert_password")

wordbank = ['bad', 'terrible','lousy','garbage','rip','low']
already_read[]

def reddit_bot()
	print("accessing subreddit")
	subreddit = r.get_subreddit("frugalmalefashion")
	print("accessing comments")
   	comments = subreddit.get_comments(limit=200)
	for comment in comments:
    	comment_content = comment.body.lower()
    	isMatch = any(string in comment_content for string in wordbank)
        if comment.id not in cache and isMatch:	
        	print("found keyword! ID is: " + comment.id)
        	comment.reply('Note taken!')
        	print("reply written")
        	already_read.append(comment.id)


while True:
	reddit_bot()
	time.sleep(20)
