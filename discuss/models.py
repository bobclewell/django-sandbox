from django.db import models

class TopicManager(models.Manager):
    def create_topic(self, title, description):
        topic = self.create(
            title=title,
            description=description
        )
        return topic


class Topic(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    objects = TopicManager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text
