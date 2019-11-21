import shutil

import requests
from facebook_scraper import get_posts


def parse(page_name):
    for post in get_posts(page_name, pages=2):
        post_id = post['post_id']
        text = post['text']
        img_url = post['image']
        # resp = requests.get(img_url, stream=True)
        # with open(post_id + '.img', 'wb') as f:
        #     shutil.copyfileobj(resp.raw, f)
        # del resp


parse('GDGAlmaty')
