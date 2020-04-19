import time

from src import scheduler
from src.helper import log, env


if __name__ == '__main__':
    try:
        log.info('auto-factorial was born!')
        if not env.is_development():
            scheduler.scheduler.start()
        else:
            log.info('Running jobs manually since DEVELOPMENT MODE is enabled, and then sleep eternally.')
            scheduler.auto_factorial_cron_job()
            while True:
                time.sleep(1000)

    except Exception as e:
        log.error(f'Unexpected error {e} in auto-factorial')
        log.exception(e)

    finally:
        log.info('Rest in peace, auto-factorial.')
