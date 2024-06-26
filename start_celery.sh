#!/bin/bash
source .venv/bin/activate
nohup celery -A app.mycelery worker --loglevel=info &


