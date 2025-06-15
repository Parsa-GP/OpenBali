## Where am i?
Welcome! Here is my workplace. my lab, some might say. where i put every dump, every note and every tool that i found or wrote for the sake of documentary.

so expect to not underestand most of the things i write in notes, although i leave comments sometimes for future me.

## some useful tabs to be open
- https://www.rapidtables.com/convert/number/ascii-to-hex.html
- https://www.rapidtables.com/convert/number/hex-to-ascii.html

- https://www.rapidtables.com/convert/number/decimal-to-hex.html
- https://www.rapidtables.com/convert/number/hex-to-decimal.html

- https://onlinestringtools.com/convert-decimal-to-string
- https://onlinestringtools.com/convert-string-to-decimal

## Documentary (hopefully i don't forget to write it everytime)

I thought it was a key value thing so that the first 4 hex chars in a row was the key id in keyboard physically, and the other 4 was the key that it should send to the device once the key is pressed. and there was 1 key values in each row

But i saw some characters were funky, like it was a offset in some of them, sometime it was each 2 row, sometime it was 3, randomly. and I found out the first 2 chars in each row are always 0's. and there are 63 characters put together in rows. there was some (i think 24) rows that had 00 as their value

As of now, i think each cell corresponds to a character, and the character is not from ASCII table (obviousely, because number 1 is not 0x29 or 0x1e)

### cfg.ini file structure
I found a cfg file and wrote a visualizer for it. there are data like this:
```ini
;X
K77=110,167,129,188, 0x02,0x58,0x00,16
```
`X` is obviosely the key name commented out. i had to name the numpad's enter key to something so that the visualizer would display it.

`K77` is the number of the key in placement order in ini file, nothing related to the physical side of the things. It is ordered *horizontaly*.

Those 4 numbers (`110,167,129,188`) are coordinates of each point for a rectangle to be drawn, so the user can click on it in the driver software. might come in handy when writing the gui for this.

`0x02,0x58,0x00` I don't have any fucking idea what these are, i tried hard, examined the cfg file, the characters for each key, nothing. But in every key entry (each row in the cfg.ini file) the 0x02 and 0x00 was the same. the only variable was the middle one. maybe that is the data i want (spoiler alert: probably not)

`16` is the number of the key counted *verticaly*. opposite of K77 thing. silly, i know.
