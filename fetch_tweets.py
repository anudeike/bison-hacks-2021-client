import tweepy as tw
import json

consumer_key= '4jn1fNxh2AsFxOpWst1EVcKD6'
consumer_secret= 'SJtLZAte2GvToUrA1FT4Y1VtKqq2wZBarMTOrqCFXnyt4DcCiP'
access_token= '1161101984688218113-WWCybxdbtm6zk7FsKEw5PFIA9cYhC6'
access_token_secret= 'fFlP1atWxvb6G5RDUW0GqlZ8WfSKBxeMPrLwmtNBf4q5H'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # auth - works
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    search_words = ["#jobsearch -filter:retweets OR #careers -filter:retweets OR #jobhunt -filter:retweets OR #employment -filter:retweets OR #jobposting -filter:retweets OR #HR -filter:retweets OR #work -filter:retweets OR #staffing -filter:retweets OR #jobopening -filter:retweets OR #jobs -filter:retweets"]

    date_since = "2020-11-16"

    # get tweets
    tweets = tw.Cursor(api.search, q=search_words, lang="en", tweet_mode="extended", since=date_since).items(1000)

    # display them
    num = 0
    array_of_json_strings = []
    for tweet in tweets:
        # append each of the json strings to the []
        print(f'{num} :::: {tweet._json}')

        # turn to json string
        array_of_json_strings.append(tweet._json)
        num += 1

    with open('all.json', 'w') as f:
        json.dump(array_of_json_strings, f)



    print("hi")