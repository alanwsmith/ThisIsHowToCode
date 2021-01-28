#!/usr/bin/env python

print("\n\n\n")
print("Running Script...")

### Make sure it's working. 
# print("Hello, World")
# print("Is this thing on?")


### This is the first sample that I got working
# resolve = app.GetResolve()
# projectManager = resolve.GetProjectManager()
# projectManager.CreateProject("Hello Scripting")


### Help commands
# resolve = app.GetResolve()
# print(resolve.GetHelp())

# resolve = app.GetResolve()
# print(resolve.GetHelp('Loader'))


### Check example scripts

### See about getting the Fusion object from the docs
### and looking at it (line 75)




#### Attempt 1

# resolve = app.GetResolve()
# projectManager = resolve.GetProjectManager()
# project = projectManager.GetCurrentProject()

# mediapool = project.GetMediaPool()

# print(dir(mediapool))
# print(mediapool.GetClipMatteList())

# clips = resolve.GetMediaStorage()

# print(dir(clips))

# print(clips.GetFileList())


### Attempt 2

# This adds clips from the given folder to the media pool 
# then prints out details on them. 

# mediaPath = 'D:\\This_Is_How_You_Program_Videos\\live-coding\\scripting-davinci-resolve--part-2\\test-clips'
# resolve = app.GetResolve()
# projectManager = resolve.GetProjectManager()
# project = projectManager.GetCurrentProject()

# mediapool = project.GetMediaPool()
# rootFolder = mediapool.GetRootFolder()
# clips = resolve.GetMediaStorage().AddItemListToMediaPool(mediaPath)

# for clip in clips:
#     print(clip)
#     print(dir(clip))



### Attempt 3

# This adds the clips found in the folder to the 
# timeline, but they are all added to the same 
# track.

mediaPath = 'D:\\This_Is_How_You_Program_Videos\\live-coding\\scripting-davinci-resolve--part-2\\test-clips'
resolve = app.GetResolve()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()

mediapool = project.GetMediaPool()

print(dir(mediapool))

rootFolder = mediapool.GetRootFolder()
clips = resolve.GetMediaStorage().AddItemListToMediaPool(mediaPath)

timelineName = "Timeline Scripted 3"
timeline = mediapool.CreateEmptyTimeline(timelineName)

print(dir(timeline))

for clip in clips:
    mediapool.AppendToTimeline(clip)

