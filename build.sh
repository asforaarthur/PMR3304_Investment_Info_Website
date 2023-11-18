#!/bin/bash
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate

# Create superuser if not existing
DJANGO_SUPERUSER_USERNAME="your_superuser_username"
DJANGO_SUPERUSER_EMAIL="your_superuser_email@example.com"
DJANGO_SUPERUSER_PASSWORD="your_superuser_password"

python -c "import os; from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username=os.environ['DJANGO_SUPERUSER_USERNAME']).exists() or User.objects.create_superuser(os.environ['DJANGO_SUPERUSER_USERNAME'], os.environ['DJANGO_SUPERUSER_EMAIL'], os.environ['DJANGO_SUPERUSER_PASSWORD'])"

# Create or retrieve Group "Basic users"
python manage.py shell <<EOF
from django.contrib.auth.models import Group, Permission

# Attempt to retrieve the group or create it if it doesn't exist
group, created = Group.objects.get_or_create(name="Basic users")

# If the group was created, assign permissions
if created:
    permissions = Permission.objects.filter(codename__in=["add_user", "view_user", "add_list", "view_list", "add_comentario", "view_investment"])
    group.permissions.add(*permissions)
EOF
