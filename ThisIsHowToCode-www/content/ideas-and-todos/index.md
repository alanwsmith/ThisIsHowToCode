---
title: "Ideas and TODOs"
---


- Examples:

    - Cash register: 

        Making change with things like N number of quarters, dimes, and nickels. 






- Make the Git repo


- Use this license: https://creativecommons.org/licenses/by-nc-sa/4.0/


- Do code reading where you look at other folks code in github and analyse it to see what's up with it. 


- Setup a newsletter

- Figure out what all this mean:

        function sleep(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }

- Figure out how `async` functions work in JavaScript

- Make video on scoping

- video on const/let/var in JS

- GitHub Desktop video

- Video of Tools to Install 

- Look at npx create-react-app APP_NAME

- Video on directory structure an root of file system

- Add some kind of dashboard that shows you which OBS scene you're on so you have the best one showing. 

- Learn about javascript promises

- do a video on arrow functions

- Less than and less than equal to (and more than and more than equal)

- figure out let/const/whatever...

- Number types - integers vs floats, etc...

- DOMContentLoaded ~ https://javascript.info/onload-ondomcontentloaded

- Command Line Intro

- Setup ll alias for ls -ll

Ideas/TODOs

- Put in a launch page for TODOs. 
- Make sure to make lots of different version of things so you can do things again and again to get conecpts down. 
- Make sure to define parts of things (e.g. constructors in react)
- Another plus of VS Code is that it does syntax highlighting and autocompletion (explain what both those things are)
- drop in full code samples at different places. Use git for that. 
- Don't put things on one line like:

        return <Square value={this.state.squares[i]} />

    If they are going to end up like this:

        return ( 
            <Square 
                value={this.state.squares[i]} 
                onClick={() => this.handleClick(i)}
            />
        )

    The addition of the second line is hard to process if you break it out like that 
    without starting like that in the beginning. And, if you're going to have things
    like the parens, put them in from the start. Don't add them later. 


- Setup so the syntax highligting is the same as VSCode default but let folks also choose the highlight they want so the code on the pages mathces the code in their editors. 

- Setup row highlighting to identify which rows changed. (make sure it's color blind accessible)

- Things to do:

    - Mutability v Immutablity 

- TODO:

    Look up this syntax:

        var player = {score: 1, name: 'Jeff'};

        var newPlayer = Object.assign({}, player, {score: 2});

- See the react tutorial section on immutability and time travel for an example of undos. 

- Setup Online Code Playgrounds

- Create video on ports and server.

- Look at https://schema.org and the way that the axiom theme uses its stuff. 

- Store AWS credentials in Mac's Keychain Access

- Store AWS credentials in Windows password storage

- Figure out how to get the link and javascript to work in `timer-for-vidoes` so you can actually launch the timer

- See if you can get Hugo to sort files off file date instead of a YAML date. That way you don't have to show dates in the videos.

- Turn off last login date time stamp on the mac

- Flip timestamp on iTerm over to use seconds since epoch? Or maybe just turn it off?

- Built a tool that checks the preferences of everything it can so you know if you need to make adjustments for streaming. (e.g. font sizes on Sublime Text)

- Build a new tool that setup up your environment for recording and then for when you're not recording. 

- Do Minecraft stuff to show boolean logic

- Find other things like Minecraft to show boolean logic

- Create a script the pulls wether info at a regular interval
    and writes it to a text file that you can pick up with
    a `cat` command at the start of your `.zshrc` file so it
    shows up each time you fire up a new window.

    Could do the same thing with system stats or something else
    just to mess around with it and the prompt

    Maybe pull a different random quote from a text file for
    the MOTD type functionality. 

    Remember that you have `~/.hushlogin` in place which prevents
    both the Last Login message as well as the MOTD message
    from showing up. That's why you need to do it in the 
    .zshrc file.

- Setup: DNSSEC - https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec.html

- Setup a privacy policy 

- Setup an email newsletter

- Capture code to look at in Pinboard under `CodeToLookAt` and use it to read on stream to figure out what's up. 

- Figure out how to use this: https://rust.godbolt.org

- Setup to automatically blur text for the account name 

- Show place holders as variables. 

- Setup a way to basically hyperlink in videos where it will stack vidoes for you pausing one and putting in the other one in some kind of tab. when it's done, you can go back to the first. Same with the idea of bookmarks in the videos with a tap. Also have the content change underneath based off what's in the video. 

- Setup so when you pause a video it brings up links to relevant supporting elements. quick hits for terms, and things. You could also add bookmarks and notes for the specific point. Have a bookmarks and notes page that shows all your stuff. 

- Video on RAID. 

- Look at OpenCourseWare - https://cs50.readthedocs.io/video/ - 

- They let you toggle between the instructor and the video. Maybe look at that, but my thinking is it's better to have fully produced videos with optionals than making them pick where they want to go. 


- Write an app that's a hotkey launcher just for apps. Like, that's its sole purpose. Select an App, select a hotkey and you're done. (Would have to check for conflicts too, but could (hopefully) let you know where the conflict is)

- Build responsive Vimeo embed (if it's not already, which it probably is)

- Update ImportPhotos so that it just reads the first N number of bytes and hashes those to do the file comparison check. 

- Setup links for music tracks you can put behind stuff to play with it as a setting. 

- Look at: https://www.freepianomethod.com

- Do things like Fantasy Football 
