#! /usr/bin/env bash
set -e

celery worker -A app.worker -l info -Q main-queue-upload,synchro-queue -c 1
