# Vendinator  
This repository is to share our source code for a Raspberry Pi device which sends a message to a Parse application when items are vended.  Please see the [Raspberry Pi Quick Start-up Guide](https://www.raspberrypi.org/help/quick-start-guide/) to setup your RPI. You must have an established Parse table with the number of items in your vending machine. This is a matter of creating a "Class" and entering the items as elements of your table, with "Quantity" and "Title" attributes.

We are working on developing a dongle to interface with various vending machines at this time, please be on the lookout for the item release! Until then, let us know if you have any suggestions by emailing gus.github@gmail.com.

----------
**Requirements:**

 1. Raspberry Pi
	 - With NOOBS and [ParsePy](https://github.com/dgrtwo/ParsePy) installed
 2. Parse database with your vending machine items as elements
 3.  A vending machine

----------
**ReadMe Contents:**
1. Configuring Raspberry Pi for automatic startup
2. Running the iOS application
3. Python Code 

----------
 - Configuring Raspberry Pi running NOOBS Linux to run our script on start-up:  
	- Bypass login (no password or username needed) 
        - modify `$/etc/inittab` on the line that starts with `1:2345:` to say `1:2345:respawn:/bin/login -f pi tty1 </dev/tty1 >/dev/tty1 2>&1"
`
    - Configure wifi to autoconnect
        - modify `/etc/wpa_supplicant/wpa_supplicant.conf`
	        - add the relevant wifi information as the first entry of SSIDs  
	    - add an auto connect attribute to 'wlan0' connection  
	        - change `/etc/network/interfaces` file to say `'autowlan0'`  
	- Add Python implementation to the startup script  
	    - Change `/etc/rc.local` to add the path to the implementation
	        - Change the python source to an executable  
		        - run `chmod +x filename`
	        - Add a line to say `/home/pi/..././filename.py`
	            - Note the `./` before the Python filename
	            - 
 - Running the iOS Application
    - In order to run the Vendinator iOS app,  you need to have an Apple computer running Mac OS X 10.9 or later and have XCode installed. 
    - From there you can run the app on the iPhone simulator included with XCode by simply pressing the Play button on the top left corner of the software.
 - Deploying our Python Code with Parse API
	 - This is a simple matter, as we've done the work for you
		 - Simply download our Python code and insert your Application Key and Master Key in the allotted spaces. 
 - Sit back and profit!

  
