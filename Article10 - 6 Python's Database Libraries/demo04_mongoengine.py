from mongoengine import *
import datetime

connect('mydb')

class BlogPost(Document):
    title = StringField(required=True, max_length=200)
    posted = DateTimeField(default=datetime.datetime.utcnow)
    tags = ListField(StringField(max_length=50))
    meta = {'allow_inheritance': True}

class TextPost(BlogPost):
    content = StringField(required=True)

class LinkPost(BlogPost):
    url = StringField(required=True)

# Create a text-based post
post1 = TextPost(title='Using MongoEngine', content='See the tutorial')
post1.tags = ['mongodb', 'mongoengine']
post1.save()

# Create a link-based post
post2 = LinkPost(title='MongoEngine Docs', url='hmarr.com/mongoengine')
post2.tags = ['mongoengine', 'documentation']
post2.save()

# Iterate over all posts using the BlogPost superclass
for post in BlogPost.objects:
    print('===', post.title, '===')
    if isinstance(post, TextPost):
        print(post.content)
    elif isinstance(post, LinkPost):
        print('Link:', post.url)

# Count all blog posts and its subtypes
print(BlogPost.objects.count())
print(TextPost.objects.count())
print(LinkPost.objects.count())

# Count tagged posts
print(BlogPost.objects(tags='mongoengine').count())
print(BlogPost.objects(tags='mongodb').count())
