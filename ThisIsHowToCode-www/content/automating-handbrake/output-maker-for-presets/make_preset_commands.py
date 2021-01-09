#!/usr/bin/env python3

input_file = '/Users/alans/Desktop/handbrake/input.mkv'
output_directory = '/Users/alans/Desktop/handbrake/output'
handbrake_path = '/Users/alans/Desktop/handbrake/HandBrakeCLI'


with open('preset_list.txt', 'r') as _file:
    presets = _file.read().splitlines()

with open('preset_run.bash', 'w') as _file:
    _file.write("#!/bin/bash\n\n")
    for preset in presets:
        preset_without_spaces = preset.replace(' ', '-')
        command = f'{handbrake_path} -Z "{preset}" -i "{input_file}" -o "{output_directory}/preset-{preset_without_spaces}.mp4"'
        _file.write(f"{command}\n")
