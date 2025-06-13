import usb.core
import binascii
from modes import *

if __name__ == "__main__":
  hex_data = Steady().hex_data()

  # Convert hex to bytes
  data = binascii.unhexlify(hex_data)

  # Find the USB device
  # change idVendor and idProduct if keyboard is different
  dev = usb.core.find(idVendor=0x258a, idProduct=0x002a)
  if dev is None:
    print("Device not found. grab usb id (258a:002a -like value) from running `lsusb` and put it in code.")
    exit(1)

  # If you are not using the supported keyboard,
  # you may check for your interface id.
  # uncomment the following code to list all interfaces.
  # you may run `sudo lsusb -v -d 258a:002a` for full details.
  # the descriptior that you want is the one with a lot of "Report Descriptor" items
  '''
  for intf in cfg:
      print(f"Interface Number: {intf.bInterfaceNumber}")
      print(f"  Class: {intf.bInterfaceClass}")
      print(f"  SubClass: {intf.bInterfaceSubClass}")
      print(f"  Protocol: {intf.bInterfaceProtocol}")
      print(f"  Endpoints: {[ep.bEndpointAddress for ep in intf]}")
  exit()
  '''

  # Detach kernel driver if necessary
  if dev.is_kernel_driver_active(1):
    dev.detach_kernel_driver(1)
  

  # Uncomment if not worky
  #dev.set_configuration()

  cfg = dev.get_active_configuration()

  # Send SET_REPORT request
  print(hex_data)
  dev.ctrl_transfer(bmRequestType=0x21, bRequest=0x09, wValue=0x030A, wIndex=1, data_or_wLength=data, timeout=1000)
