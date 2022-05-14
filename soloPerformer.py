# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pylsl import StreamInlet, resolve_stream
from pythonosc.udp_client import SimpleUDPClient
import time
import threading
import util

# LSL init params
prop = 'name'
val = 'BioSemi'

numChannels = 64
#numChannels = np.array([38, 9, 33, 0, 20, 50, 55, 2])
#prop = 'name'
#val = 'EE225-000000-000144'
sample_rate = 1000

# OSC init params
ip = '127.0.0.1'
port = 12345
address = '/ant/timeseries/'

testSize = 10 # For fake data
sleepTime = 0 # For fake data


#t1 = threading.Thread(target = util.send_osc_singleSampleTest(ip, port, testSize, sleepTime, address))

#util.send_osc_singleSampleTest(ip, port, testSize, sleepTime, address)
#util.read_lsl(prop, val)
#streams = resolve_stream(prop, val)

try:
    # Resolve an EEG stream on the network
    print ("Looking for EEG stream...")
    streams = resolve_stream('type', 'EEG')
    print ('EEG stream found')
    print(f'stream is {streams}')
    # Create a new inlet to read from the stream
    print ("Opening an inlet")
    inlet = StreamInlet(streams[0])
    print ("inlet opened")
    print(f'inletshape{streams}')
    
    # OSC message
    client = SimpleUDPClient(ip, port)
    
    while True:
        print ("Pulling sample")
        sample, timestamp = inlet.pull_sample()
        print('---------------',type(sample[0]))
        #print('length: ', len(sample), 'type: ', type(sample))
        #send_msg = timestamp
        send_msg = sample[:numChannels]
        print (timestamp)
        # Send data to OSC
        client.send_message(address, send_msg)
        
except KeyboardInterrupt() as e:
    print ("Ending program")
    raise e