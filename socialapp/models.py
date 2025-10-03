from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return self.caption
    

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.text:
            self.post.comment_count += 1
            self.post.save()    
        super().save(*args, **kwargs)


    def __str__(self):
        return f'Comment on {self.post.caption} at {self.created_at}'
    

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    like = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.like:
            self.post.like_count += 1
            self.post.save()    
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Like on {self.post.caption} at {self.created_at}'