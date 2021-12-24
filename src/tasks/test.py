from src.app import create_worker_app
from src.extensions import celery

app = create_worker_app()


@celery.task(
    default_retry_delay=600,
    retry_backoff=True,
    retry_kwargs={'max_retries': 5},
    queue='test'
)
def sayhi():
    print("Hello")


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls reverse_messages every 10 seconds.
    # sender.add_periodic_task(10.0, reverse_messages, name="reverse every 10")
    #
    # # Calls log('Logging Stuff') every 30 seconds
    # sender.add_periodic_task(30.0, log.s(("Logging Stuff")), name="Log every 30")
    #
    # # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1), log.s("Monday morning log!"),
    # )
    print("Bye")


sayhi.delay()