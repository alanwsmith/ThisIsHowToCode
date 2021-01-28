$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = "D:\gif_automation_test\test-v2\source"
$watcher.Filter = "*.gif"

$action = { 
    $SourcePath = $Event.SourceEventArgs.FullPath
    $FileName = $Event.SourceEventArgs.Name
    $DestinationPath = "D:\gif_automation_test\test-v2\destination\$FileName"
    Add-Content -Path "D:\gif_automation_test\test-v2\log.txt" -Value "---"
    Add-Content -Path "D:\gif_automation_test\test-v2\log.txt" -Value "SourcePath: $SourcePath"
    Add-Content -Path "D:\gif_automation_test\test-v2\log.txt" -Value "DestinationPath: $DestinationPath"
    ffmpeg.exe -ss 0 -i "$SourcePath" -vf "fps=14,scale=480:-2:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 -y "$DestinationPath"
    Remove-Item -Path $SourcePath 
} 

Register-ObjectEvent $watcher "Changed" -Action $action

while ($true) {
    sleep 1
}