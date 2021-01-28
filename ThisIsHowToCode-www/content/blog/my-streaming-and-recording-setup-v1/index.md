---
title: "My Stream/Recording Setup"
date: 1611598351
tags:
- Blog
- Behind The Scenes
---

First off, you don't need all this to get started. It took me a year to put this together (not including all the stuff I had from my former life as a photographer). I [got started](https://www.youtube.com/watch?v=XgAM4EjB5WM) with the built-in webcam. They're prefectly fine for getting up and running. 

With that said, here's what my setup looks like as of January 2021:

### PC

- 2016 era Windows 10 Desktop PC
- [Insignia 43" 4K TV](https://www.amazon.com/gp/product/B086VRY8GZ)
- [Moonlander Keyboard](https://www.zsa.io/moonlander/)
- [Logitech G502 Hero Mouse](https://www.amazon.com/Logitech-G502-Performance-Gaming-Mouse/dp/B07GBZ4Q68)
- [Elgato 4K60 Pro MK.2 PCIe Capture Card](https://www.amazon.com/gp/product/B07VWXCXM7)
- [Elgato Stream Deck](https://www.amazon.com/gp/product/B06XKNZT1P)
- [11 Port USB Hub](https://www.amazon.com/gp/product/B07DW646GY)
- [32 Foot HDMK 2.0 Cable](https://www.amazon.com/gp/product/B07ZVDF2SS)
- [32 Foot USB 3.0 Extension Cable](https://www.amazon.com/gp/product/B07QDXJR9Z)

_Notes:_

- The PC was assembed from parts I bought off a co-worker who's a gamer and was looking to upgrade. The CPU is a Ryzen 5 1600 Six-core 3.20GHz with 16 GB of RAM and an NVIDA GeForce GTX 1080. This is overkill for streaming/recording but not bad for video editing. I'm going to add more RAM to hopefully help that even more.
- I didn't start with the Windows system. I started with a 2015 MacBook Pro. I could code on it, capture the webcam and desktop in OBS and stream without much issue. The only thing that would happen would be the fans spinning up from time to time. 
- I use the 43" TV for a monitor because I have the screen about 5' away. The reason is all about the camera position. I want the camera pushed back that far to get the perspecive I'm after. One where you can see the keyboard without having lots of wide angle distortion from a closer position. It's not the most flattering angle, but it works better for the scene.
- The Moonlander keyboard is new to me. I wanted to try a split keyboard and lots of folks from a discord I'm in spoke highly of it. I'm a couple weeks in and so far I'm liking it. Though changing keyboards at the same time I moved from Mac to Windows is a lot at one time. One fear I have is that it may make the videos less accessible. Or, more intimidating. As in, seeing a fancy keyboard may make some folks think you have to have one in some way. (Hopefully, I'm overthinking that.)
- The mouse doesn't really matter, but since I was putting everything else in, I figured I'd include it. It moves the pointer and clicks just fine. No complaints.
- The long cables are so I can put the computer in another room to get rid of fan noise. Noise suppression would take care of it, but after years working on just a laptop, I like the quiter environment.
- The USB hub is so I can connect everything without having to run tons of long cables. Combined with the cable it works fine, but I haven't really pushed it by sending lots of data. 


### Software

- [OBS](https://obsproject.com/) 
- [DaVinci Resolve 17](https://www.blackmagicdesign.com/products/davinciresolve/)
- [Elgato 4K Capture Utility](https://help.elgato.com/hc/en-us/articles/360027964472-Elgato-4K-Capture-Utility-Release-Notes)

_Notes:_

- All that stuff is free, which is amazing. 
- When I stream, I do everything directly through OBS. The green screen chroma key took a while to get right. While it's not a good a full-on, custom post-production clean up in DaVinci Resolve, it's really solid. 
- When I record VODs, I capture the desktop in OBS and the camera feed in Elgato 4K Capture Utility. I combine the two files in DaVinci Resolve (where I also chroma key out the green screen).


### Audio

- [Shure SM 58 Mic](https://www.amazon.com/gp/product/B0179T2CM8)
- [Shure Shock Mount](https://www.amazon.com/gp/product/B0002GZOSA)
- [XLR Right Angle Adapter](https://www.amazon.com/gp/product/B073X2SDMJ)
- [Boom Arm with XLR cable](https://www.bhphotovideo.com/c/product/1023480-REG/auray_bai_2x_2_sect_brdcst_arm.html)
- [Zoom H5](https://www.amazon.com/Zoom-H5-Four-Track-Portable-Recorder/dp/B00KCXMBES/)
- [USB A to B-Mini to connect H5 to PC](https://www.amazon.com/AmazonBasics-USB-2-0-Cable-Male/dp/B00NH11N5A)


_Notes:_

- I had the SM 58 and the Zoom from an earlier bout of mania. They work fine, but I might have made diffent choices if I was buying specifically for streaming/recording. 
- I like the SM 58 because it lets me get it out of frame while still sounding pretty good. Still experimenting with it's placement. (I'm doing some audio test. I'll link them up when they are done.)
- Right now, I'm just using the H5 to get sound into the computer and doing compression in OBS. I just discoverd the Zoom can do some compression as well. I'll be testing that as well.
- The XLR right angle adapter is just to help get the cord out of the way when the mic is visible. 

_Current OBS Settings_

- Noise Suppression Method: Speedx (lower CPU usage) at -39dB. (I had more success with this than RNNoise since I could dial in the level)
- Compressor Ratio: 10.00:1
- Compressor Threshold: -15.60 dB
- Compressor Attack: 6 ms
- Compressor Release: 60 ms
- Compressor Output Gain: 8.80 dB
- Compressor Sidechain/Ducking: None


### Video

- [Canon 90D body](https://www.amazon.com/Canon-Digital-Camera-Black-3616C002/dp/B07WFQYDD5)
- [Canon 16-35mm f/2.8L lens](https://www.amazon.com/Canon-16-35mm-2-8L-III-Lens/dp/B01KURGS8U)
- [C-Stand](https://www.bhphotovideo.com/c/product/112099-REG/Matthews_756140_Century_C_Turtle_Base.html)
- [Manfrotto Magic Arm](https://www.amazon.com/Manfrotto-143N-Magic-Arm-without/dp/B00281TWTY)
- [Manfrotto Super Clamp](https://www.amazon.com/Manfrotto-035RL-Super-Clamp-Standard/dp/B0018LQVIA)
- [Manfrotto Camera Bracket](https://www.amazon.com/Manfrotto-143BKT-Replacement-Camera-Bracket/dp/B00134SCCA)
- [Mini HDMI to HDMI Cable](https://www.amazon.com/gp/product/B00608XLUM)
- [25 Feet 4k HDMI Extender](https://www.amazon.com/gp/product/B00GBBSGSA)


_Notes:_

- First off, I *do not* recommend the 90D for most setups. It's not full frame which makes getting wide enough shots hard. 
- The main reason I got the 90D is because I already had the lens from my photography days.
- Speaking of lenses, that link goes to a newer model of the 16-35. Mine is the original. It's 15+ years old but it still works great. (Money spent on good glass doesn't go to waste)
- The 90D shoots 4K which is important to me when I'm recording VODs. I want those to have as long a shelf life as possible so want them as high quality as possible. If I was just streaming, I would have considered a less expensive camera that just did 1080p. 
- The C-Stand is another old piece of kit from my photography days. I use it to mount the camere so I can get it closer to the wall (which helps get the perspective I'm looking for)
- The Manfrotto pieces are what I use to attach the camera to the c-stand. More 20 year old stuff from my days as a photographer. The arm has some slop in it when tightining which makes it tricky to sight in. But, once it's lined up, it's solid. 
- Cables continue the trend of running down the hall into the other room.


### Physical Space

- [Green Chroma Key Background](https://www.amazon.com/gp/product/B017WNJS3M)
- [Softboxes](https://www.amazon.com/gp/product/B07NBP6D98)
- [2700K Warm White 100W Equivalent LED Bulbs](https://www.amazon.com/gp/product/B07QJ84SDN)
- [Blackout Curtains](https://www.amazon.com/gp/product/B07QNSLXKR)
- [C-Stand with Arms](https://www.bhphotovideo.com/c/product/112099-REG/Matthews_756140_Century_C_Turtle_Base.html)
- [Background stand](https://www.bhphotovideo.com/c/product/1531896-REG/impact_bgs_s12_v2_background_support_system_12.html)
- [Steamer](https://www.amazon.com/gp/product/B07HF3X6Y4)
- [Floor Cord Cover](https://www.amazon.com/gp/product/B07BKSNZ7C) (so I'm less likely to trip over the long cord runs)
- [Sand bags](https://www.amazon.com/AmazonBasics-Photographic-Empty-Sandbag-Stands/dp/B07P217V6H) to put on the lightstands
- [X-Rite ColorChecker](https://www.amazon.com/gp/product/B0173FP6P8)
- [Extension Cords](https://www.amazon.com/gp/product/B07N4MY5P2)
    


_Notes:_ 

- I started with a smaller, foldable greenscreen but wanted something wider. This one is fine, but is still a little tough to deal with wrinkles. Next step is going to be to paint the wall...
- I currently have four softboxes. Two pointed directly at the background. A hairlight above me on a c-stand arm and the key light up and to the left in front of me. I'm looking at getting two more to get an even smoother spread on the background to make keying easier. 
- The bulbs that came with the softboxes were 5400K daylight balanced bulbs. I really don't like that type of bluish light. It hurts my eyes. So, I changed them out with the 2700K bulbs with their much warmer light. I manually set the color balance on the camera to match them (which I would have done with any light source, actually).
- The steamer is the only way I had a fighting chance against the wrinkles in the green screen backdrop
- Sandbags are for the light stands. The C-stands are pretty hefty but the little stands that came with the softboxes tip easily. Drop twenty pounds at their base, though, and they become very stable.
- The ColorChecker is for color balance. There's a built-in feature in DaVinci Resolve that uses it that's great. This is only for the VODs. I've got the camera set manually to match the color of the lights pretty well so it's fine in the streams. If you don't see a comparison, most folks would never know, but it's nice to clean up in post for the VODs. 
- The blackout curtains let me control the light in the room. The big reason for this is becuase the color temperature of window light is very blue compared to the bulbs I have in the softboxes. It would look pretty bad if they were both in the same scene. 
- In additon to using a C-stand to mount the camera, I use a couple to mount the key and hair lights. In fact, the keylight is on the same stand as the camera. The C-stand arm with the hairlight acts as a boom to get it above me while keeping the stand it self out of frame. 
