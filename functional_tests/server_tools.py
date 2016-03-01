from os import path
import subprocess
import logging
from urllib.parse import urlparse
#import sys
# the mock-0.3.1 dir contains testcase.py, testutils.py & mock.py
#sys.path.append('/usr/local/lib/python2.7/site-packages')
#from fabric.api import env
logging.basicConfig(level=logging.INFO)

THIS_FOLDER = path.dirname(path.abspath(__file__))
logger = logging.getLogger("server-tools-local")
ssh_port = '9055'

def create_session_on_server(host, email):
    logger.info('create session: THIS_FOLDER=%s', THIS_FOLDER)
    parsed = host.split("@")[1]
    parsed = parsed.split(":")[0]
    return subprocess.check_output(
        [
            'fab',
            'create_session_on_server:email={}'.format(email),
#            '--host={}'.format(host),
#            '--host={}'.format('superlists-staging.par7en.com'),
            '--host={}:{}'.format(parsed, ssh_port),
#            '-i{}'.format('~/.ssh/id_rsa_par7en'),
            '-i',
            '~/.ssh/id_rsa_par7en',
            '--hide=everything,status',
        ],
        cwd=THIS_FOLDER
    ).decode().strip()


def reset_database(host):
    logger.info('reset_database: THIS_FOLDER=%s', THIS_FOLDER)
    logger.info('host: %s', host)
    parsed = host.split("@")[1]
    parsed = parsed.split(":")[0]
    logger.info('parsed: %s', parsed)
    subprocess.check_call(
        [
            'fab',
            'reset_database',
#            '--host={}'.format(host),
#            '--host={}'.format('superlists-staging.par7en.com'),
            '--host={}:{}'.format(parsed, ssh_port),
            '-i',
            '~/.ssh/id_rsa_par7en',
#            '--show=debug',

        ],
            cwd=THIS_FOLDER
    )
