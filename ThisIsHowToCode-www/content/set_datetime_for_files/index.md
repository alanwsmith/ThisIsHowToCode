---
title: Setting The Date And Time Of The Posts
layout: blog
date: 1610240272
---

I decided when I first started the site that I didn't want dates and times to show up. I'll note when stuff is time sensative and keep things up to date, but dates themselves are a distraction. (I feel the same way about my blog which is why I only do the month and year for them)

Anyway, I figure out that I can use epoch timestamps for the dates. I'm not trying to hide the dates, just obfuscate them and that does a great job. 

The trick is that I made a whole bunhc of posts without dates in the YAML front matter. The good news is that I can still figure out when the dates are. 

I ran this command on my mac to pull the `stat` data for each file in the content directory. 

    find . -name '*.md' -exec stat {} +

It finds all the `.md` (markdown) files and runs `stat` on them. That command outputs some details including (TKTKTK I think it's when the inode was created, but need to verify) the TKTKTK timestamp that I can use. 

Now, all I need to do is turn those timestamps into epoch time format and insert them into the files. 

That'll make a good project. 

(Look in the `output_from_find.txt` for the data to work with) 

NOTE: I'm not sure if those are all accurate. Another source to look at is the Videos. Not sure about the timestamps, but the filenames are generally date/time strings. 



