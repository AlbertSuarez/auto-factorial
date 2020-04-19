from apscheduler.schedulers.blocking import BlockingScheduler

from src.config import CRON_TYPE, CRON_DAY_OF_WEEK
from src.cron import runner
from src.helper import env
from src.helper.timer import Timer

scheduler = BlockingScheduler()


@scheduler.scheduled_job(CRON_TYPE, day_of_week=CRON_DAY_OF_WEEK, hour=env.get_start_hour())
def auto_factorial_cron_job():
    with Timer(auto_factorial_cron_job.__name__):
        runner.run()
