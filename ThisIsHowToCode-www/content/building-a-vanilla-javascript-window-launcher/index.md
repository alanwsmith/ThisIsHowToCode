---
title: Building A Vanilla JavaScript Window Launcher
---

In this one I build a little vanilla javascript function to launch my timer window from a link. I can control the size and position of the window to fit just my timer and put it where I want on the screen.

I start off with a button and then move to an `<a>` anchor tag. While doing the anchor tag I discovered I couldn't pass parameters to a function called by `addEventListener`. My solution was to add an inline function that called the external function with the parameter. Once I got that in place, everything worked like a champ.

All this work is done in plain-old "vanilla" javascript. No frameworks involved. I've got nothing against frameworks, but there are times like this when they'd be overkill. If I'd already had a framework in place that included the window launching ability, I would have used it. Since I didn't, I just stuck with the basics. 

### Links

- [Google Search: addeventlistener](https://www.google.com/search?client=safari&rls=en&q=addeventlistener&ie=UTF-8&oe=UTF-8)
- [Google Search: javascript event listener](https://www.google.com/search?client=safari&rls=en&q=javascript+event+listener&ie=UTF-8&oe=UTF-8)
- [Google Search: javascrtip laucnh windows](https://www.google.com/search?client=safari&rls=en&q=javascrtip+laucnh+windows&ie=UTF-8&oe=UTF-8)
- [Google Search: pass data to event listener function](https://www.google.com/search?client=safari&rls=en&q=pass+data+to+event+listener+function&ie=UTF-8&oe=UTF-8)
- [Google Search: prevent default](https://www.google.com/search?client=safari&rls=en&q=prevent+default&ie=UTF-8&oe=UTF-8)
- [MDN: Event.preventDefault() - Web APIs](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault)
- [MDN: EventTarget.addEventListener() - Web APIs](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
- [MDN: Window.open() - Web APIs](https://developer.mozilla.org/en-US/docs/Web/API/Window/open)
- [MDN: Window.open() - Web APIs](https://developer.mozilla.org/en-US/docs/Web/API/Window/open#Popup_condition)
- [Stack Overflow: How to pass arguments to addEventListener listener function?](https://stackoverflow.com/questions/256754/how-to-pass-arguments-to-addeventlistener-listener-function)
- [Vanilla JS](http://vanilla-js.com/)
