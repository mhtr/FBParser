# FBParser

The bot parses the selected page on Facebook and sends the latest news to the chat.

## Using
```shell script
$ git clone git@github.com:mhtr/FBParser.git
```
```shell script
$ cd FBParser
```
Copy your telegram-bot TOKEN, CHAT_ID and FB_PAGE into ```src/vars.py```

```shell script
$ docker build -t fbparser .
```
```shell script
$ docker volume create posts
```
```shell script
$ cp posts/posts.json /var/lib/docker/volumes/posts/_data
```
```shell script
$ docker run -d --name fbparser --mount source=posts,target=/app/src/posts fbparser
```


