# AccuKnox_Assignment
Created to post answers for an assignment.

To run the codes in Question1.py, Question2.py and Question3.py files, you need to follow these steps:

### **Prerequisites:**
- Make sure you have Python and Django installed on your system.
- Create a Django project and a Django app.

### **Step-by-step Procedure:**

#### **1. Install Python and Django:**

If you don't have Python and Django installed, you can install them as follows:

- **Install Python**:
  Download Python from [here](https://www.python.org/downloads/) and follow the instructions for your platform.

- **Install Django**:
  You can install Django using pip:
  ```bash
  pip install django
  ```

#### **2. Create a Django Project and App:**

1. **Create a new Django project:**
   ```bash
   django-admin startproject myproject
   cd myproject
   ```

2. **Create a new Django app (for example, `myapp`):**
   ```bash
   python manage.py startapp myapp
   ```

3. **Add the app (`myapp`) to your `INSTALLED_APPS`** in `myproject/settings.py`:
   ```python
   INSTALLED_APPS = [
       # Other installed apps
       'myapp',
   ]
   ```

#### **3. Define the Signal Code:**

1. **Create a file `signals.py` inside your app directory (`myapp`):**

Place the following content inside `myapp/signals.py` (replace with the corresponding code from my first response):

```python
# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

# Example for Question 1 (Synchronous Signals)
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)  # Simulating a long-running task
    print("Signal finished")
```

2. **Connect the signal in the `apps.py` of your app:**

In `myapp/apps.py`, modify the `MyappConfig` class to include the signal registration:

```python
# myapp/apps.py
from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.signals  # Import signals here
```

#### **4. Add the View:**

1. **Create the view for testing the signal in `myapp/views.py`:**

```python
# myapp/views.py
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_user(request):
    print("Before user creation")
    user = User.objects.create(username="new_user")  # This triggers the post_save signal
    print("After user creation")
    return HttpResponse("User created!")
```

2. **Add a URL route to access the view in `myapp/urls.py`:**

Create a `urls.py` file in the `myapp` directory if it doesn’t exist, and add the following content:

```python
# myapp/urls.py
from django.urls import path
from .views import create_user

urlpatterns = [
    path('create-user/', create_user),
]
```

3. **Include `myapp` URLs in the project's `urls.py` file:**

In `myproject/urls.py`, include the app’s URL:

```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

#### **5. Migrate and Run the Django Server:**

1. **Make migrations and migrate:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Create a superuser (for accessing the admin panel if needed):**
   ```bash
   python manage.py createsuperuser
   ```

3. **Run the Django development server:**
   ```bash
   python manage.py runserver
   ```

#### **6. Test the Example:**

1. Open a browser and go to:
   ```
   http://127.0.0.1:8000/create-user/
   ```

   This will trigger the `create_user` view, which creates a user and fires the `post_save` signal. You should see the printed output from the signal handler in the terminal running the Django server.

   You’ll see:
   ```
   Before user creation
   Signal started
   (5 seconds delay)
   Signal finished
   After user creation
   ```

This process will allow you to run the codes in Question1.py, Question2.py and Question3.py files, demonstrating how signals in Django behave when executed synchronously, in the same thread, and within the same database transaction.
