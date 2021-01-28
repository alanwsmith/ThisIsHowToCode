---
title: Scripting DaVinci Resolve - Part 1
date: 1610645798
draft: true 
tags:
- DaVinci Resolve
- Python
- Automation 
---


Overview
--------

This one was a slog. 

I use DaVinci Resolve to edit these vidoes. In this session I pound my head against the wall for two hours until I get a script running. Now that I know how to do it, I'll move on to seeing how much of the editing process I can automate. 

There's not a lot of code writing in this one, but it's a good look at the process of getting something setup that doesn't have the greatest documentation. 

(If you want to see me actually work on coding, skip to [Part 2](scripting-davinci-resolve-17--part-2/))


TKTKTK Video goes here


# The Solution 

- The first trick is that I needed to install Python 3.6 specifcially. I already had Python 3.9, but Resolve wouldn't work with that.

    Installer for the different verisons of Python are on [this page](https://www.python.org/downloads/windows/). However, there's not an installer for the most recent version (3.6.12). The most recent one I found was 3.6.8. So, I used that. 

- The next step was to ignore everything in the directions and use `app.GetResolve()` for the script. I made a file at:

        %APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility\hello_world.py

    which, for me was:

        C:\Users\alan\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility\hello_world.py

- The script contents of `hellow_world.py` are:

        #!/usr/bin/env python

        resolve = app.GetResolve()
        projectManager = resolve.GetProjectManager()
        projectManager.CreateProject("Hello Scripting")

- The script shows up under the top menu at:

        Workspace -> Scripts -> hello_world
    
    Run it, and it'll make a new project named "Hello Scripting"

- That's it. 

    Took me two hours and a bunch of rabbit holes to get there, but it's working. 


### Miscelaneous Notes

- To get to the docs: 

    - Help -> Documentation -> Developer
    - Once you're in there, click into the Scripting folder

- I tried setting the environmental variables, but nothing I did seemed to work. This might be because I'm on the free version of Resolve and there are some limitations. Not really sure, but that went by the way side when I get the `app.GetResolve()` solution in place. 

- I don't know how to setup Python Virtual Environments on Windows yet. I could have done it in PyCharm, but that wouldn't have worked for DaVinci. There's a Windows port of pyenv that I'll look at. I want to do more research before picking a path. 

- While I was initially working to get the module working, I copied:
        C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules\DaVinciResolveScript.py

    To:
        C:\Users\alan\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility\DaVinciResolveScript.py
    
    That worked in terms of getting the module to load, but still wasn't getting the example script to run. 

    I ended up removing that file. Leaving the note here in case something changes in the future and it's worth a revisit. 

- The other way I got the module to load was like this:

        import imp
        lib = 'C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\fusionscript.dll'
        dvr_script = imp.load_dynamic('fusionscript', lib)

    As above, that still didn't get the example running. Leaving it here though in case it needs a revisit later. 

### Errors

When I was first trying to get the module to load, I was hitting this error:

    Traceback (most recent call last):
        File "C:\Users\alan\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility\hw.py", line 12, in <module>
            import DaVinciResolveScript as dvr_script
    ModuleNotFoundError: No module named 'DaVinciResolveScript'

I couldn't get PYTHONPATH setup to work with it. So, I ended up just copying the `DaVinciResolveScript.py` file in directly as listed above. That fixed the module loading error, but more errors followed...

Other errors I hit while trying to figure stuff out:

    Traceback (most recent call last):
        File "C:\Users\alan\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility\hw.py", line 14, in <module>
            fusion = resolve.Fusion()
    AttributeError: 'NoneType' object has no attribute 'Fusion'

And:

    Traceback (most recent call last):
        File "C:\Users\alan\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility\hw.py", line 10, in <module>
            projectManager = resolve.GetProjectManager()
    AttributeError: 'NoneType' object has no attribute 'GetProjectManager'

And:

    Traceback (most recent call last):
        File "C:\Users\alan\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility\hw.py", line 20, in <module>
            projectManager = resolve.GetProjectManager()
    TypeError: 'NoneType' object is not callable

And:

    Traceback (most recent call last):
        File "<nofile>", line 1, in <module>
    TypeError: 'NoneType' object is not callable

This was all in an effort to get this to work:

    import DaVinciResolveScript as dvr_script
    resolve = dvr_script.scriptapp("Resolve")
    fusion = resolve.Fusion()
    projectManager = resolve.GetProjectManager()
    projectManager.CreateProject("Hello Scripting")

Moving over to using `app.GetResolve()` made all those issues go away. 


### Links From The Session 

(NOTE: I just moved to windows and don't have a tool setup yet to automatilly grab the titles for these. So, they're just URLs for now.)

- https://github.com/pressreset/resutil/blob/master/resutil.py
- https://deric.github.io/DaVinciResolve-API-Docs/
- https://documents.blackmagicdesign.com/UserManuals/Fusion8_Scripting_Guide.pdf
- https://diop.github.io/davinci-resolve-api/#/
- https://deric.github.io/DaVinciResolve-API-Docs/
- https://www.steakunderwater.com/wesuckless/viewtopic.php?t=3116
- http://timlehr.com/python-scripting-in-davinci-resolve/
- https://drive.google.com/file/d/1CMzfr3S1IR9rkFtDHzavjN93ZBqTuzjC/view
- https://deric.github.io/DaVinciResolve-API-Docs/
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=103007
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=116859
- https://stackoverflow.com/questions/1489599/how-do-i-find-out-my-python-path-using-python
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=103007
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=99270
- https://www.steakunderwater.com/wesuckless/viewtopic.php?t=3116
- https://deric.github.io/DaVinciResolve-API-Docs/
- https://diop.github.io/davinci-resolve-api/#/
- https://documents.blackmagicdesign.com/UserManuals/Fusion8_Scripting_Guide.pdf
- http://timlehr.com/python-scripting-in-davinci-resolve/
- https://stackoverflow.com/questions/5971312/how-to-set-environment-variables-in-python
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=121798
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=87567
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=100770
- https://www.steakunderwater.com/wesuckless/viewtopic.php?t=3116
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=113252
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=96281
- https://askubuntu.com/questions/470982/how-to-add-a-python-module-to-syspath
- https://stackoverflow.com/questions/44749636/what-path-to-install-python-3-6-to-on-windows#:~:text=The%203.6%20installer%20suggests%20C,any%20other%20software%20on%20Windows.
- https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages
- https://www.steakunderwater.com/wesuckless/viewtopic.php?t=3116
- https://www.python.org/downloads/windows/
- https://www.python.org/downloads/release/python-3612/
- https://www.python.org/downloads/release/python-3612/
