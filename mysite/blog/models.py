from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# 定制自己的管理器
class PublishedManger(models.Model):
    def get_queryset(self):
        return super(PublishedManger, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = {
        ('draft', 'Draft'),
        ('published', 'Published')
    }
    # 转为varchar
    title = models.CharField(max_length=250)
    # 构建url用的
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    # 转为text
    body = models.TextField()
    # 创建时间
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    objects = models.Manager()
    published = PublishedManger()

    class Meta:
        # 查询数据库时按这个字段降序排列
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year, self.publish.strftime('%m'),
                             self.publish.strftime('%d'), self.slug])
