from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# 定制自己的查询管理器,继承自系统的管理器
class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset()\
            .filter(status='published')


# 文章模型
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    #  标题
    title = models.CharField(max_length=250)

    # 构建url的字符
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')

    # 正文
    body = models.TextField()
    # 发布时间
    publish = models.DateTimeField(default=timezone.now)
    # 创建时间
    created = models.DateTimeField(auto_now_add=True)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    objects = models.Manager()  # 默认的管理器
    published = PublishManager()  # 我们的管理器

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    # 文章模型的绝对路径
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])
