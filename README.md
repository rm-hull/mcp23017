mcp23017
========

Schematics and build info for assembling multiple MCP23017 input/output port
expanders with bi-directional level shifters and selectable power source
(Internal 3V3, 5V, External 5V), as below.

![Level shifter](https://raw.github.com/rm-hull/mcp23017/master/doc/level-shifter.jpg) [Attribution unknown]

Further technical details for the MCP23017 expander can be found in the 
[datasheet](https://raw.github.com/rm-hull/mcp23017/master/doc/MCP23017%20datasheet.pdf) [PDF].

Schematic
---------
![Stripboad Layout](https://raw.github.com/rm-hull/mcp23017/master/doc/schematic_bb.png)

Installation
------------
Edit `/etc/modules` and add the following entries:

    i2c-bcm2708
    i2c-dev

and reboot. Alternatively, modprobe them in. Either way, confirm the driver
has loaded properly:

    $ dmesg | grep i2c
    [   18.310467] bcm2708_i2c bcm2708_i2c.0: BSC0 Controller at 0x20205000 (irq 79) (baudrate 100k)
    [   18.332292] bcm2708_i2c bcm2708_i2c.1: BSC1 Controller at 0x20804000 (irq 79) (baudrate 100k)
    [   18.480593] i2c /dev entries driver

Then add your user to the i2c group:

    $ sudo adduser pi i2c

Install some packages:

    $ sudo apt-get install i2c-tools python-smbus

Check to see if the chip has registered (revision 2 RPi's should use icbus
1, whereas earlier revisions use 0):

    $ i2cdetect -y 1
         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    20: 20 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    70: -- -- -- -- -- -- -- --    

TODO
----
* Expand documentation

* Example programs

References
----------
* http://nathan.chantrell.net/20120602/raspberry-pi-io-expander-board/

* http://www.bootc.net/archives/2012/05/19/i2c-and-the-raspberry-pi/



[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/rm-hull/mcp23017/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

