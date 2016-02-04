from os import path
import subprocess
import logging

THIS_FOLDER = path.dirname(path.abspath(__file__))
logger = logging.getLogger(__name__)


def create_session_on_server(host, email):
    logger.info('create session: THIS_FOLDER=%s', THIS_FOLDER)
    return subprocess.check_output(
        [
            'fab',
            'create_session_on_server:email={}'.format(email),
            '--host={}'.format(host),
            '--hide=everything,status',
        ],
        cwd=THIS_FOLDER
    ).decode().strip()


def reset_database(host):
    logger.info('reset_database: THIS_FOLDER=%s', THIS_FOLDER)
    subprocess.check_call(
        ['fab', 'reset_database', '--host={}'.format(host)],
        cwd=THIS_FOLDER
    )
