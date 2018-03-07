#!/usr/bin/env python
'''Snapshot script'''
# pylint: disable=invalid-name
import json
import time
from datetime import datetime
import psutil
import config

class Snapshot:
    '''Snapshot class'''
    def __init__(self):
        self.cpu = None
        self.mem = None
        self.swap = None
        self.disk = None
        self.net = None
        self.time = None
        self.counter = 0

    def get(self):
        '''get function'''
        self.cpu = str((psutil.cpu_percent(interval=None)))
        self.mem = str((psutil.virtual_memory().used))
        self.swap = str((psutil.swap_memory().used))
        self.disk = str((psutil.disk_io_counters().read_count))
        self.net = str((psutil.net_io_counters().bytes_sent))
        self.counter += 1
        self.time = str(datetime.now())


    def wr_txt(self):
        '''write to txt file'''
        fil = open("myfile", "a")
        fil.write("SNAPSHOT " + str(self.counter))
        fil.write(" " + self.time + "\n")
        fil.write("\tCPU percent: " + self.cpu + "\n")
        fil.write("\tMemory Usage: " + self.mem + "\n")
        fil.write("\tSWAP Usage: " + self.swap + "\n")
        fil.write("\tDisk read: " + self.disk + "\n")
        fil.write("\tNet sent: " + self.net + "\n")
        fil.close()

    def wr_json(self):
        '''write to json file'''
        jsn_dict = {'Snapshot': str(self.counter), 'Time': self.time,
                    'CPU': self.cpu, 'Memory': self.mem, 'SWAP': self.swap,
                    'Disk': self.disk, 'Net': self.net}
        fil = open("myjson", "a")
        json.dump(jsn_dict, fil, indent=4, ensure_ascii=False)
        fil.close()


test = Snapshot()
while True:
    test.get()
    if config.f_type == "txt":
        test.wr_txt()
    else:
        test.wr_json()
    if test.counter >= config.checks:
        break
    time.sleep(config.sleep)
