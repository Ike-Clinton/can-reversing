# can-reversing
Repo for python CAN capture file reverse engineering

## Usage Examples

### Make Virtual CAN Interface
Use the provided "make_vcan0.sh" script to setup a virtual CAN
interface for testing. 
```sudo ./make_vcan0.sh
You can then do things like:
```candump vcan0
```cansend vcan0 123#FFFFFFFF
To test out that your can-utils are working correctly

### Send a list of CAN frames across an interface
Useful for replaying CAN frames, use the provided send_list.sh
script to send a list of frames in the format:
ID#DATA
Example: ``` ./send_list.sh replays/headlight_indicator_toggle.txt
Modify the script if you want it to send across vcan0 instead of can0

### Count Frame IDs in a log file
This python script parses a log file given by CANdump
and will tell you the frequency of all CAN IDs present in
the log file
