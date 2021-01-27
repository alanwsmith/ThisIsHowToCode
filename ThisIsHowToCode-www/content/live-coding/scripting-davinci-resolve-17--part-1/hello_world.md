---
title: Hello World DaVinci Resolve Script
date: 1610672553
tags:
- Code
- DaVinci Resolve
---

This is a copy of all the stuff that I tried during the session. All the commented out stuff is what didn't work. The three lines at the end are what got me going. 

{{< highlight python "linenos=table" >}}
#!/usr/bin/env python

# import os 
# os.environ["PYTHONPATH"] = "C:\\ProgramData\\Blackmagic Design\\DaVinci Resolve\\Support\\Developer\\Scripting\\Modules\\"


# import imp
# lib = 'C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\fusionscript.dll'
# dvr_script = imp.load_dynamic('fusionscript', lib)


# Create the instances you need...
# resolve = dvr_script.scriptapp('resolve')
# projectManager = resolve.GetProjectManager()

# print(dir(dvr_script.scriptapp()))

# print(dvr_script.scriptapp('StartHost'))

# print(dvr_script.scriptapp('GetHostList'))

# resolve = dvr_script.scriptapp('Resolve')
# projectManager = resolve.GetProjectManager()



# print(dir(dvr_script))


# print("Hello, Reslove")

# import DaVinciResolveScript as dvr_script
# resolve = dvr_script.scriptapp("Resolve")
# #fusion = resolve.Fusion()
# projectManager = resolve.GetProjectManager()
# projectManager.CreateProject("Hello Scripting")



# import imp
# lib = 'C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\fusionscript.dll'
# dvr_script = imp.load_dynamic('fusionscript', lib)


# import imp
# lib = 'C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\fusionscript.dll'
# dvr_script = imp.load_dynamic('fusionscript', lib)

##########

'''
This is how to get details from the help docs

resolve = app.GetResolve()
print(resolve.GetHelp('Loader'))
'''

##########

resolve = app.GetResolve()
projectManager = resolve.GetProjectManager()
projectManager.CreateProject("Hello Scripting")
{{< / highlight >}}