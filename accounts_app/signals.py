from django.dispatch import Signal

create_shipping_profile = Signal(providing_args=['instance'])