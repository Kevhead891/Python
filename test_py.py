from __future__ import print_function
import time
import random
import binascii
import ftd2xx
import random
import xlwt
from xlwt import Workbook
import serial #needed to communicate with serial communications


#ser = serial.Serial(port = 'COM5', baudrate = 19200)
time.sleep(1)
# #Find number of devices connected
dev_num = ftd2xx.createDeviceInfoList()

#Print the information of the devices
for i in range (0,dev_num):
    print(ftd2xx.getDeviceInfoDetail(i))


  # Open Device using serial number
d = ftd2xx.openEx(b'DP51RBFCA')

d.setTimeouts(5000, 5000)
#d.purge(ftd2xx.defines.PURGE_TX | ftd2xx.defines.PURGE_RX)
#print(d.getDeviceInfo())
#d.setTimeouts(1000,1000)
#d.purge()


#tx_data = str(bytearray([2,3]))

#=========Excel Sheet ===========
# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, "RAW_DATA")
#sheet1.write(0, 1, "PROCESSED_DATA")







# random_datalist = []
# for i in range(0,65535):
#     n = random.randint(0,255) # random int
#     random_datalist.append(n)
# print(random_datalist)
#
# tx_data = (bytes(random_datalist))
#
#
# for i in range(0, len(tx_data)):
#     print(hex(tx_data[i]))
#     sheet1.write((i+1), 0, hex(tx_data[i]))




#print("tx_data: " + str(tx_data))

#d.write(b"\x16")  # best way to write it

#d.purge(ftd2xx.defines.PURGE_TX | ftd2xx.defines.PURGE_RX) # clean the garbage
#time.sleep(100e-3)

#================ WRITE BLOCK==============================
# write_start_t = time.time()
# d.write(tx_data)
# write_end_t = time.time()
# write_time =  write_end_t - write_start_t
#=======================================================


# bytes_received = d.getQueueStatus()
# #
# print(bytes_received)
#
# print ("Queue Status: " + str(bytes_received))


init = int("0xAA",0)
init_dat = (bytes([init]))
d.write(init_dat)

time.sleep(0.1)

cw = int("0xAF", 0)
cw2 = int("0xAE", 0)
tx_data = (bytes([cw]))
 # d.purge(ftd2xx.defines.PURGE_TX | ftd2xx.defines.PURGE_RX)
d.write(tx_data)
time.sleep(1)
#read_start_time = time.time()
num_reads = 512
rx_data = (d.read(num_reads))  # reads and returns a byte array
#read_stop_time = time.time()
tx_data2 = (bytes([cw2]))
d.write(tx_data2)
rx_data2 = (d.read(8))

rxdata_str = str(rx_data) # convert the received data into string form
rxdata_str2 = str(rx_data2)

    #time.sleep(1)
#read_time = read_stop_time - read_start_time




for i in range(0,num_reads):
    print(hex(rx_data[i]))
    sheet1.write((i+1) , 0, hex(rx_data[i]))


for i in range(0,8):
    print(hex(rx_data2[i]))
    sheet1.write((i+1) , 1, hex(rx_data[i]))

#print("Read Time: " + str(read_time))


# print("Write Time : " + str(write_time) )
# print(str(128/(read_time+write_time)))


#print("read_data : " + hex(rx_data))

wb.save('fifo2.xls')
time.sleep(10e-2)
bytes_received = d.getQueueStatus()

print ("Queue Status: " + str(bytes_received))


# time.sleep(10e-3)
# rx_data = bytearray(d.read(len(tx_data)))
#
# for x in range (0, len(tx_data)):
#     d.purge(ftd2xx.defines.PURGE_TX | ftd2xx.defines.PURGE_RX)
#     print("Data Bit #"+ str(x+1) +  ": " + hex(rx_data[x]))
#     time.sleep(10e-3)
# time.sleep(10e-3)
# print (bytearray(d.read(1)))
# print("rx_data in integer: " + str(rx_data[0]) + " rx+data in hex: "+ hex(rx_data[0]))

d.close()



