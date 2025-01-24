import praw
from config import REDDIT  # Import credentials from config.py
from praw.exceptions import RedditAPIException
from requests.exceptions import RequestException

# Reddit API authentication
reddit = praw.Reddit(
    client_id=REDDIT["client_id"],
    client_secret=REDDIT["client_secret"],
    username=REDDIT["username"],
    password=REDDIT["password"],
    user_agent=REDDIT["user_agent"]
)

# Example: Post to a subreddit
def post_to_subreddit(subreddit_name, title, body):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        subreddit.submit(title, selftext=body)
        print(f"Posted to {subreddit_name}: {title}")
    except RedditAPIException as e:
        print(f"Reddit API error: {e}")
    except RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example: Comment on a post
def comment_on_post(post_id, comment_text):
    try:
        post = reddit.submission(id=post_id)
        post.reply(comment_text)
        print(f"Commented on post {post_id}: {comment_text}")
    except RedditAPIException as e:
        print(f"Failed to comment: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example: Upvote a post
def upvote_post(post_id):
    try:
        post = reddit.submission(id=post_id)
        post.upvote()
        print(f"Upvoted post {post_id}")
    except RedditAPIException as e:
        print(f"Failed to upvote: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example: Send a private message
def send_private_message(username, subject, message):
    try:
        reddit.redditor(username).message(subject=subject, message=message)  # Updated to use keyword arguments
        print(f"Message sent to {username}: {message}")
    except RedditAPIException as e:
        print(f"Failed to send message: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Post to r/test
    post_to_subreddit("test", "Hello Reddit!", "This is an automated post.")

    # Comment on a specific post (replace `post_id` with an actual post ID)
    comment_on_post("1gon66l", "This is an automated comment.")

    # Upvote a specific post (replace `post_id` with an actual post ID)
    upvote_post("1gon66l")

    # Send a private message (replace `example_user` with a real username)
    send_private_message("MemeMandir", "Hello!", "This is a test message.")
