#
# 
#

import logging
import argparse
import sys

def main():
    logger.info("-" * 50)
    logger.info("          Script Name here")
    logger.info("-" * 50)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Describe your script')
    parser.add_argument('-v', '--verbosity', type=int, default=1, help='Select output level: 0: WARNING, 1: INFO, 10: DEBUG')
    args = parser.parse_args()

    # Log Settings
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Handle the log file
    log_file = "script.log"
    handler = logging.FileHandler(log_file, mode='w')
    handler.setLevel(logging.DEBUG)

    # Create the Logginf Format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Create a handle for stdout as well
    handler2 = logging.StreamHandler(sys.stdout)
    handler2.setLevel(logging.INFO)
    if (args.verbosity == 0):
        handler2.setLevel(logging.WARNING)
    elif (args.verbosity > 9):
        handler2.setLevel(logging.DEBUG)

    formatter2 = logging.Formatter('[-] %(message)s')
    handler2.setFormatter(formatter2)

    # agregar hanldes a logger
    logger.addHandler(handler)
    logger.addHandler(handler2)
    logger.info('Log file: %s\n' %log_file)
    logger.debug('Verbosity Level Selected: %i' %args.verbosity)

    # call main code
    main()