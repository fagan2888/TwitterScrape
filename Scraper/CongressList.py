import tweepy
from tweepy import OAuthHandler
import twitter_creds
import fileinput

auth = OAuthHandler(twitter_creds.CONSUMER_KEY, twitter_creds.CONSUMER_SECRET)
auth.set_access_token(twitter_creds.ACCESS_TOKEN, twitter_creds.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# modified snippet from https://gist.github.com/macloo/5c69cdf5294fa97eb41d6ad950233cee
slug = 'governors'
owner = 'cspan'
# slug and owner is in the url of the list

members = []
# without this you only get the first 20 list members
for page in tweepy.Cursor(api.list_members, owner, slug).items():
    members.append(page)
# create a list containing all usernames
f = open('government_users.txt', 'a')

for user in members:
    f.write(user.screen_name + '\n')

f.close()