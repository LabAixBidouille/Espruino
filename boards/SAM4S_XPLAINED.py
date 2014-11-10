#!/bin/false
# This file is part of Espruino, a JavaScript interpreter for Microcontrollers
#
# Copyright (C) 2014 Thibaut VIARD for LabAixBidouille <aethaniel@sam-geek.org>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# ----------------------------------------------------------------------------------------
# This file contains information for a specific board - the available pins, and where LEDs,
# Buttons, and other in-built peripherals are. It is used to build documentation as well
# as various source and header files for Espruino.
# ----------------------------------------------------------------------------------------

import pinutils;
info = {
 'name' : "SAM4S-Xplained",
 'link' : [ "http://www.atmel.com/tools/sam4s-xpld.aspx" ],
 'variables' : 2250,
 'bootloader' : 0,
 'serial_bootloader' : False,
 'binary_name' : 'foo.bin',
};
chip = {
  'part' : "ATSAM4S16C-AU",
  'family' : "SAM4S",
  'package' : "LQFP100",
  'ram' : 128,
  'flash' : 1024,
  'speed' : 120,
  'usart' : 4,
  'spi' : 1,
  'i2c' : 2,
  'adc' : 1,
  'dac' : 1,
};
# left-right, or top-bottom order
board = {
  'J1_top' : [ 'PA4', 'PB3', 'PA13', 'PA14', '3.3' ],
  'J1_bottom' : [ 'PA3', 'PB2', 'PA31', 'PA12', 'GND' ],
  'J2_top' : [ 'PC12', 'PB1', 'PA21', 'PC15', '3.3' ],
  'J2_bottom' : [ 'PA22', 'PB0', 'PA17', 'PC13', 'GND' ],
  'J3_top' : [ 'PA11', 'PA18', 'PA16', 'PC2', '5.0' ],
  'J3_bottom' : [ 'PA20', 'PA23', 'PA15', 'PA2', 'GND' ],
  'J4_top' : [ 'PA4', 'PB3', 'PA13', 'PA14', '3.3' ],
  'J4_bottom' : [ 'PA3', 'PB2', 'PA30', 'PA12', 'GND' ],
};
devices = {
  'OSC_12M' : { 'pin_in' :  'PA7',
                'pin_out' : 'PA8' },
  'OSC_32K' : { 'pin_in' :  'PB9',
                'pin_out' : 'PB8' },
  'LED1' : { 'pin' : 'PC10' },
  'LED2' : { 'pin' : 'PC17' },
  'BP2' : { 'pin' : 'PA5' },
  'USB' : { 'pin_dm' : 'PB10',
            'pin_dp' : 'PB11' },
};

board_css = """
#board {
  width: 1293px;
  height: 868px;
  left: 300px;
  background-image: url(img/SAM4S-Xplained.png);
}
#boardcontainer {
  height: 1000px;
}
#J1_top {
  top: 31px;
  left: 171px;
}
#J1_bottom {
  bottom: 71px;
  left: 171px;
}
#J2_top {
  top: 698px;
  left: 175px;
}
#J2_bottom {
  top: 738px;
  left: 175px;
}
#J3_top {
  top: 0px;
  left: 906px;
}
#J3_bottom {
  bottom: 71px;
  left: 906px;
}
#J4_top {
  top: 699px;
  left: 904px;
}
#J4_bottom {
  bottom: 739px;
  left: 904px;
}
.leftpin { height: 24px; }
.rightpin { height: 24px; }

""";

def get_pins():
  pins = pinutils.scan_pin_file([], 'atsam4s.ods', 11, 12, 11)
  return pinutils.only_from_package(pinutils.fill_gaps_in_pin_list(pins), chip["package"])
