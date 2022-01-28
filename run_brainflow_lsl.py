import os

board_id = 2
serial_port = 'COM3'
name = 'mindset_EXG'
data_type = 'EXG'
channel_names = 'Fz,FC1,FC2,C3,Cz,C4,CP1,CP2,P3,Pz,P4,PO3,PO4,O1,Oz,O2'
uid = 'brainflow'

cmd = "python brainflow_lsl.py --board-id %s --serial-port %s --name %s --data-type %s --channel-names %s --uid %s" % (board_id, serial_port, name, data_type, channel_names, uid)
print(cmd)

os.system(cmd)

