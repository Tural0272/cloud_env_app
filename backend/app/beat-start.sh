#! /usr/bin/env bash
set -e

celery -A app.worker beat --loglevel=debug --pidfile=/tmp/celerybeat.pid