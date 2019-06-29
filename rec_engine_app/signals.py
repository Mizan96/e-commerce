from django.dispatch import Signal

user_preference_signals = Signal(providing_args=['request'])