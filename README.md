# can-reversing
A collection of python and bash utilities to aid in the reverse-engineering
process of identifying and understanding CAN bus implementations in vehicles.

## Usage Examples

### Make Virtual CAN Interface
Use the provided "make_vcan0.sh" script to setup a virtual CAN
interface for testing. 

```bash
sudo ./make_vcan0.sh
```
You can then do things like:

```bash
candump vcan0
cansend vcan0 123#FFFFFFFF
```

to test out that your can-utils are working correctly.

### Send a list of CAN frames across an interface
Useful for replaying CAN frames, use the provided send_list.sh
script to send a list of frames in the format:

ID#DATA

Example: 
```bash
 ./send_list.sh replays/headlight_indicator_toggle.txt
```

Modify the script if you want it to send across vcan0 instead of can0

### Count Frame IDs in a log file
The python script "count_ids.py" parses a log file given by CANdump
and will tell you the frequency of all CAN IDs present in
the log file
