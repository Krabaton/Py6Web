from models import Post, LinkPost, TextPost, ImagePost, User

_id = '6318e0ca1344bce24e48acdd'

post = Post.objects(id=_id)
print(post.delete())

