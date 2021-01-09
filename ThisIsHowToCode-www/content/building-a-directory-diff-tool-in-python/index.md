---
title: Live Coding A Directory Diff Tool In Python
date: 1609801779
---

### Video


-- Video goes here when it's ready --


### Warning - Inelegant Code Ahead

This is not elegant code. Except for one function at the top, it's one big procedure from top to bottom. Coding is keeping context in your head. That's harder to do when things aren't broken into parts. This script is riiiight at the limit for me being able to hang-on to the entire thing.

This also isn't how I code most of the time. And, there are times when you __absolutely should not__ run in this type of procedural manner without automated tests (TKTKTK: Video about procedural code). But, it's a tool in the toolkit. For small jobs with little risk it can be just fine.



### Overview

My photography archive is spread out across multiple hard drives and directories. I'm consolidating it down into one location. I want to make _really_ sure that all the files end up getting moved and none of them get corrupted.

Solution: Build a script that verifies everything is in the right place and had the right bits.

### Details

- The script I ended up with is a bit of a hack, but it works.
- While this would have been a good time to practice a little TDD, the script deals with the file system and that's always tripped me up. In retrospect, there are parts I could have tested. It's just a one off script though. So, I opted to test it manually.
- The script is used by setting two directories. A source and a destination.
- When the script is run, it does two things: 1) Make sure that all the files in the source directory show up in the destination directory, and 2) Make sure that the contents of the files are identical.
- I'm using a sha256 hash of the files to do the comparison that ensure they are the same.
- The script produces a simple report of missing files and invalid files. If any files have problems their relative paths are there so I can troubleshoot.
- Files that are missing show up on the invalid list. That's a little duplication and not expected, but I'm fine with it for this script. If I was going to put this into production and run it repeatedly I'd adjust that. But, I only need to run this once right now and will maybe run it a handful of times in the future.

### Notes

This is the method I'm using to generate the sha256 hash sum signatures for each file:

{{< highlight python "linenos=table" >}}
def sha_sum_256(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file_to_hash:
        for chunk in iter(lambda: file_to_hash.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()
{{< /highlight >}}

There are a couple parts of that I don't understand. So:

- TODO: Figure out what `b''` does at the end of the lambda.
- TODO: Figure out how lambdas work.

### Links

- TKTKTK globs and how glob works
- [15.1. os — Miscellaneous operating system interfaces — Python 2.7.18 documentation](https://docs.python.org/2/library/os.html#os.listdir)
- [hashlib — Secure hashes and message digests — Python 3.9.1 documentation](https://docs.python.org/3/library/hashlib.html)
- [MD5 - Wikipedia](https://en.wikipedia.org/wiki/MD5#Collision_vulnerabilities)
- [python - Generating an MD5 checksum of a file - Stack Overflow](https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file/3431838#3431838)
- [python - How do I list all files of a directory? - Stack Overflow](https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory)
- [python directory list recursive - Google Search](https://www.google.com/search?client=safari&rls=en&q=python+directory+list+recursive&ie=UTF-8&oe=UTF-8)
- [python get list of files in a directorty - Google Search](https://www.google.com/search?client=safari&rls=en&q=python+get+list+of+files+in+a+directorty&ie=UTF-8&oe=UTF-8)
- [rsync - Google Search](https://www.google.com/search?newwindow=1&client=safari&rls=en&ei=QrfzX9XpCIrW5gLrhpXYBw&q=rsync)
- [rsync(1) - Linux man page](https://linux.die.net/man/1/rsync)
- [scripting - Python recursive folder read - Stack Overflow](https://stackoverflow.com/questions/2212643/python-recursive-folder-read)
