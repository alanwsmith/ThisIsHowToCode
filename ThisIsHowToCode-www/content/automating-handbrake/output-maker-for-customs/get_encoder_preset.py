#!/usr/bin/env python3 

import subprocess


encoders = [
    'x264','x264_10bit','x265','x265_10bit','x265_12bit',
    'mpeg4', 'mpeg2', 'VP8', 'VP9', 'theora'
]

for encoder in encoders:
    response = subprocess.run([
        '/Users/alans/Desktop/handbrake/HandBrakeCLI', 
        '--encoder-preset-list',
        encoder
        ], stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(response)

