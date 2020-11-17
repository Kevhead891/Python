from __future__ import print_function
import time
import random
import binascii
import ftd2xx
from xlwt import Workbook

dev_num = ftd2xx.createDeviceInfoList()

#Print the information of the devices
for i in range (0,dev_num):
    print(ftd2xx.getDeviceInfoDetail(i))


  # Open Device using serial number
d = ftd2xx.openEx(b'DP52HZZZA')

d.setTimeouts(1000, 1000)
# init = int("0xAA",0)
# init_dat = (bytes([init]))
#
#
# d.write(init_dat)

raw = (bytes([int("0xAF", 0)]))
proc = (bytes([int("0xAE", 0)]))
init = (bytes([int("0xAA", 0)]))

d.purge(ftd2xx.defines.PURGE_TX | ftd2xx.defines.PURGE_RX)
d.write(init)
#d.purge(ftd2xx.defines.PURGE_TX | ftd2xx.defines.PURGE_RX)
d.write(raw)
#d.write(raw)
# time.sleep(0.1)
#
# d.write(proc)
# time.sleep(0.1)
# d.write(proc)

time.sleep(0.1)
num_reads = 512
rx_data = d.read(num_reads)
#
# d.write(raw)
# rx_data2= (d.read(128))
#
# time.sleep(0.1)
#
rx = list(rx_data)
# rx.extend(rx_data2)
print(rx_data)
# print(rx_data2)
# print(rx)
print(len(rx))
print('[{}]'.format(', '.join(hex(element) for element in rx)))

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, "RAW_DATA")


for i in range(0,num_reads):
    #print(hex(rx[i]))
    sheet1.write((i+1) , 0, hex(rx[i]))

wb.save('fifo2.xls')

d.close()



