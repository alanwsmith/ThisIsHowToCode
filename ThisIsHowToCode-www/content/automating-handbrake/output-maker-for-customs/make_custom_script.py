#!/usr/bin/env python3

input_file = '/Users/alans/Desktop/handbrake/input.mkv'
output_directory = '/Users/alans/Desktop/handbrake/output'
handbrake_path = '/Users/alans/Desktop/handbrake/HandBrakeCLI'

encoders = [
    {
        'name': 'x264',
        'presets': [ 'ultrafast','veryfast', 'fast', 'slow', 'veryslow' ]
    },
    {
        'name': 'x265',
        'presets': [ 'ultrafast','veryfast', 'fast', 'slow', 'veryslow' ]
    },
    {
        'name': 'VP8',
        'presets': [ 'veryfast', 'fast', 'slow', 'veryslow' ]
    }
]


qualities = [
    '5',
    '10',
    '15',
    '20',
    '25',
    '30',
    '35'
]

rates = [
    '20',
    '24',
    '25',
    '30',
]

sizes = [
    {
        'width': '1920',
        'height': '1080'
    },
    {
        'width': '1280',
        'height': '720'
    }
]


optimize_flags = [
    '--optimize',
    ''
]



with open("custom_run.bash", 'w') as _file:
    _file.write("#!/bin/bash\n\n")        
    for encoder in encoders:
        for preset in encoder['presets']:
            for quality in qualities: 
                for rate in rates:
                    for size in sizes:
                        for optimize_flag in optimize_flags:
                                
                            command = '"{}" -r {} -q {} -e {} --encoder-preset {} {} --width {} --height {} -i "{}" -o "{}/custom-{}-{}-{}-r-{}-q-{}{}.mp4"'.format(
                                handbrake_path,
                                rate,
                                quality,
                                encoder["name"], 
                                preset,
                                optimize_flag,
                                size['width'],
                                size['height'],
                                input_file,
                                output_directory,
                                size['height'],
                                encoder["name"],
                                preset,
                                rate,
                                quality,
                                optimize_flag,
                            )

                            _file.write(f"{command}\n")
