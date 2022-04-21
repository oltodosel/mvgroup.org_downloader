#!/usr/bin/env python

import re, os, time
import requests

# Downloads new torrents to a given ./path
# Gets torrents from both MAIN TRACKER and FORUM TRACKER

# Official RSS has been broken for over a month as of 21.04.2022 and admins don't do anything about it - https://forums.mvgroup.org/index.php?showtopic=92565

# cron:
# 5 */8 * * * python3 ~/.scripts/mvgroup.org.py

##########################################

LOGIN = 'zxc'
PASSWORD = 'zxc'
path_to_save_torrent_files = os.path.expanduser('~/d/')
# file that stores the list of already downloaded torrents
path_seen = os.path.expanduser('~/.scripts/mvgroup.org.seen')

##########################################

try:
    seen = [ x.strip() for x in open(path_seen).readlines() if len(x.strip()) ]
except:
    seen = []

os.makedirs(path_to_save_torrent_files, exist_ok=True)

data = {
    'act': 'Login',
    'CODE': '01',
    'UserName': LOGIN,
    'PassWord': PASSWORD,
}

response = requests.post('https://forums.mvgroup.org/index.php', data=data)
cc = response.cookies.get_dict()

FT = requests.get(url = 'https://forums.mvgroup.org/forumtracker.php?orderby=added&order=DESC&', cookies = cc).text
MT = requests.get(url = 'https://forums.mvgroup.org/maintracker.php?orderby=added&order=DESC&', cookies = cc).text

torrents = re.findall('<a class="torrentlink" href="(.*?)">', FT) + re.findall('<a class="torrentlink" href="(.*?)">', MT)

for torrent in torrents:
	torrent_link = 'https://forums.mvgroup.org' + torrent[1:]
	torrent_name = torrent.split('/')[-1]
	
	if torrent_link not in seen:
		print(torrent_name)
		torrent_file = requests.get(url = torrent_link).content

		f = open(path_to_save_torrent_files + '/' + torrent_name, 'wb')
		f.write(torrent_file)
		f.close()

		print(torrent_link, file=open(path_seen, 'a'))

		time.sleep(.5)
	