import praw

reddit = praw.Reddit(client_id = 'FhCZAoozfF60nQ', client_secret = 'qT_sfXUwNI5IIVgoqSAgpEKaWUo', user_agent = 'rougndraft', username = 'BrightnessShallanVin', password = 'Waterband')

# reddit = create_reddit_object()

thewallstreet_subred = reddit.subreddit('thewallstreet') 

hot = thewallstreet_subred.hot(limit=5)
new = thewallstreet_subred.new(limit=5)
contr = thewallstreet_subred.controversial(limit=5)
top = thewallstreet_subred.top(limit=5)
gild = thewallstreet_subred.gilded(limit=5)


for i in hot:
    print(f'{i.subreddit_name_prefixed} \n {i.title} \n at: {i.shortlink} \n {i.selftext} \n upvotes: {i.ups} \n downvotes: {i.downs} \n # of comments: {i.num_comments} \n score:{i.score} \n')
    for comment in i.comments:
        print(comment.body)
    
    