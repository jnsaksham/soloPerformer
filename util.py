# -*- coding: utf-8 -*-
import numpy as np
import time
from pylsl import StreamInlet, resolve_stream
from pythonosc.udp_client import SimpleUDPClient

def osc_single_sample_test(samples, sleepTime, address, client):
    # Sends one sample at a time via osc with given sleepTime in s
    array = np.arange(1, samples+1).astype('float')
    #sum = 0
    #t0 = time.time()
    for i in np.arange(len(array)):
        print (samples) 
        sample = array[i]
        #t1 = time.time()
        client.send_message(address, sample)
        time.sleep(sleepTime)
        print ('Message %s sent'% i)
        #t2 = time.time()
        #sum += t2-t1
    #tf = time.time()
    #print ('total time: ', tf-t0)
    #print ('comm time total: ', sum)

def send_osc_singleSampleTest(ip, port, samples, sleepTime, address):
    # run = type of data: oneSampleTest, Test, Actual
    client = SimpleUDPClient(ip, port)
    osc_single_sample_test(samples, sleepTime, address, client)

def read_lsl(prop, val):
    try:
        # Resolve an EEG stream on the network
        print ("Looking for EEG stream...")
        #stream_name = lsl_get_name()
        #print(f'stram name{stream_name}')
        #stream_info = lsl_get_streamInfo()
        #stream_type = lsl_get_type()
        streams = resolve_stream(prop, val)
        print ('EEG stream found')
        print(f'stream is {streams}')
        # Create a new inlet to read from the stream
        print ("Opening an inlet")
        inlet = StreamInlet(streams[0])
        print ("inlet opened")
        
        while True:
            print ("Pulling sample")
            sample, timestamp = inlet.pull_sample()
            print (timestamp, sample)
            
    except KeyboardInterrupt() as e:
        print ("Ending program")
        raise e

def soloPerformer(ip, port):
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
        
        # Create osc client
        client = SimpleUDPClient(ip, port)
        
        while True:
            print ("Pulling sample")
            sample, timestamp = inlet.pullsample()
            print (timestamp, sample)
            client.send_message(address, sample)
            
    except KeyboardInterrupt() as e:
        print ("Ending program")
        raise e