---
title: Making Animated GIFs with Adobe Premiere and ffmpeg (Part 2)
date: 1611630271
tags:
- PowerShell
- ffmpeg
- Automation
- Scripting
---

Picking up where we left off. 

Got a PowerShell script setup that watches a specific folder and runs an ffmpeg command to process any gif files and place them in a new directory before deleting the original. 

This was my first time using PowerShell to script something. It's very different from what I'm used to, but I can see the appeal. Definitely going to take some getting used to. 

TKTKTK: Make a How-To out of this one

### Links

- https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item?view=powershell-7.1
- https://docs.microsoft.com/en-us/dotnet/api/system.io.filesystemeventargs?view=net-5.0
- https://docs.microsoft.com/en-us/dotnet/api/system.management.automation.pseventargs.sourceeventargs?view=powershellsdk-7.0.0
- https://stackoverflow.com/questions/38797889/event-sourceeventargs-attribute-is-returning-a-null-or-empty-object 
- https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/add-content?view=powershell-7.1
- https://stackoverflow.com/questions/30011267/windows-equivalent-of-touch-i-e-the-node-js-way-to-create-an-index-html
- https://stackoverflow.com/questions/29066742/watch-file-for-changes-and-run-command-with-powershell
- https://mcpmag.com/articles/2019/05/01/monitor-windows-folder-for-new-files.aspx
- https://docs.microsoft.com/en-us/dotnet/api/system.io.filesystemwatcher.created?view=net-5.0
- https://docs.microsoft.com/en-us/dotnet/api/system.io.filesystemwatcher?redirectedfrom=MSDN&view=net-5.0
- https://dereknewton.com/2011/05/monitoring-file-system-changes-with-powershell/
- https://social.technet.microsoft.com/Forums/scriptcenter/en-US/c75c7bbd-4e32-428a-b3dc-815d5c42fd36/powershell-check-folder-for-new-files
- https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/register-objectevent?view=powershell-7.1
- https://superuser.com/questions/226828/how-to-monitor-a-folder-and-trigger-a-command-line-action-when-a-file-is-created
- https://www.cloudsavvyit.com/2000/how-to-monitor-a-windows-folder-for-new-files-and-take-action/

