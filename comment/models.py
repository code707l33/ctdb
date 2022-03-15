from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.utils import today


class Comment(models.Model):
    post_date = models.DateField(verbose_name=_('Date'), default=today)
    post_choice = (('share',_('share')), ('discuss',_('discuss')), ('help',_('help')), ('message',_('message')))
    post_type = models.CharField(
        verbose_name=_('Post type'),
        max_length=15, 
        choices=post_choice, 
        default='message'
        )
    post_title = models.TextField(verbose_name=_('Title'), null=False)
    comment = models.TextField(verbose_name=_('Post Comment'), blank=True)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-post_date']
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def get_create_url(self):
        return reverse('comment:comment_create')

    def get_update_url(self):
        return reverse('comment:comment_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('comment:comment_delete', kwargs={'pk': self.pk})
    
    def get_message_url(self):
        return reverse('comment:comment_message_list', kwargs={'pk': self.pk})


class CommentMessage(models.Model):
    message_date = models.DateField(verbose_name=_('Date'), default=today)
    message_post = models.ForeignKey(to='comment', on_delete=models.CASCADE)
    message_content = models.TextField(verbose_name=_('Message'), blank=True)
    message_create_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-message_date']
    
    def __str__(self):
        return self.message_post
    
    def get_create_url(self):
        return reverse('comment_message:comment_message_create')

    def get_update_url(self):
        return reverse('comment_message:comment_message_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('comment_message:comment_message_delete', kwargs={'pk': self.pk})

