# PyCon2019
This repo contains the Circuit Python Quickstart worksheet and example code for the PyCon 2019 
Circuit Playground Express, sponsored by Digi-Key and Adafruit!

Everyone will be receiving a Circuit Playground Express in their swag bag! Getting started with it
requires a micro USB to USB cable. We will have a few for use during the CircuitPython Open Spaces,
however we do not have enough for everyone. Beware of charge-only cables, they will not work for
programming your Circuit Playground Express! **Please remember to bring a _DATA CAPABLE_ micro USB
cable with you!**

We will be hosting Open Spaces every day at PyCon, May 3 - May 5, 2019. We'll have this Quickstart
available as a worksheet, including some examples on the back to get you started. This repo will
have those examples and more available for you to try, play with, and modify. We'll also have some
extras (servos, potentiometers and external NeoPixel strips) available for you to connect to
your Circuit Playground Express.

**The Adafruit Circuit Playground Express (CPX) has CircuitPython on board!** It’s a Microchip
SAMD21 microcontroller running at 48 MHz, with 256kB flash, plus a 2MB external flash chip
for the CIRCUITPY USB drive. The board is loaded with all kinds of sensors, LEDs, touch pads,
buttons and more!

#### Check out these Adafruit Learn Guide Links!
* Welcome to CircuitPython: http://adafru.it/cpy-welcome
* CPX Guide: https://adafru.it/adafruit-cpx
* CP Made Easy on CPX: https://adafru.it/cp-made-easy-on-cpx 

#### Download the latest CircuitPython for Circuit Playground Express!
* CircuitPython for CPX: https://circuitpython.org/board/circuitplayground_express/

#### Are you on Windows 7?
You need to install drivers before plugging in! See [Welcome->Installing
CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython). 

Windows 10, Mac, and Linux don’t need drivers.

#### Plug It In!
Use a micro-USB cable with data (beware charge/power-only cables). A USB drive called **CIRCUITPY**
will appear. If there’s a **code.py** on **CIRCUITPY**, it will run automatically. 

#### Avoiding Filesystem Corruption
Windows and Linux don’t write back data to **CIRCUITPY** immediately: they can delay for 10s of
seconds. (Not an issue on MacOS.) **Eject or sync after you copy files, and always before you
unplug or press the Reset button.** Otherwise **CIRCUITPY** may become corrupted. Continue reading
to see editors that write immediately so you don’t need to Eject or sync every time you edit.
If **CIRCUITPY** does get corrupted, see **_Restoring or Installing CircuitPython_** in this
Quickstart.

#### Editing Code
If you already have a favorite code editor, you can use it. Be sure you’re using one that writes
back immediately: VS Code, Atom (install the fsync-on-save package), Sublime, gedit, vim with `-n`
option, emacs, PyCharm with Safe Write. **_Don’t_ use** Notepad, nano, IDLE. See [Welcome->Creating
and Editing Code](https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code)
for more details.

#### Another Editor Option
Mu is the easiest editor to use: it includes a Python editor and easy serial REPL access. See [Welcome
->Installing Mu Editor](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor).
The latest version for Windows and Mac are available at https://codewith.mu. For Linux, or any OS,
you can create a `venv` and use `pip3` to install Mu: `pip3 install --user mu-editor`

#### Auto-Reload
Every time you write a file, **code.py** will be re-run, unless you are in the REPL. Just edit
**code.py** and see it run right away. This makes for a fast workflow.

#### Libraries
CircuitPython has builtin native libraries, but also has libraries written in Python (which are
compiled into **.mpy** files to save space). The board has a does not currently have a **lib**
folder because all of the necessary libraries for these examples are built into CircuitPython for
CPX. But, if you want to use external peripherals in the future, you’ll need to download the right
libraries. See [Welcome->CircuitPython
Libraries](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries).

#### Restoring or Installing CircuitPython
[CircuitPython.org](https://adafru.it/cp-cpx) has the current version of the CircuitPython UF2 for
the Circuit Playground Express. **WARNING: In rare cases, this process can result in the loss of
any files on the board - backup your files if possible first!** To restore or update your board,
double-tap the reset button found in the center of the board. The LEDs will flash red and then turn
green, and you’ll see a **CPLAYBOOT** drive show up on your computer. Copy the .uf2 file to
**CPLAYBOOT**. It will disconnect and the drive will disappear. A few seconds later, **CIRCUITPY**
will reappear. If this does not resolve your issue, check out [Welcome->Troubleshooting->CIRCUITPY Drive
Issues](https://learn.adafruit.com/welcome-to-circuitpython/troubleshooting#circuitpy-drive-issues-20-20)
for instructions to fully erase the filesystem. **The steps found here WILL erase everything on the
board.**

#### Connecting to the Serial Console
The serial console and REPL are built into Mu - simply click the icon labeled “Serial”. 

If not using Mu, on Windows, try **Putty** or **Tera Term**. See [Welcome->Advanced Serial Console
On Windows](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-windows)
for more details. On Mac and Linux, try **`screen`** or **picocom**, or any other terminal emulator
you may already be using. Use tab completion for the paths on Mac `/dev/tty.usbmodem*` or Linux 
`/dev/ttyACM*` while entering `screen` commands. See [Welcome->Advanced Serial Console on Mac and
Linux](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-mac-and-linux)
for more details.

* To connect using `screen` on Mac:
    * `screen /dev/tty.usbmodem* 115200`
* To connect using `screen` on Linux:
    * `screen /dev/ttyACM0 115200`
