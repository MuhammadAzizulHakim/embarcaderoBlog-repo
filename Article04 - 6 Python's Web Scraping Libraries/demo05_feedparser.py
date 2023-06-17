import feedparser

d = feedparser.parse('http://stackoverflow.com/feeds')

print(d.feed.title)
print(d.feed.title_detail)
print(d.feed.link)
print(d.entries)