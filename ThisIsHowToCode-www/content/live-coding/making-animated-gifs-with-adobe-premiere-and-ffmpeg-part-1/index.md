---
title: Making Animated GIFs with Adobe Premiere and ffmpeg (Part 1)
date: 1611547528
tags:
- Live Coding
- ffmpeg
- Adobe Premiere
---

TODO: Get ImageMagik installed and test the conversion in this answer https://superuser.com/a/556031/85635


I used [GIF Brewery](https://gfycat.com/gifbrewery) to make GIFs on my Mac. Since moving to Windows, I haven't found a good replacement... Until now. 

In this session, I figure out how to get Adobe Premiere to setup the loop and then export an initial cropped file. Running that through ffmpeg give me a nice quality GIF at whatever size I specify. (Took longer than expected to figure out what was going on with the way the Premiere exports stuff, but I finally got a handle on it.)

Now that I've to this working, I can setup some automation so that I only have to do the export from Premiere and the ffmpeg can pick up the files and create the GIFs targated at a certain size. 

The finale ffmpeg command I ended up with is:

    ffmpeg -ss 0 -i neo-blocking.gif -filter_complex "[0:v] fps=12,scale=480:-2,split [a][b];[a] palettegen [p];[b][p] paletteuse" output-1.gif

It was from [this page](https://engineering.giphy.com/how-to-make-gifs-with-ffmpeg/). That one keeps a single pallet for the entire GIF. There's a version with pallets for each from on the page as well:

    ffmpeg -ss 0 -i neo-blocking.gif -filter_complex "[0:v] fps=12,scale=480:-2,split [a][b];[a] palettegen=stats_mode=single [p];[b][p] paletteuse=new=1" output-2.gif

There's another one to try from [this SuperUser answer](https://superuser.com/a/556031/85635)

    ffmpeg -ss 0 -i neo-blocking.gif -vf "fps=12,scale=480:-2:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output-3.gif

And:
    
    ffmpeg -ss 0 -i neo-blocking.gif -vf "fps=12,scale=480:-2:flags=lanczos,split[s0][s1];[s0]palettegen=stats_mode=diff[p];[s1][p]paletteuse" -loop 0 output-4.gif

Where the `palettegen` is setup to focus only on the moving parts of the image. And this one where the palettegen is setup for each frame:

    ffmpeg -ss 0 -i neo-blocking.gif -vf "fps=12,scale=480:-2:flags=lanczos,split[s0][s1];[s0]palettegen=stats_mode=single[p];[s1][p]paletteuse=new=1" -loop 0 output-5.gif



### Links

- https://www.pexels.com/video/close-up-video-of-women-leaning-on-each-other-s-face-4763990/
- https://www.quora.com/How-do-I-change-the-aspect-ratio-in-Adobe-Premiere-Pro
- https://helpx.adobe.com/premiere-pro/user-guide.html/premiere-pro/using/source-monitor-program-monitor.ug.html#button-editor
- https://helpx.adobe.com/premiere-pro/using/playing-assets.html
- https://video.stackexchange.com/questions/10461/adobe-premiere-pro-cc-crop-a-video-and-export-at-the-exact-cropped-size 
- https://medium.com/@Peter_UXer/small-sized-and-beautiful-gifs-with-ffmpeg-25c5082ed733
- https://superuser.com/a/556031/85635
- https://ffmpeg.org/ffmpeg-filters.html#paletteuse


