from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    SOCIAL_CHOICES = [
        ('twitter', 'Twitter / X'),
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn'),
        ('facebook', 'Facebook'),
        ('youtube', 'YouTube'),
        ('tiktok', 'TikTok'),
        ('threads', 'Threads'),
        ('blog', 'Blog / Artículo'),
        ('podcast', 'Podcast'),
        ('libro', 'Libro'),
        ('otro', 'Otro'),
    ]

    text = models.TextField()
    author = models.CharField(max_length=200)
    link = models.URLField(blank=True, default='')
    source = models.CharField(max_length=20, choices=SOCIAL_CHOICES, default='otro')
    source_custom = models.CharField(max_length=100, blank=True, default='')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author} — {self.text[:60]}"

    def get_source_display_name(self):
        if self.source == 'otro' and self.source_custom:
            return self.source_custom
        return self.get_source_display()
