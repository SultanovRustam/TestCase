from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name='Имя')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name


class Source(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name='Имя')
    link = models.URLField(max_length=200,
                           verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'

    def __str__(self):
        return self.name


class Post(models.Model):
    content = models.TextField()
    popularity = models.IntegerField()
    source = models.ForeignKey(Source,
                               on_delete=models.CASCADE,
                               related_name='posts')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.content


class Subscription(models.Model):
    name = models.CharField(max_length=255)
    source = models.ForeignKey(Source,
                               on_delete=models.CASCADE,
                               related_name='subscriptions')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='subscriptions')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.name} для {self.user}'


class Digest(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='users')
    posts = models.ManyToManyField(Post)

    class Meta:
        verbose_name = 'Дайжест'
        verbose_name_plural = 'Дайжесты'

    def __str__(self):
        return f'Дайджест для {self.user.name}'
