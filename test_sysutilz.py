
import sysutilz

rpiZ = sysutilz.rpi()


cpu_usage = rpiZ.get_cpu_usage()
print('cpu usage = {}'.format(cpu_usage))
cpu_temp = rpiZ.get_cpu_temp()
print('cpu temp = {}'.format(cpu_temp))

mem_total = rpiZ.get_mem_total()
print('mem total = {}'.format(mem_total))
mem_available = rpiZ.get_mem_available()
print('mem avail = {}'.format(mem_available))
mem_used = rpiZ.get_mem_available()
print('mem used = {}'.format(mem_used))

disk_total = rpiZ.get_disk_total()
print('disk total = {}'.format(disk_total))
disk_used = rpiZ.get_disk_used()
print('disk used = {}'.format(disk_used))
disk_free = rpiZ.get_disk_free()
print('disk free = {}'.format(disk_free))
disk_percent = rpiZ.get_disk_percent()
print('disk percent = {}'.format(disk_percent))
