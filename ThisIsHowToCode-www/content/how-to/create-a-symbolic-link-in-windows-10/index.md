---
title: How-To Create A Symbolic Link In Windows 10
date: 1610675692
tags:
- Windows 10
- Needs Video
---

To create a symbolic link:

- Run Command Prompt as an Administrator 

        (This won't work with PowerShell)

- To link a file:

        mklink PATH_TO_MAKE SOURCE_PATH
    
- And for a directory:

        mklink /D PATH_TO_MAKE SOURCE_PATH


### Notes 

- See if there's a way to do this with PowerShell
- Add hard links

        # file:
        mklink /H PATH_TO_MAKE SOURCE_PATH

        # directory:
        mklink /J PATH_TO_MAKE SOURCE_PATH
        