#! /usr/bin/python

import smbus
import time

bus = smbus.SMBus(1) # For revision 1 Raspberry Pi, change to bus = smbus.SMBus(1) for revision 2.

address = 0x25 # I2C address of MCP23017
bus.write_byte_data(address,0x00,0x00) # Set all of bank A to outputs
bus.write_byte_data(address,0x01,0x00) # Set all of bank B to outputs
register = 0x12 # = bank A, 0x13 = bank B

# Handle the command line arguments
def main():

    value = 0
    while True:
        value = (value + 1) % 8

        # Now write to the IO expander
        bus.write_byte_data(address,register,value)

        time.sleep(0.5)

if __name__ == "__main__":
   main()
