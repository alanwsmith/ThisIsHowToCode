#!/usr/bin/env python3

import glob 
import os.path 
import subprocess
import time 


# Config
source_dir = r'D:\gif_automation_test\test-v3\source'
destination_dir = r'D:\gif_automation_test\test-v3\destination'


while True:
    # print("Getting file list...")
    source_list = glob.glob(f'{source_dir}/*.gif')

    for source_path in source_list:

        try:  
            file_name = os.path.basename(source_path)
            destination_path = f'{destination_dir}\\{file_name}'
            # print(f'Moving: {source_path}')
            # print(f'To: {destination_path}')
            subprocess.run([
                'ffmpeg.exe', '-ss', '0', '-i', source_path, '-vf', 'fps=14,scale=480:-2:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse', '-loop', '0', '-hide_banner', '-loglevel', 'warning', '-y', destination_path
            ], shell=True, stderr=subprocess.PIPE).stderr
            os.remove(source_path)
        except:
            pass
    
    time.sleep(1)
