from django.db import models
from django.db.models.signals import (
    post_delete, post_save, pre_save, pre_delete
)
from django.dispatch import receiver
from django.core.mail import send_mail, send_mass_mail
from django.core.cache import cache

from .transliterator import my_slugify
from .email import email_template


class BooksModel(models.Model):
    title = models.CharField('Title', max_length=150)
    slug = models.CharField('Slug', max_length=255, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


@receiver(pre_save, sender=BooksModel)
def book_pre_created_or_saved(sender, instance, **kwargs):
    instance.slug = my_slugify(instance.title)


@receiver(post_save, sender=BooksModel)
def book_created_or_saved(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject=email_template.new_book['subject'],
            message=email_template.new_book['message'],
            from_email=email_template.from_email,
            recipient_list=email_template.recipient_list,
            fail_silently=False,
            html_message=email_template.new_book['html_message'],
        )
        instance.save()
    else:
        message1 = (
            email_template.saved_book['subject'],
            email_template.saved_book['html_message'],
            email_template.from_email,
            email_template.recipient_list,
        )
        message2 = (
            email_template.testing_message['subject'],
            email_template.testing_message['html_message'],
            email_template.from_email,
            email_template.recipient_list.append(email_template.testing_email),
        )
        send_mass_mail((message1, message2), fail_silently=False)
    cache.set('book::%(id)d' % {'id': instance.id}, instance)


@receiver(post_delete, sender=BooksModel)
def book_deleted(sender, instance, **kwargs):
    send_mail(
        subject=email_template.deleted_book['subject'],
        message=email_template.deleted_book['message'],
        from_email=email_template.from_email,
        recipient_list=email_template.recipient_list,
        fail_silently=False,
        html_message=email_template.deleted_book['html_message'],
    )
    cache.delete('book::%(id)d' % {'id': instance.id})
