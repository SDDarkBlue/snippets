import time
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

def run():
    s = 0
    logging.debug('   start counting')
    for i in range(50000000):
        s += i
    logging.debug('   finished counting')

def main():
    for i in range(10):
        logging.debug("starting thread {0}".format(i))
        t = threading.Thread(target=run)
        t.start()
        #t.join()
        logging.debug("{0} done".format(i))
    threads_running = True
    while threads_running:
        running_threads = threading.enumerate()
        logging.debug('running threads: {0}'.format(len(running_threads)))
        if len(running_threads) == 1:
            threads_running = False
        time.sleep(2)


main()
