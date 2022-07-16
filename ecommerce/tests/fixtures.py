import pytest
from django.contrib.auth.models import User 
from django.core.management import call_command

# This file gonna run and utilize, because of we include it inside of "conftest.py"
@pytest.fixture
def create_admin_user(django_user_model):
    """
    Return admin user
    """
    return django_user_model.objects.create_superuser("asdmin", "asdmin@gmail.com", "asdFasdf")

@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup,  django_db_blocker):
    """
    Load DB data fixtures
    """
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")