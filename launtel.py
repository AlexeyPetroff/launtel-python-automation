import argparse
import logging
import re
import sys
import os
import requests

BASE_URL = 'https://residential.launtel.net.au'

logging.basicConfig(
    format='%(asctime)s:%(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %I:%M:%S%p',
    level=logging.DEBUG,
    stream=sys.stdout)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', metavar='action', help='`pause` or `unpause`', choices=['pause', 'unpause'],
                        type=str.lower)
    return parser.parse_args()


def login(email, password):
    session = requests.Session()
    data = {'username': email, 'password': password}
    response = session.post(f'{BASE_URL}/login', data=data)
    response.raise_for_status()
    logging.info('Login successful')
    service_id = int(re.search(r'onclick=\"pauseService\((\d+),', response.text).group(1))
    return session, service_id


def change_service_status(action):
    session, service_id = login(os.environ['LAUNTEL_EMAIL'], os.environ['LAUNTEL_PASSWORD'])
    response = session.post(f'{BASE_URL}/service_{action}/{service_id}')
    response.raise_for_status()
    logging.info(f'Service has been {action}d')


if __name__ == '__main__':
    args = parse_args()
    change_service_status(action=args.action)
