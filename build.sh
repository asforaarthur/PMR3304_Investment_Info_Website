
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

cat <<EOF | python manage.py shell
import os
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

User = get_user_model()

User.objects.filter(username=os.environ["DJANGO_SUPERUSER_USERNAME"]).exists() or \
    User.objects.create_superuser(os.environ["DJANGO_SUPERUSER_USERNAME"], os.environ["DJANGO_SUPERUSER_EMAIL"], os.environ["DJANGO_SUPERUSER_PASSWORD"])

g = Group(name="Basic users")
g.save()
g.permissions.set([Permission.objects.get(codename=c) for c in ["add_user","view_user","add_list","view_list", "add_comentario", "view_investment"]])
Group.objects.filter(name="Basic users").exists() or g.save()
EOF