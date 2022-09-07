from models import Post, LinkPost, TextPost, ImagePost, User

_id = '6318de7af9767e9feb6ae7ef'

post = Post.objects(id=_id)
post.update(link_url='http://docs.mongoengine.org/')

print(post)

for p in post:
    # print(p.title, p.link_url)
    print(p.to_mongo().to_dict())
    