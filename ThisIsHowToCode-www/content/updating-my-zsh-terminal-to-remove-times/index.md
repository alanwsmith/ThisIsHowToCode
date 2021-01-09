---
title: Updating My ZSH Terminal To Remove Times
draft: true 
---

Overview
--------

Just like it says on the tin. I removed the times
that were showing up on my terminal. It's irrelevant 
info and can be a little distracting so it got the
boot. 

While taking them out, I added a section to the 
prompt that shows the website name. Makes for a nice
touch if you ask me. 

The way I stopped the initial login message was to do:

    touch ~/.hushlogin

That turns off the "Last Login" message as well as
the Message Of The Day (aka MOTD). I don't use the
MOTD so that's not a big deal. Though... I might 
use it in the future. If I do, one recommendation 
was to add `cat /etc/motd` to the top of my .zshrc 
file, but that would only output the text. I might
want to do something dynamic with it in which case
I'll need to find another option. 



### Links

- TKTKTKT ZSH
- TKTKTKT Terminals
- [Change the Terminal Message of the Day in Mac OS X](https://osxdaily.com/2007/01/30/change-the-mac-os-x-terminals-message-of-the-day/)
- [dont show login time in terminal - Google Search](https://www.google.com/search?client=safari&rls=en&q=dont+show+login+time+in+terminal&ie=UTF-8&oe=UTF-8)
- [motd without last login mac - Google Search](https://www.google.com/search?newwindow=1&client=safari&rls=en&ei=9hTpX8HIKIyG5wLh6qfwAw&q=motd+without+last+login+mac&oq=motd+without+last+login+mac&gs_lcp=CgZwc3ktYWIQAzIFCCEQoAEyBQghEKABMgUIIRCrAjIFCCEQqwIyBQghEKsCOgQIABBHUKuQAliSlAJg9pgCaABwAngAgAFriAHvApIBAzIuMpgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab&ved=0ahUKEwjBm4PhpO_tAhUMw1kKHWH1CT4Q4dUDCAw&uact=5)
- [Remove last login message but keep motd in terminal? - Ask Different](https://apple.stackexchange.com/questions/254690/remove-last-login-message-but-keep-motd-in-terminal)
- [ssh - How to prevent "Last Login:" message from showing up when using sftp? -...](https://unix.stackexchange.com/questions/125531/how-to-prevent-last-login-message-from-showing-up-when-using-sftp)



    