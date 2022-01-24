import os

board_id = 2
serial_port = 'COM3'
name = 'mindset_EXG'
data_type = 'EXG'
channel_names = 'FP1,FP2,C3,C4,P7,P8,O1,O2,F7,F8,F3,F4,T7,T8,P3,P4'
uid = 'brainflow'

cmd = "python brainflow_lsl.py --board-id %s --serial-port %s --name %s --data-type %s --channel-names %s --uid %s" % (board_id, serial_port, name, data_type, channel_names, uid)
print(cmd)

os.system(cmd)

