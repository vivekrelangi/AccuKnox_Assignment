"""Answer: By default, Django signals are executed synchronously. This means that the signal handlers are called immediately in the same flow of execution, and they block further execution of the code until they finish. In the below code, when User.objects.create is called, the post_save signal is triggered synchronously, and the execution of the view is blocked until the signal handler finishes its execution. The After user creation print statement will only appear after the signal handler completes."""

# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)  # Simulating a long-running task
    print("Signal finished")

# views.py
from django.contrib.auth.models import User

def create_user(request):
    print("Before user creation")
    user = User.objects.create(username="new_user")  # This triggers the post_save signal
    print("After user creation")

# Output:
# Before user creation
# Signal started
# (5 seconds delay)
# Signal finished
# After user creation
