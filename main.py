from facebook_scraper import get_posts
import requests
import shutil

for post in get_posts('GDGAlmaty', pages=2):
    post_id = post['post_id']
    print(post['text'])
    url = post['image']
    resp = requests.get(url, stream=True)
    with open(post_id, 'wb') as f:
        shutil.copyfileobj(resp.raw, f)
    del resp

# TODO bot

