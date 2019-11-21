import vars
from telegram.ext import Updater
from facebook_scraper import get_posts
import logging
import json


def main():
    updater = Updater(vars.TOKEN)
    j = updater.job_queue

    def newAlert(bot, job):
        with open('posts.json', 'r') as f:
            post_ids = json.load(f)
            print(post_ids['published'])
        for post in reversed(list(get_posts('GDGAlmaty', pages=4))):
            post_id = post['post_id']
            if post_id not in post_ids['published']:
                text = post['text']
                img_url = post['image']
                if img_url:
                    bot.sendMessage(chat_id='252150963', text=img_url)
                if text:
                    bot.sendMessage(chat_id='252150963', text=text, disable_web_page_preview=True)
                post_ids['published'].append(post_id)
                with open('posts.json', 'w') as out:
                    json.dump(post_ids, out)

    j.run_repeating(newAlert, 15)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)
    main()