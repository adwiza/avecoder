import logging


extra_data = {'user': 'adwiz@suroviy.ru'}


def debug_log():
    logging.debug('Here is a debug-level log message', extra=extra_data)


def main():

    dateStr = '%m/%d/%Y %I:%M:%S %p'
    fmtstr = 'User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s line:%(lineno)d %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        filename='log_output.log',
                        filemode='w',
                        format=fmtstr,
                        datefmt=dateStr
                        )

    # logging.debug('Here is a debug-level log message')
    logging.info('Here is an info-level log message', extra=extra_data)
    logging.warning('Here is a warning-level log message', extra=extra_data)
    # logging.critical('Here is a critical-level message')

    # logging.warning(f'Here is a variable {"String"} and an int: {42}')
    debug_log()


if __name__ == '__main__':
    main()
