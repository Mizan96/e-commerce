from django.dispatch import Signal

create_billing_info = Signal(providing_args=['instance'])