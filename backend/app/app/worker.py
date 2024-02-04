from raven import Client

from celery.schedules import crontab

from app.core.celery_app import celery_app
from app.core.config import settings

from scheduler import upload_synchronization, database_update

client_sentry = Client(settings.SENTRY_DSN)


@celery_app.task(acks_late=True)
def test_celery(word: str) -> str:
    return f"test task return {word}"

@celery_app.task(acks_late=True)
def upload_auftrag(session_id: int) -> str:
    response = upload_synchronization(session_id)
    return f"{response.ok}"

@celery_app.task
def update():
    database_update()
    return f"True"