import os
import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_project.settings")
django.setup()

from .models import User, Post
from django.utils import timezone
import random

fake = Faker()

def generate_fake_users(num_users=10):
    for _ in range(num_users):
        username = fake.user_name()
        email = fake.email()
        bio = fake.text()
        joined_at = fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)
        age = random.randint(18, 100)  # Generate a random age between 18 and 100
        User.objects.create(username=username, email=email, bio=bio, joined_at=joined_at, age=age)

def generate_fake_posts(num_posts=20):
    users = User.objects.all()
    for _ in range(num_posts):
        user = random.choice(users)
        post_text = fake.text()
        created_at = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
        Post.objects.create(user=user, post=post_text, created_at=created_at)

generate_fake_users()
generate_fake_posts()
print('alles gut')
