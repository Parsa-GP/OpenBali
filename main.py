import usb.core
import binascii
from modes import *


def set_mode(mode:Mode):
  hex_list = {
    "Steady":                 "0a0101020500000000000000000000000000000000000000000000000000000000000000000000000000",
    "Shadow_disappear":       "0a0201020500000000000000000000000000000000000000000000000000000000000000000000000000",
    "Breathing":              "0a0301020500000000000000000000000000000000000000000000000000000000000000000000000000",
    "Gaming Special Key": 		"0a0401020500000000000000000000000000000000000000000000000000000000000000000000000000",
    "Retro_snake":            "0a0501020500000000000000000000000000000000000000000000000000000000000000000000000000",
    "Diagonal transformation":"0a0601020500000000000000000000000000000000000000000000000000000000000000000000000000",
    "Marquee effect":         "0a0701020500000000000000000000000000000000000000000000000000000000000000000000000000",
    "Flowing light and color":"0a0801020500000000000000000000000000000000000000000000000000000000000000000000000000",
    "Dazzling":               "0a0901020500000000000000000000000000000000000000000000000000000000000000000000000000"
  }
  if hasattr(mode, 'brightness'):
    data = "0a"+f"{mode.id:02d}"+"0102"+"0"+str(mode.brightness)
  else:
    data = "0a"+f"{mode.id:02d}"+"0102"+"05"
  return f"{data:084}"



if __name__ == "__main__":
  hex_data = set_mode(mode=Dazzling(brightness=5))

  # Find the USB device
  dev = usb.core.find(idVendor=0x258a, idProduct=0x002a)
  if dev is None:
    raise ValueError("Device not found")

  # Detach kernel driver if necessary
  if dev.is_kernel_driver_active(1):
    dev.detach_kernel_driver(1)

  # Uncomment if not worky
  #dev.set_configuration()

  # Convert hex to bytes
  data = binascii.unhexlify(hex_data)

  # Send SET_REPORT requests
  dev.ctrl_transfer(bmRequestType=0x21, bRequest=0x09, wValue=0x030A, wIndex=1, data_or_wLength=data, timeout=1000)
