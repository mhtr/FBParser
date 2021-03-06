import json
import logging

from facebook_scraper import get_posts
from telegram.ext import Updater

import vars


def main():
    updater = Updater(vars.TOKEN)
    j = updater.job_queue

    def newAlert(bot, job):
        with open('/app/src/posts/posts.json', 'r') as f:
            post_ids = json.load(f)
            print(post_ids['published'])
        for post in reversed(list(get_posts(vars.FB_PAGE, pages=2))):
            post_id = post['post_id']
            if post_id not in post_ids['published']:
                text = post['text']
                img_url = post['image']
                if img_url:
                    bot.send_photo(chat_id=vars.CHAT_ID, photo=img_url)
                if text:
                    bot.sendMessage(chat_id=vars.CHAT_ID, text=text, disable_web_page_preview=True)
                post_ids['published'].append(post_id)
                with open('/app/src/posts/posts.json', 'w') as out:
                    json.dump(post_ids, out)
                logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - Post {} added!'.format(post_id), level=logging.INFO)

    j.run_repeating(newAlert, 60)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()