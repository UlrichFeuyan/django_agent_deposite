#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py loaddata agent_deposit/fixtures/theme.json
python manage.py loaddata agent_deposit/fixtures/auth.json
python manage.py loaddata agent_deposit/fixtures/agent_deposit.json
