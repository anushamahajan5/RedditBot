# Reddit Automation Bot

## Overview
This project is a Python-based Reddit automation bot designed to automate certain tasks on Reddit, such as posting, commenting, or liking posts based on predefined rules. The bot interacts with the Reddit API using `praw`, a Python wrapper for Reddit's API, and performs actions like posting to subreddits, upvoting/downvoting, and commenting based on specific conditions.

## Features
- Automated posting on specific subreddits.
- Ability to comment on posts that match certain keywords.
- Upvote or downvote posts based on user-defined conditions.
- Customizable scheduling for actions.

## Dependencies
- Python 3.x
- `praw` (Python Reddit API Wrapper)
- `time` (For scheduling tasks)
- `schedule` (For task scheduling)

## Setup

### Step 1: Install Required Libraries
Run the following command to install the required dependencies:
```bash
pip install praw schedule
```

### Step 2: Create Reddit Application
1. Visit Reddit App Preferences.
2. Create a new application (choose script).
Obtain the following credentials:
  Client ID
  Client Secret
  User Agent
  Username
  Password

### Step 3: Configure the Bot
Create a config.py file with the following content to store the credentials:
```bash
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
USER_AGENT = 'your-user-agent'
USERNAME = 'your-username'
PASSWORD = 'your-password'
```
### Step 4: Implement the Bot Logic
Created a script bot.py where the bot’s actions are defined

### Step 5: Run the Bot
Execute the bot script with the following command:
```bash
python reddit_bot.py
```
### Step 6: Monitor Results
The bot will:
Post to the "test" subreddit every hour.
Comment on the latest posts in the "learnpython" subreddit if the title contains the keyword "automation."
Check the Reddit subreddits for:
New posts created by the bot.
Comments left by the bot on posts with relevant keywords.

## Results
After running the bot, you should observe:
```bash
(env) C:\Users\anush\OneDrive\Desktop\Projects\SocialMediaBot>python bot.py
Posted to test: Hello Reddit!
Commented on post 1gon66l: This is an automated comment.
Upvoted post 1gon66l
Message sent to MemeMandir: This is a test message.

(env) C:\Users\anush\OneDrive\Desktop\Projects\SocialMediaBot>
````
