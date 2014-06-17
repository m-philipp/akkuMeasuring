'''
Created on 30.10.2012

@author: Martin
'''

import serial
import io
import time

def integrate():
    f = open('17-6-14.txt', "r")
    cap = [0,0,0,0,0,0]
    for line in f:
        value = line.rstrip()
        parts = value.split(" ")
        # Aufloesung des ADC-Wandlers ist 10bit (1024) bei max 5V
        for i in range(0,6):
            volts = ((float(parts[i+1])/1024)*5)
            
            # Die Spannung wurde alle 3 Sekunden gemessen.
            # Der meue Akku hatte einen Last Widerstand von 110 Ohm
            tempCap = (volts / 110)*3
            cap[i] += tempCap
    f.close()
    # Umrechnung von As in Ah
    for i in range(0,6):
        print "Kapazitat des " + str(i) + " Akkus: " + str(cap[i]/(60*60))
    
    
def serialRead():
    ser = serial.Serial(
    # "COM8",            #number of device or a device string
    "/dev/ttyACM0",            #number of device or a device string
    baudrate=9600,    #baudrate
    )
    while 1:
        f = open('17-6-14.txt', 'a')
        line = ser.readline()   # read a '\n' terminated line
        x = str(time.time()) + " " + line
        f.write(x)
        print x
        
        
if __name__ == '__main__':
    print "Text.py Started"
    integrate()
    #serialRead()
        
