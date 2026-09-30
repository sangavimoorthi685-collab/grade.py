from django.conf import settings
import django

settings.configure(
    DEBUG=True,
    SECRET_KEY="123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
)

django.setup()

from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("""
    <h1>Book Management</h1>
    <form>
    Book Name: <input type="text"><br><br>
    Author: <input type="text"><br><br>
    <button>Add Book</button>
    </form>
    """)

urlpatterns = [
    path("", home),
]

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "program13.py", "runserver", "0.0.0.0:8002"
    ])