"""Yes, by default, Django signals run in the same thread as the caller. In the below code, both the caller (the create_user view) and the signal handler run in the same thread, as indicated by the same thread ID printed in the output."""

# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal thread ID: {threading.get_ident()}")

# views.py
from django.contrib.auth.models import User
import threading

def create_user(request):
    print(f"Caller thread ID: {threading.get_ident()}")
    user = User.objects.create(username="new_user")

# Output:
# Caller thread ID: 140375623014144
# Signal thread ID: 140375623014144
