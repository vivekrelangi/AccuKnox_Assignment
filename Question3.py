"""Answer: Yes, by default, Django signals run in the same database transaction as the caller if the signals are triggered inside a transaction block. If the transaction is rolled back, the changes made by the signal will also be rolled back. In the below code, even though the signal handler changes the username to "modified_user" and saves it, the entire transaction is rolled back due to the exception. As a result, the change made by the signal handler is also rolled back, which confirms that signals run in the same transaction.
"""
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal started")
    instance.username = "modified_user"
    instance.save()  # This save is part of the same transaction
    print("Signal finished")

# views.py
from django.contrib.auth.models import User
from django.db import transaction

def create_user(request):
    try:
        with transaction.atomic():
            user = User.objects.create(username="new_user")  # This triggers the post_save signal
            raise Exception("Some error")  # Simulating an exception to rollback the transaction
    except:
        pass

    print(User.objects.filter(username="modified_user").exists())  # Should print False

# Output:
# Signal started
# Signal finished
# False
