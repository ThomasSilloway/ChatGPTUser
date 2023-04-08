@echo off
echo Launching chrome
start chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\GithubRepos\LLMUser\ChromeProfile"
