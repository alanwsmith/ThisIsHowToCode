#!/usr/bin/env pyhton3

import json
import time

from shutil import copy2

"""

NOTE: Make sure to read the notes in the web page
to understand why you have to have an source
`original.settings.json` file.

/Users/alans/Library/Application Support/Code/User/original.settings.json

"""

live_settings_path = '/Users/alans/Library/Application Support/Code/User/settings.json'
original_settings_path = '/Users/alans/Library/Application Support/Code/User/original.settings.json'

copy2(live_settings_path, original_settings_path)

with open(original_settings_path, 'r') as json_file:
    json_lines = json_file.readlines()

# The original version of the settings file had a comment
# on the first line. This removes that. It hasn't come
# back, but leaving this here in case it does.
# json_lines.pop(0)

json_string = ''.join(json_lines)

json_data = json.loads(json_string)

themes = [
    "GitHub Light",
    # "Default High Contrast",
]

with open('font_size_test_input.html', 'r') as _input_file:
    input_template = _input_file.readlines()

# Clear the file so it starts with an empty setup.
with open('font_size_sampler.html', 'w') as sample_file_clear:
    pass

time.sleep(4)

for font_size in range(8, 37, 1):
    for theme in themes:
        json_data['workbench.colorTheme'] = theme
        json_data['editor.fontSize'] = font_size

        with open(live_settings_path, 'w') as json_output:
            json.dump(json_data, json_output, sort_keys=True, indent=2)

        with open('font_size_sampler.html', 'w') as sample_file:
            print(font_size)
            for output_line_number, output_line_text in enumerate(input_template, start=1):
                # Just output the line, don't prepend with line numbers
                sample_file.write(output_line_text.format(font_size))

                # if output_line_number == 1:
                #     sample_file.write(output_line_text)
                # else:
                #     if output_line_number % 10:
                #         display_number = output_line_number % 10
                #     else:
                #         display_number = output_line_number
                #     sample_file.write(
                #         f"{display_number} {output_line_text.format(font_size)}"
                #     )


        # Note that this has to be outside the file writing `with`
        # so the filehandle is closed for long enough for VS Code
        # to be able to grab the change.
        time.sleep(9)
