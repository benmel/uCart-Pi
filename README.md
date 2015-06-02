# uCart-Pi
This application runs on a Raspberry Pi. It sends data from a barcode scanner and card runner over bluetooth.

### Start application automatically
1. In `/etc/inittab` comment `1:2345:respawn:/sbin/getty --noclear 38400 tty1` and add `1:2345:respawn:/bin/login -f pi tty1 </dev/tty1 >/dev/tty1 2>&1`
2. In `/etc/profile` add:

  ```
  cd /home/pi/uCart-Pi
  python main.py
  ```
3. Reboot
