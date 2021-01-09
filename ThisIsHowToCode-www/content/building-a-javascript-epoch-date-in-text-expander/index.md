---
title: Building A JavaScript Epoch Date In Text Expander
tags:
- JavaScript 
- TextExpander
- LiveCoding
date: 1609264761
---


Overview 
--------

- I want to add dates to my posts, but I don't want the date to be a distraction
- I setup a Text Expander snippet to produce a epoch seconds timestamp
- I got super confused and thrown off by a sample of code 
- After the first take, I did dug in and figured out I was right. Seconds since epoch is always the same.




### Code 

The Text Expander Code we ended up with turned out to be this super straight forward line:

{{< highlight javascript "linenos=table" >}}
Math.round( Date.now() / 1000);
{{< /highlight >}}






### Links


- [Epoch Second Test We Did](epoch-second-test.html)
- TKTKTK Video on Timezones and epoch and UTC 
- TKTKTK Date Format Strings
- [datetime - How can I get seconds since epoch in Javascript? - Stack Overflow](https://stackoverflow.com/questions/9456138/how-can-i-get-seconds-since-epoch-in-javascript)
- [Epoch Converter - Unix Timestamp Converter](https://www.epochconverter.com/)
- [epoch date - Google Search](https://www.google.com/search?client=safari&rls=en&q=epoch+date&ie=UTF-8&oe=UTF-8)
- [Get Number of Seconds Since Epoch in JavaScript](https://futurestud.io/tutorials/get-number-of-seconds-since-epoch-in-javascript)
- [javascript epoch seconds - Google Search](https://www.google.com/search?client=safari&rls=en&q=javascript+epoch+seconds&ie=UTF-8&oe=UTF-8)
- [Current Millis ‐ Milliseconds since Unix Epoch](https://currentmillis.com/)
- [Date.now() - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/now)
- [Date.prototype.getTime() - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTime)
- [Epoch Converter - Unix Timestamp Converter](https://www.epochconverter.com/)
- [epoch date - Google Search](https://www.google.com/search?client=safari&rls=en&q=epoch+date&ie=UTF-8&oe=UTF-8)
- [Get Number of Seconds Since Epoch in JavaScript](https://futurestud.io/tutorials/get-number-of-seconds-since-epoch-in-javascript)
- [How can I get a formatted date for a UNIX timestamp from the command line -...](https://unix.stackexchange.com/questions/940/how-can-i-get-a-formatted-date-for-a-unix-timestamp-from-the-command-line)
- [How to get seconds since epoch in JavaScript? - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-get-seconds-since-epoch-in-javascript/)
- [javascrtit date gettime - Google Search](https://www.google.com/search?client=safari&rls=en&q=javascrtit+date+gettime&ie=UTF-8&oe=UTF-8)
- [mac print epoch time - Google Search](https://www.google.com/search?client=safari&rls=en&q=mac+print+epoch+time&ie=UTF-8&oe=UTF-8)
- [macos - Time in milliseconds since epoch in the terminal - Ask Different](https://apple.stackexchange.com/questions/135742/time-in-milliseconds-since-epoch-in-the-terminal)
- [National Institute of Standards and Technology | NIST](https://www.time.gov/)
- [seconds since epoch - Google Search](https://www.google.com/search?client=safari&rls=en&q=seconds+since+epoch&ie=UTF-8&oe=UTF-8)
- [Seconds since the Epoch (GNU Coreutils)](https://www.gnu.org/software/coreutils/manual/html_node/Seconds-since-the-Epoch.html)
- [The Problem with Time & Timezones - Computerphile - YouTube](https://www.youtube.com/watch?v=-5wpm-gesOY&list=LLhgxsceCCl4iX1smQPLn6Dw&index=3092)
- [time zones computers trouble - Google Search](https://www.google.com/search?newwindow=1&client=safari&rls=en&ei=MWnrX4jtLavy5gKZrquYDQ&q=time+zones+computers+trouble&oq=time+zones+computers+trouble)
- [Unix time - Wikipedia](https://en.wikipedia.org/wiki/Unix_time)



