---
banner: This Is How To Code
title: Scripting DaVinci Resolve 17 - Part 3
date: 1610851224
---

(Note: I'm using a new keyboard in this one, so there, a bunch of me banging around)

Picking up where we left off in part 2, trying to see what we can do with the automation.

- made a help_text.py file that dumps out the output stuff. need to compare it to the read me to see if there's more stuff in it. 

- it doesn't look like there's a way to add tracks via a script. 

- at the end of the sesison, I stumbled onto something called "EDL" turns out that's for Edit Decision List. Going to look into those to see if that will work. 





### Links

- http://timlehr.com/python-scripting-in-davinci-resolve/
- https://documents.blackmagicdesign.com/UserManuals/Fusion8_Scripting_Guide.pdf
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=100770
- https://diop.github.io/davinci-resolve-api/#/?id=timeline
- https://deric.github.io/DaVinciResolve-API-Docs/
- https://www.steakunderwater.com/wesuckless/viewtopic.php?t=3116
- https://gist.github.com/X-Raym/2f2bf453fc481b9cca624d7ca0e19de8
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=94911
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=113040
- https://forum.blackmagicdesign.com/viewtopic.php?f=12&t=82788
- https://www.steakunderwater.com/wesuckless/viewtopic.php?f=35&t=2012&sid=f37e5dd965a51a8e183af818f92f5126
- https://www.w3schools.com/python/ref_string_strip.asp
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=42299
- https://forum.blackmagicdesign.com/viewtopic.php?f=32&t=95917
- https://forum.blackmagicdesign.com/viewtopic.php?f=33&t=96309
- https://blog.frame.io/2019/03/29/conforming-with-resolve/
- https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=117270
- https://documents.blackmagicdesign.com/UserManuals/Fusion8_Scripting_Guide.pdf
- 



---

Found this:

Timeline
  AddTrack(trackType, audioTrackType)             --> Bool               # Adds a track of the given type ("audio", "video" or "subtitle") to the timeline. The audioTrackType is only needed for audio tracks and is one of "mono", "stereo", "5.1film", "7.1film", or "adaptive".
  DeleteTrack(trackType, index)                   --> Bool               # Deletes a track of the given type at the specified index (int). 1 <= index <= GetTrackCount(trackType)
  SetTrackEnable(trackType, index, enable)        --> Bool               # Enables or disables the given track. The enable parameter is a boolean value.
  GetIsTrackEnabled(trackType, index)             --> Bool               # Returns whether a track is enabled or not.
  SetTrackLock(trackType, index, lock)            --> Bool               # Locks or unlocks the given track. The lock parameter is a boolean value.
  GetIsTrackLocked(trackType, index)              --> Bool               # Returns whether a track is locked or not.
  SetClipsLinked([items], link)                   --> Bool               # Links or unlinks the given clips (TimelineItem objects). The link parameter is a boolean value.

TimelineItem
  GetClipEnabled()                                --> Bool               # Returns whether a clip is enabled or not.
  SetClipEnabled(enable)                          --> Bool               # Enables or disables a clips. The enable parameter is a boolean value.
  SetNodeLocked(nodeIndex, lock)                  --> Bool               # Locks or unlocks a Color page node at the given nodeIndex (int). The lock parameter is a boolean value.

  here: https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=113040

