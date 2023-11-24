from urllib.parse import urlparse
from github import Github
from datetime import datetime, timezone

def get_username_from_url(url):
    parsed_url = urlparse(url)
    return parsed_url.path.split('/')[-1]

def get_user_info(username):
    g = Github()
    creation_date = g.get_user(username).created_at
    return creation_date

def calculate_account_age(creation_date):
    now = datetime.now(timezone.utc)
    return now - creation_date

# get the user's URL
url = input('Enter the GitHub user\'s URL: ')
username = get_username_from_url(url) # get the username from the URL
print(f'The GitHub username is => {username}')

# get the user's creation date
creation_date = get_user_info(username)
print(f'Created at => {creation_date}')

# calculate the account age
account_age = calculate_account_age(creation_date)
print(f'The GitHub account age is => {account_age}')