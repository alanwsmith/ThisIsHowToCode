#!/usr/bin/env python3

html_header = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video Startup Checklist</title>
<style>
#checklist {
    list-style-type: none;
}
body {
    font-size: 1.2rem;
}
li {
    margin-bottom: 0.3rem;
}

</style>
<script>
function open_timer(event) {
    windowFeatures = "screenX=0,screenY=140,width=240,height=210,menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes";
    window.open('file:///Users/alans/Desktop/ThisIsHowYouProgram/how-to-build-a-javascript-timer/timer.html', 'ClockWindow', windowFeatures);
    event.preventDefault();
}
</script>

</head>
<body>
    <ul id="checklist">
    
'''


html_footer = '''
    <script>
        const launch_link = document.getElementById('time_launcher');
        launch_link.addEventListener('click', function(event) { open_timer(event) });
    </script>
</ul>
</body>
</html>'''



with open('checklist_items.txt', 'r') as checklist_input:
    checklist_items = checklist_input.read().split('\n')

with open('checklist.html', 'w') as checklist_output:
    checklist_output.write(html_header)

    counter = 1

    for checklist_item in checklist_items:
        output_item = f'<li>\n'
        output_item += f'  <input type="checkbox" id="checkbox_{counter}">\n'
        output_item += f'  <label for="checkbox_{counter}">\n'
        output_item += f'    {checklist_item}\n'
        output_item += f'  </label>\n'
        output_item += f'</li>\n'
        checklist_output.write(output_item)
        counter += 1

    checklist_output.write(html_footer)





