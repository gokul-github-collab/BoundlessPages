from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    about = models.CharField(max_length=600, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    excert = models.CharField(max_length=300)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    content = models.TextField()
    slug = models.SlugField(null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.title}"


class Comment(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    text = models.TextField()
    post = models.ForeignKey(Post,  on_delete=models.CASCADE, related_name="comments")
