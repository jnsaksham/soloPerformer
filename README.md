# soloPerformer
A live brain music performance system originally conceptualized by Alvin Lucier. The system reads EEG data real-time from ANT Neuro/ OpenBCI systems and uses that to play percussions acoustically.

## Compatible devices
Can potentially work with any device with upto 64 EEG channels. Have personally tested with ANT Neuro's and Brain Vision's 32 and 64 channel EEG devices.

## Networking
System uses lab streaming layer for networking

## Generation
We have used max to select relevant channels, filter EEG signals to alpha. wave region (8-12 Hz) and then send them out to physical amplifiers and speaker drivers which then resonate with the skin of the percussive instrument
