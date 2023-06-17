# Import libraries
import pandas as pd, tweepy

# Key & access tokens
consumer_key = "YOUR CONSUMER KEY"
consumer_secret = "YOUR CONSUMER SECRET"
access_token = "YOUR ACCESS TOKEN"
access_token_secret = "YOUR ACCESS TOKEN SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open your text file/snscrape output
tweet_url = pd.read_csv("twitter-@EmbarcaderoTech.txt", index_col= None, header = None, names = ["links"])
print(tweet_url.head())

# Extract the tweet_id using .split function
af = lambda x: x["links"].split("/")[-1]
tweet_url['id'] = tweet_url.apply(af, axis=1)
print(tweet_url.head())

# Convert our tweet_url Series into a list
ids = tweet_url['id'].tolist()

# Process the ids by batch or chunks.
total_count = len(ids)
chunks = (total_count - 1) // 50 + 1

# Username, date and the tweet themselves, so my code will only include those queries.
def fetch_tw(ids):
    list_of_tw_status = api.statuses_lookup(ids, tweet_mode= "extended")
    empty_data = pd.DataFrame()
    for status in list_of_tw_status:
        tweet_elem = {"tweet_id": status.id,
                      "screen_name": status.user.screen_name,
                      "tweet":status.full_text,
                      "date":status.created_at,
                      "retweet_count": status.retweet_count,
                      "favorite_count": status.favorite_count}
        empty_data = empty_data.append(tweet_elem, ignore_index = True)
    empty_data.to_csv("embarcaderoTech_Tweets.csv", mode="a")

# Create another for loop to loop into our batches while processing 50 entries every loop
for i in range(chunks):
    batch = ids[i*50:(i+1)*50]
    result = fetch_tw(batch)