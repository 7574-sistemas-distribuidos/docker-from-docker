import logging
import subprocess
import os
import sys
import time

SLEEP_SECONDS = 10
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    while True:
        result = subprocess.run(['docker', 'stop', 'dockerfromdocker_nginx_1'], check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info('Command executed. Result={}. Output={}. Error={}'.format(result.returncode, result.stdout, result.stderr))
        
        result = subprocess.run(['docker', 'ps'], check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info('Command executed. Result={}. Output={}. Error={}'.format(result.returncode, result.stdout, result.stderr))
        time.sleep(SLEEP_SECONDS)

        result = subprocess.run(['docker', 'start', 'dockerfromdocker_nginx_1'], check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info('Command executed. Result={}. Output={}. Error={}'.format(result.returncode, result.stdout, result.stderr))

        result = subprocess.run(['docker', 'ps'], check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info('Command executed. Result={}. Output={}. Error={}'.format(result.returncode, result.stdout, result.stderr))
        time.sleep(SLEEP_SECONDS)