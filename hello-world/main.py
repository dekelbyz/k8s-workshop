from time import sleep

# configure logginglogs_format = '[%(asctime)s] %(levelname)s - %(message)s'logger = logging.getLogger()# this is needed in order to see the logs through K8s logs# '/proc/1/fd/1' file is functioning as the Pod's STDOUT.handler = logging.FileHandler('/proc/1/fd/1', mode='w')logger.setLevel(logging.DEBUG)formatter = logging.Formatter(logs_format)handler.setFormatter(formatter)logger.addHandler(handler)
while True:
    print('Hello World!!!')
    sleep(5)
