__author__ = 'Aguarate - @aguarate'
# -*- coding:UTF-8

import tweepy, OAuth, URLs, os

auth=OAuth.login()
api = tweepy.API(auth)
import time
import random

ID_sv = os.path.expanduser('~/.botijo_lastid')


if not os.path.exists(ID_sv):
    since = "533935298606952448"
else:
    f = open(ID_sv, 'r')
    since = f.readline().strip()
    f.close()

frases = ("miaaau", "toma, tu gato gordo", "MIAU!", "prrr prrrr")

while 1:

    twts = api.search(q=["#gatogordo"], since_id=since)

    for status in twts:
        print (status.user.screen_name + ">> " + status.text + " ID: {}".format(status.id))
        api.update_status("@" + status.user.screen_name  + " " + URLs.gatos[random.randrange(0,URLs.gatos.__len__(),1)] + " " + frases[random.randrange(0,frases.__len__(),1)], in_reply_to_status_id=status.id)
        since = "{}".format(status.id)

    f = open(ID_sv, 'w')
    f.write("{}".format(since))
    f.close()
    time.sleep(60)


