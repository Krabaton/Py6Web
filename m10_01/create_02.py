from models import Post, LinkPost, TextPost, ImagePost, User

steve = User(email='steve@example.com', first_name='Steve', last_name='Buscemi').save()

post1 = ImagePost(title='Node.js the best', author=steve)
post1.image_path = 'https://web-creator.ru/uploads/Page/22/nodejs.svg'
post1.tags = ['node', 'js']
post1.save()
