# GitHubSearch
A code to automate search for a substring in public repositories:

Requires - `selenium 3.141.0`

`python3.7 -m pip install selenium`

WebDriver - I have used ChromeDriver which can be downloaded from

`https://chromedriver.chromium.org/downloads`

How to use:

Add URL's of public repositories within which you want to search for a particular substring

`python searchGit.py -if input.txt -of output.txt -d /home/arvindabraham/chromedriver -s "hello"`

If you want to search for multiple substrings - add them within double quotes.

`python searchGit.py -if input.txt -of output.txt -d /home/arvindabraham/chromedriver -s "hi hello"` 

Note: In case of multiple substrings the files containing all mentioned substrings will only be populated in the output file.