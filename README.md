Downloads new torrents to a given ./path  
Gets torrents from both MAIN TRACKER and FORUM TRACKER

Official RSS has been broken for over a month as of 21.04.2022 and admins don't do anything about it - https://forums.mvgroup.org/index.php?showtopic=92565

### Edit `LOGIN` and `PASSWORD` in `mvgroup.org.py`
```
cron:   
5 */8 * * * python3 ~/.scripts/mvgroup.org.py
```
