from django.db import models
from django.contrib.auth.models import User
from rec_engine_app.signals import user_preference_signals
from rec_engine_app.utils import preference_calculation

class UserPreferenceManager(models.Manager):

    def new(self, request, prefer_type):
        qs = UserPreference.objects.filter(user=request.user)
        if qs.count() > 0:
            get_info = qs.first()
            get_info.prefer_type = int(prefer_type)
            get_info.save()
        else:
            UserPreference.objects.create(user = request.user,
                                          prefer_type = int(prefer_type))


class UserPreference(models.Model):
    user        = models.ForeignKey(User)
    prefer_type = models.IntegerField() 
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    objects     = UserPreferenceManager()

    def __str__(self):
        return str(self.prefer_type)

def user_prefer_calc(sender, request, *args,**kwargs):
    prefer_type = preference_calculation(request)
    UserPreference.objects.new(request, prefer_type)

user_preference_signals.connect(user_prefer_calc)
