---
title: "My Video Production Process (V1) With DaVinci Resolve 17"
date: 1610243800
layout: blog
category: How-To
tags:
- DaVinci Resolve
- Video Production
---




This is the process I go through to assemble a video 

(TKTKTK This page is a work in progress)


- Rename Media If Necessary 

	- If you're importing from a bunch of clips from multiple sources, rename the clips with leading "01-", "02-", etc... to pair them up and keep them together

---


- Start up DaVinci Resolve

- Create and name a new project 

- Setup the Project

	- Resolution: 3860x2160
	- Frame rate: 29.967 (TKTKTK: Do test with 24 FPS)
	- Playback framerate: 29.967 (TKTKTK)



- Select media from the Media tab

- Switch to Edit Tab

- Add a solid color 

	- Click Effects Library in the secondary top menu
	- Choose "Solid Color" from favorites and drag it into a track
	- If it's not in favorites for some reason, search for "Color" and you'll find it under "Generators"

- Set the color

	- Click on the color in the timeline 
	- Look in the inspector tab under "Video -> Generator" and click the color chip to change the color
	- Initial color you're using is: #afafaf



	Background color you used initally on Jan. 13, 2021:
		- R: 154
		- G: 99
		- B: 73
		
	Another color to look at is:
		- R: 104
		- G: 69
		- B: 0





- Drag the desktop clip onto the timeline in track 2

- Tranform the initial desktop clip:

	- Zoom: .93
	- Position X: -134
	- Position Y: 75

- Add Drop Shadow (which you can leave at it's defaults)

	- It's in Favoraites
	- If it's not in favorites for some reason, click "Open FX" in the "Effects Library" and search for "Drop"	
	- Or, find it under: Effects Library -> Open FX -> Filters -> Resolve FX -> Drop Shadow
	- Defaults which you can use are:
		- Shadown Strenght: 0.5
		- Drop Angle: 37.5
		- Drop Distance: 0.05
		- Blur: 0.55
		- Color: #000000

- Drag the desktop on the timeline again

	- This is the full screen version that you won't mess with:
	- TKTKTK: Figure out if you want to screen the full screen back a little. 


- Drag talking head clip on the timeline once

- Align clips via Audio Waveform:

	- Ctrl+a to select all the clips
	- Right click on a clipn
	- Coose: Auto Align Clips -> Based Off Waveform 
	
- Press the down arrow until you hit the end of the shortest clip from the group

- Remove the excess footage:

	- Select all with Ctrl+a
	- Cut with Ctrl+b
	- Click on the track(s) that need to be deleted and remove them
	
- Expand the solid color clip track so that it goes to the end of the shortest of the other clips	
	
- Mute all the tracks except for the last one (which will be from the talking head clip)

- Set contrast, exposure, highlights, and shadows for talking head clip

- Do color correction for talking head clip

- Do chroma key for talking head clip

- Set window for talking head clip:

	- Size: 74.9
	- Softness (all of them): 0

- Duplicate the talking head track

	- Deselect everything then hold Alt then click on the talking head clip and drag it up to a new track. 

- Resize the new talking head track to:

	- Zoom: .420
	- Position X: 1480
	- Position Y: -640
	
- Add Fade-in and Fade-out

- Make cuts

- Apply transisions to cuts



