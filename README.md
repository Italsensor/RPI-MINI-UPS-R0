# RPI-MINI-UPS

**Introduction**
RPI-MINI-UPS, is a small Raspberry Pi board (made of 4 layers pcb) that work as UPS and is also able to manage the Raspberry Pi power-on and power-off like a classical desktop system by means of an external normally-open push-button, other than is also incorporated a dedicated RTC module accessibile through the Raspberry I2C bus and also a RS232 driver connected to the serial pins of the Raspberry GPIO for direct usage by the user.

The board can be queried from the I2C bus to know many operative parameters (presence or not of the main power supply, backup battery voltage, state of charging of the backup battery, ecc...) and expose to the user also an EEPROM memory area (16 registers) that can be used directly by the user to store in a permanent way any desired data.

The board support two functioning modes:

- auto mode;
- manual mode;

*Auto mode*

The board act as a classical UPS, charging the battery if needed when the main power supply source is available and supply power when the main power supply is lost, before depleteing the backup battery a signal is sent to a dedicated pin of the GPIO in order to let the Raspberry perform a gracefully shutdown.

*Manual mode*

In this mode, by adding an external push-button (normally open) between a pin and 0V the board can act to manage the power-on and power-off from the user action and before depleteing the backup battery a signal is sent to a dedicated pin of the GPIO in order to let the Raspberry perform a gracefully shutdown.

**Examples**

Examples files for the RPI-MINI-UPS board can be found inside the Examples folder.

*ex-i2c.py* : python script to show how communicate through the I2C bus with the MINI-UPS-BOARD.

**Board picture*

Into the *Images* folder there are some images of the board.

![Image](/Images/miniups_r0-1.jpg)

Figure 1: Top layer view (perpective)

![Image](/Images/miniups_r0-3.jpg)

Figure 2: Bottom layer view (perspective) - the battery is about the RTC module.
