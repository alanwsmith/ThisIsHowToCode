---
title: Scripting DaVinci Resolve 17 (Part 2)
date: 1610663048
tags:
- DaVinci Resolve
- Automation
- Python
---

Overview
--------

Took two hours to figure out how to get a script to run. Now I can acutally try to do something with them. 


This is a lot of me looking at other code and documentation to try to figure out how to do what I'm after. There's very little online about this. Depending on what I find, it has me thinking about Adobe scripting. Setting a greenscreen was much easier on DaVinci, but if I only have to define it once in Adobe and can script it. That would be worth looking at. 


### Notes:

- Script file location:

    C:\Users\alan\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility\davinci_resolve_17_script_test_1.py


- Doc folder:

    C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting



- via: This Page: https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=103007 there's a `GetHelp()` command you can run. e.g. 

        resolve = app.GetResolve()
        print(resolve.GetHelp())
    
    And then for the classes:
                
        resolve = app.GetResolve()
        print(resolve.GetHelp('Loader'))

    That script outputs the lists of classes. 
    
    (TKTKTK link to file that has teh output list of all the classes that's in the same folder as this file)

- This is a notes from the TKTKTKT-PATH Documentation:

        
    Getting values: 

    Invoke "Project:GetSetting", "Timeline:GetSetting" or "MediaPoolItem:GetClipProperty" with the appropriate property key. 

    To get a snapshot of all queryable properties (keys and values), you can call "Project:GetSetting", "Timeline:GetSetting" or "MediaPoolItem:GetClipProperty" without parameters (or with a NoneType or a blank property key). 

    Using specific keys to query individual properties will be faster. Note that getting a property using an invalid key will return a trivial result.




### Links

- https://gist.github.com/X-Raym/2f2bf453fc481b9cca624d7ca0e19de8
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=102648
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=53385
- https://forum.blackmagicdesign.com/viewtopic.php?f=22&t=42488
- https://documents.blackmagicdesign.com/UserManuals/Fusion8_Scripting_Guide.pdf

