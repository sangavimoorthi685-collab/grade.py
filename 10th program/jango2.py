from django.conf import settings
import django

settings.configure(
    DEBUG=True,
    SECRET_KEY="123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"]
)

django.setup()

from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("""
    <h1>Employee Management</h1>
    <form>
    Name: <input type="text"><br><br>
    Salary: <input type="number"><br><br>
    Department: <input type="text"><br><br>
    <button>Add Employee</button>
    </form>
    """)

urlpatterns = [path("", home)]

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "employee.py", "runserver", "8007"
    ])