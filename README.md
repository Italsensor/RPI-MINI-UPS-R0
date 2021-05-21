# RPI-MINI-UPS

**Introduction**

RPI-MINI-UPS, is a small Raspberry Pi board (made of 4 layers pcb) that work as UPS and is also able to manage the Raspberry Pi power-on and power-off like a classical desktop system by means of an external normally-open push-button, other than is also incorporated a dedicated RTC module accessibile through the Raspberry I2C bus and also a RS232 driver connected to the serial pins of the Raspberry GPIO for direct usage by the user.

**Board registers**

The board can be queried from the I2C bus to know many operative parameters (presence or not of the main power supply, backup battery voltage, state of charging of the backup battery, ecc...) and expose to the user also an EEPROM memory area (16 registers) that can be used directly by the user to store in a permanent way any desired data.

Here a table of the available registers:

| Register address | Name        | Access | Description                                          |
| ---------------- | ----------- | ------ | ---------------------------------------------------- |
| 0x00 - 0x0F      | EEPROM AREA | R/W    | EEPROM user area                                     |
| 0x10             | POWER ON HI | R      | Power on counter hi-byte                             |
| 0x11             | POWER ON LO | R      | Power on counter lo-byte                             |
| 0x2E             | FW_REV      | R      | Firmware revision                                    |
| 0x2D             | FW_VER      | R      | Firmware version                                     |
| 0x34             | IBCHGMAX    | R      | LiPo max charge current default setting              |
| 0x3E             | BATTV       | R      | LiPo measured battery voltage                        |
| 0x41             | VIN         | R      | Input measured voltage                               |
| 0x42             | IBCHG       | R      | Lipo measured charging current                       |
| 0x50             | FAULT_FLAG  | R      | Fault event flag                                     |
| 0x51             | FAULT_RST   | R      | Fault event flag reset                               |
| 0x52             | FAULT_CURR  | R      | Fault register values for the current fault event    |
| 0x53             | FAULT_PREV  | R      | Fault register values before the current fault event |
| 0x54             | VINSTATE    | R      | Status of the input voltage (present / absent)       |
| 0x55             | BTCHGSTAT   | R      | Current charging stage for the LiPo battery          |

R: readable register  
W: writeable register  
R/W: readable and writeable register  

A writing operation to an only readable register have no effect, also writing on a register address that is not addressed on the table above have no effect, reading on a register that is not into the table above may report arbitrary value.

**Raspberry Pi RPI-MINI-UPS board dedicated GPIO resource**

In order to signal to the Raspberry module whwn the main power supply is lost (blackout bvent) and then when is time to start the controlled shutdown, the RPI-MINI-UPS board use the physical pin 11 (GPIO17) pin of the GPIO Raspberry board connector, this is the only pin that is used by the board itself, all the other pins on the GPIO are transparent from the board perspective.

**Operating modes**

The board can operate in two functioning modes:

- auto mode;
- manual mode;

*Auto mode*

The board act as a classical UPS, charging the battery if needed when the main power supply source is available and used the battery stored energy to supply the Raspberry Pi when the main power supply is lost. Before the backup battery is discharged a signal is sent to a dedicated pin of the GPIO in order to let the Raspberry perform a gracefully shutdown.

*Manual mode*

In this mode, by adding an external push-button (normally open) between a dedicated pin on the board and the 0V, the RPI-MINI-UPS can act to manage the power-on and power-off from the user action. Before the backup battery is discharged a signal is sent to a dedicated pin of the GPIO in order to let the Raspberry perform a gracefully shutdown.

The current charging status of the LiPo battery and the presence/absence of the main supply or when a fault event occur is also signaled through some dedicated leds that are on the board.

**Examples**

Examples files for the RPI-MINI-UPS board can be found inside the *Examples* folder.

*ex-i2c.py*  
python script to show how communicate through the I2C bus with the MINI-UPS-BOARD (with using the smbus module).

*ex-subprocess-i2c.py*  
python script to show how communicate through the I2C bus with subprocess module (without using the smbus module).

*ex-serial.py*  
python script (for Python 2.x) to test the serial communication.

*ex-serial-py3.py*  
python script (for Python 3.x) to test the serial communication.

*RPI-HW-Checker.py*  
python script (for Python 3.x) to check the hardware state of the RaspberryPi by means of the vcgencmd Python package.

**Board picture**

Into the *Images* folder there are some images of the board.

![Image](/Images/miniups_r0-1.jpg)

Figure 1: Top layer view (perpective)

![Image](/Images/miniups_r0-3.jpg)

Figure 2: Bottom layer view (perspective) - the battery shown is about the RTC module. The backup battery connector is the white one.
