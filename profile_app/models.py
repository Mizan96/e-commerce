from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from profile_app.signals import object_viewed_signals

class ObjectViewed(models.Model):
    user            = models.ForeignKey(User)
    ip_address      = models.CharField(max_length=220, null=True, blank=True)
    content_type    = models.ForeignKey(ContentType)
    obj_id          = models.PositiveIntegerField()
    content_object  = GenericForeignKey('content_type', 'obj_id')
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s viewed on %s" %(self.content_object, self.timestamp)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'

def object_viewed_signals_receiver(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender)
    if request.user.is_authenticated():
        ObjectViewed.objects.create(
            user=request.user,
            content_type = c_type,
            obj_id = instance.id
            )

object_viewed_signals.connect(object_viewed_signals_receiver)