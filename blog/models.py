from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " | " + self.post.__str__() + " | " + self.timestamp.__str__()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Category(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_blog.jpg', upload_to='blog_pics')
    categories = models.ManyToManyField(Category)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()


