---
title: Font Size Checks
draft: true 
updated: 1609372540
---

### Overview

When I first setup for streaming, I ran some tests and decided that the balance of size and readability I liked best was to enlarge fonts a little and crop in to the middle of my monitor. It works great except for the fact that you can't see what I do on the menu bar most of the time. So, I'm testing again at full screen. These videos are what I'm using for the test. 

You can probably skip the first video. It's me checking different magnifications in Safari. I'm just going through the sizes manually and looking at a few web pages to see the differences. 

The second video is more interesting. I'm testing font sizes and color themes in VS Code. And, instead of doing it manually, I write a script to do it for me. It takes me longer to write the script than it would to have just manually tested, but I knew that up front and I'm totally fine with it. While the main goal is getting video samples at the different sizes, these types of little projects make great coding exercises. For example, while writing the script I learned that Pythons `.pop()` can take stuff off the front of a list as well as the back.

### Notes on the Script

This script is designed to help test picking a font size for use in these videos. It loops through a set of VS Code themes and font sizes and updates Code's settings.json file with them. It also writes out a sample file that identifies what the current settings are. 

The script is designed to be used with a copy of the settings.json file. That is, the first step is to do:

    cp settings.json original.settings.json
    
That gives a backup of the settings file and it also acts as a source for every update to settings.json. The reason for that is that we have to remove a `//` comment line at the start of the file. This is done in a brute force way by removing the first line without looking at it that's fine for this basic script but is not an approach you'd generally want to use. 

The problem would show up if you wrote to the settings file and then read out from it again. The first time through would remove the line that's supposed to be removed. Writing back out to the file means it wouldn't be there and reading the next time would remove a line of actual JSON.



- Second video is where you built the script. The test was setup when you had the full screen view of the desktop running at your standard resolution which is set to 1920x1080 on the mac but renders as 3840x2160 through the elgato.

- Third video is when you updated the script so that it could run safely put copying the settings.json file over to an original copy first. This run was done at the cropped in size that you originally setup for twitch. Mac set to 1920x1080 with an actual resolution of 3840x2160. Look at the screenshot aws-obs-video-crop-1.png in this directory for the view on the mac. 

- The fourth video is with the mac set at 1280x720 and the full screen showing in OBS including the menu bar.


---

Next Round To Do:

- Mac at 720 - no crop
- Mac at 1080 - no crop
- Mac at 1080 - crop in 

- Run through font sizes in Sublime text or VS Code
- Run through font sizes in Safari 

- Figure out where Tailwind breaks it's different sizes and use that to set the details for the windows you test on the crop for the mac. 








### Links

- TKTKTK - % operator
- TKTKTK - Video on enumerate (with start=N)
- TKTKTK: pwc
- [Code: The Hidden Language of Computer Hardware and Software - Wikipedia](https://en.wikipedia.org/wiki/Code:_The_Hidden_Language_of_Computer_Hardware_and_Software)
- [5. Data Structures — Python 3.9.1 documentation](https://docs.python.org/3/tutorial/datastructures.html)
- [How to determine a Python variable's type? - Stack Overflow](https://stackoverflow.com/questions/402504/how-to-determine-a-python-variables-type)
- [popleft() method of deque class | Pythontic.com](https://pythontic.com/containers/deque/popleft)
- [python - deque.popleft() and list.pop(0). Is there performance difference? -...](https://stackoverflow.com/questions/32543608/deque-popleft-and-list-pop0-is-there-performance-difference)
- [python - How to read a file line-by-line into a list? - Stack Overflow](https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list)
- [python check data type - Google Search](https://www.google.com/search?client=safari&rls=en&q=python+check+data+type&ie=UTF-8&oe=UTF-8)
- [python join - Google Search](https://www.google.com/search?client=safari&rls=en&q=python+join&ie=UTF-8&oe=UTF-8)
- [python list - Google Search](https://www.google.com/search?client=safari&rls=en&q=python+list&ie=UTF-8&oe=UTF-8)
- [python popleft - Google Search](https://www.google.com/search?client=safari&rls=en&q=python+popleft&ie=UTF-8&oe=UTF-8)
- [python readlines list - Google Search](https://www.google.com/search?client=safari&rls=en&q=python+readlines+list&ie=UTF-8&oe=UTF-8)
- [python slice - Google Search](https://www.google.com/search?client=safari&rls=en&q=python+slice&ie=UTF-8&oe=UTF-8)
- [Python slice()](https://www.programiz.com/python-programming/methods/built-in/slice)
- [Python String join() Method](https://www.w3schools.com/python/ref_string_join.asp)
- [python unshift - Google Search](https://www.google.com/search?client=safari&rls=en&q=python+unshift&ie=UTF-8&oe=UTF-8)
- [Settings - vscode](https://vscode.readthedocs.io/en/latest/getstarted/settings/)
- [Software Developer's Bookmark: python list append, pop, unshift, shift, deque...](http://pl-developer.blogspot.com/2018/01/python-list-append-pop-unshift-shift.html)
- [visual studio code settings file - Google Search](https://www.google.com/search?client=safari&rls=en&q=visual+studio+code+settings+file&ie=UTF-8&oe=UTF-8)
- [Visual Studio Code User and Workspace Settings](https://code.visualstudio.com/docs/getstarted/settings)
- [Why Python's list does not have shift/unshift methods? - Stack Overflow](https://stackoverflow.com/questions/34210969/why-pythons-list-does-not-have-shift-unshift-methods)
- [How do I copy a file in Python? - Stack Overflow](https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python)
- [python copy file - Google Search](https://www.google.com/search?client=safari&rls=en&q=python+copy+file&ie=UTF-8&oe=UTF-8)
- [f string python pre variable - Google Search](https://www.google.com/search?client=safari&rls=en&q=f+string+python++pre+variable&ie=UTF-8&oe=UTF-8)
- [f-strings in Python - GeeksforGeeks](https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/)
- [How to loop with indexes in Python - Trey Hunner](https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/)
- [python - Accessing the index in 'for' loops? - Stack Overflow](https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops)
- [python - Getting rid of \n when using .readlines() - Stack Overflow](https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines)
- [python - How can I use f-string with a variable, not with a string literal? -...](https://stackoverflow.com/questions/54351740/how-can-i-use-f-string-with-a-variable-not-with-a-string-literal)
- [Python 3's f-Strings: An Improved String Formatting Syntax (Guide) – Real Python](https://realpython.com/python-f-strings/)
- [python f string in variable - Google Search](https://www.google.com/search?client=safari&rls=en&q=python+f+string+in+variable&ie=UTF-8&oe=UTF-8)
- [python for index - Google Search](https://www.google.com/search?client=safari&rls=en&q=python+for+index&ie=UTF-8&oe=UTF-8)
- [python readline remove newlines - Google Search](https://www.google.com/search?client=safari&rls=en&q=python+readline+remove+newlines&ie=UTF-8&oe=UTF-8)


