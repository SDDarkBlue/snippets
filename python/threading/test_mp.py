import time
from multiprocessing import Pool
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

def run(x):
    s = 0
    logging.debug('   start counting')
    for i in range(50000000):
        s += i
    print x
    logging.debug('   finished counting')

def main():
    logging.debug('starting pool')
    p = Pool(processes=10)
    p.map(run, [['a', 1], ['b', 2], ['c', 3]])
    logging.debug('pool finished')

main()
