import threading
import os
import psutil


def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


class rpi(object):
    """ A class to return info about how the pi is performning """

    def __init__(self):
        self._lock = threading.Lock()

    def get_cpu_temp(self):
        with self._lock:
            temp = os.popen("vcgencmd measure_temp").readline()
            Celsius = float(temp.replace("temp=", "").replace("'C", ""))
            # (C * 9/5) + 32 = F
            Fahrenheit = 9.0 / 5.0 * Celsius + 32
            return Fahrenheit

    def get_cpu_usage(self):
        with self._lock:
            # cpu = psutil.cpu_percent()
            cpu = psutil.cpu_percent(interval=1)
            return cpu

    def get_disk_total(self):
        with self._lock:
            disk = psutil.disk_usage('/')
            disk_total = disk.total / 2**30     # GiB.
            return disk_total

    def get_disk_used(self):
        with self._lock:
            disk = psutil.disk_usage('/')
            disk_used = disk.used / 2**30
            return disk_used

    def get_disk_free(self):
        with self._lock:
            disk = psutil.disk_usage('/')
            disk_free = disk.free / 2**30
            return disk_free

    def get_disk_percent(self):
        with self._lock:
            disk = psutil.disk_usage('/')
            disk_percent = disk.percent
            return disk_percent

    def get_mem_total(self):
        with self._lock:
            mem = psutil.virtual_memory()
            return bytes2human(mem.total)

    def get_mem_available(self):
        with self._lock:
            mem = psutil.virtual_memory()
            return bytes2human(mem.available)

    def get_mem_used(self):
        with self._lock:
            mem = psutil.virtual_memory()
            return bytes2human(mem.used)
