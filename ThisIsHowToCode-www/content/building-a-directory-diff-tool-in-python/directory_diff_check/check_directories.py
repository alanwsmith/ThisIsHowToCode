#!/usr/bin/env python3

import glob
import hashlib

from os.path import isfile


def sha_sum_256(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file_to_hash:
        for chunk in iter(lambda: file_to_hash.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

# source_directory = 'test_dirs/identical_directories/a'
# destination_directory = 'test_dirs/identical_directories/b'

# source_directory = 'test_dirs/missing_dest_file/a'
# destination_directory = 'test_dirs/missing_dest_file/b'

source_directory = 'test_dirs/invalid_dest_file/a'
destination_directory = 'test_dirs/invalid_dest_file/b'

source_files = [
    file for file in glob.glob(
        f"{source_directory}/**/*",
        recursive=True
    )
    if isfile(file)
]

destination_files = [
    file for file in glob.glob(
        f"{destination_directory}/**/*",
        recursive=True
    )
    if isfile(file)
]

file_details = {}

for source_file in source_files:
    file_sub_path = source_file.replace(
        f"{source_directory}/",
        ''
    )

    file_details[file_sub_path] = {
        "source": True,
        "dest": False,
        "sha256": sha_sum_256(source_file),
        "valid": False,
    }

for destination_file in destination_files:
    dest_sub_path = destination_file.replace(
        f"{destination_directory}/",
        ''
    )

    if dest_sub_path in file_details:
        file_details[dest_sub_path]['dest'] = True

        dest_sha_sum = sha_sum_256(destination_file)

        if dest_sha_sum == file_details[dest_sub_path]['sha256']:
            file_details[dest_sub_path]['valid'] = True

missing_files = []

# Find missing files
for file_sub_path, file_detail in file_details.items():
    if not file_detail['dest']:
        missing_files.append(file_sub_path)

# Print missing files
print(f"Missing files: {len(missing_files)}")
for missing_file in missing_files:
    print(missing_file)

# Find invalid files
invalid_files = []

for file_sub_path, file_detail in file_details.items():
    if not file_detail['valid']:
        invalid_files.append(file_sub_path)

# Output invalid files
print(f"Invalid files: {len(invalid_files)}")
for invalid_file in invalid_files:
    print(invalid_file)
