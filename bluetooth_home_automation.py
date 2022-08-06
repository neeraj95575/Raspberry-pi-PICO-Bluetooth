from machine import Pin,UART

import utime

uart = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

relay1 = machine.Pin(2, machine.Pin.OUT)
relay2 = machine.Pin(3, machine.Pin.OUT)
relay3 = machine.Pin(4, machine.Pin.OUT)
relay4 = machine.Pin(5, machine.Pin.OUT)

relay1.value(1)
relay2.value(1)
relay3.value(1)
relay4.value(1)


while 1:
        data_read = uart.read()# 6 denotes number of data in bytes(you can change as you can w.r.t application)
        if data_read is not None:
            data = data_read.decode("utf-8")
            print("data = ",data)#bytes(n,'utf-8')
            if data == 'A':
                relay1.value(0)
                print('relay 1 ON')
                
            elif data == 'W':
                relay1.value(1)
                print('relay 1 OFF')
                
            elif data == 'B':
                relay2.value(0)
                print('relay 2 ON')
                
            elif data == 'X':
                relay2.value(1)
                print('relay 2 OFF')
                
            elif data == 'C':
                relay3.value(0)
                print('relay 3 ON')
                
            elif data == 'Y':
                relay3.value(1)
                print('relay 3 ON')
                
            elif data == 'D':
                relay4.value(0)
                print('relay 4 ON')
                
            elif data == 'Z':
                relay4.value(1)
                print('relay 4 ON')
                
