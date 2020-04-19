import time

from src.helper import log, env
from src.scheduler import scheduler


if __name__ == '__main__':
    try:
        log.info('auto-factorial was born!')
        if not env.is_development():
            scheduler.scheduler.start()
        else:
            log.info('Running jobs manually since DEVELOPMENT MODE is enabled, and then sleep eternally.')
            scheduler.run()
            while True:
                time.sleep(1000)

    except Exception as e:
        log.error(f'Unexpected error {e} in auto-factorial')
        log.exception(e)

    finally:
        log.info('Rest in peace, auto-factorial.')
