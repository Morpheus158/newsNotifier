import feedparser
from win10toast import ToastNotifier
import time

toast = ToastNotifier()
url = r"https://www.aktualne.cz/rss/"
old_feed = ""

while True:
  feed = feedparser.parse(url)
  new_feed = feed.entries[0].title
  
  if new_feed == old_feed:
    False
  else:
    toast.show_toast("Aktuální zprávy",new_feed)

  old_feed = new_feed
  time.sleep(60)