---
title: "How-To: Sort By Size On The Command Line"
---

### Goal

I've got 1,142 sample video files with various compressions settings that I [built with an automatic Handbrake script](/automating-handbrake/). The files show up sorted by name, but I want them sorted by size to get a better idea of which ones I should look at.

### Solution 

The solution I ended up with was to combine the `ls` and `awk` commands. The `ls` command does the listing an sorting while the `awk` command parses the data down to just the columns I need. Using `awk` for this type of parsing is not something you'd want to do for a system you're going to put into production as you'll see in the video, but for my need it worked just fine. 

Here's the command that displays the text on the command line:

    ls -lSh | awk '{print $5 "\t" $9}'

And here's the version that writes to a file

    ls -lSh | awk '{print $5 "\t" $9}' > report.txt

(In the video, I used `../report.txt` to create the file one folder up. It's a little clearer without that so I'm leaving it as just `report.txt` here.)


### Quick Reference

- I used `man ls` to get to the "manual" file (aka a "man page") for the ls command. `man` works with most command on a mac and linux. (TKTKTKT: Figure out what the man command equivalent on a Windows machine is)
- The first thing to know about man pages is that you just need to type `q` to get you out of one. 
- The `/` key is how you start a search once you're in a man page. Just do something like `/display` to search for the word "display". Note that the search is [case sensitive](/tktktk/). So, your search will find "display" with a lower case "d", but not "Display" with an upper case "D". 
- You can do case insensitive searches by typing `-i` at the `:` which will flash a message like `Ignore case in searches  (press RETURN)`. After that, `/display` will also match "Display". 
- If you want to turn off the case insensitive search for some reason just to `-i` again. 



### Links

- TKTKTK: Setting Up Your Mac Terminal
- TKTKTK: Setting Up Your Windows Terminal
- [AWK - Basic Examples - Tutorialspoint](https://www.tutorialspoint.com/awk/awk_basic_examples.htm)
- [bash - How do I echo just 1 column of output from ls command? - Unix & Linux...](https://unix.stackexchange.com/questions/101580/how-do-i-echo-just-1-column-of-output-from-ls-command)
- [Google Search: awk basics](https://www.google.com/search?client=safari&rls=en&q=awk+basics&ie=UTF-8&oe=UTF-8)
- [Google Search: awk ls](https://www.google.com/search?client=safari&rls=en&q=awk+ls&ie=UTF-8&oe=UTF-8)
- [Google Search: grep not](https://www.google.com/search?client=safari&rls=en&q=grep+not&ie=UTF-8&oe=UTF-8)
- [Google Search: ls show only certainly columns](https://www.google.com/search?client=safari&rls=en&q=ls+show+only+certainly+columns&ie=UTF-8&oe=UTF-8)
- [linux - Can I show certain columns in ls -l command? - Super User](https://superuser.com/questions/1432701/can-i-show-certain-columns-in-ls-l-command)
- [ParsingLs - Greg's Wiki](http://mywiki.wooledge.org/ParsingLs)
- [Stack Overflow: awk '{print $9}' the last ls -l column including any spaces...](https://stackoverflow.com/questions/1447809/awk-print-9-the-last-ls-l-column-including-any-spaces-in-the-file-name)
- [Stack Overflow: Negative matching using grep (match lines that do not contain foo)](https://stackoverflow.com/questions/3548453/negative-matching-using-grep-match-lines-that-do-not-contain-foo)
