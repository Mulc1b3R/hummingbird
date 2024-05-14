# hummingbird

A comprehensive data exfiltration suite consisting of 23 python scripts . Extracts all possible file types.

Internal and external links , css , javascript , metadata , whois lookup , ssl cert , ip address , mp3's , mp4's , xml , swf ,

blog posts and articles , all image types, favicons , reddit and wikipedia mentions, web manifest , rss feeds , e.c.t.

# method

Requires python3 installed locally . Clone the repo , fork it or download the .zip , depending on preference.

Main = hummingbird.py : 

Choose a 'target url' and enter it into you .env file + save. (TARGET_URL=https://www.example.com).

In root dir (your folder name) . type ; pip install -r requirements.txt

This will load all the dependeccies .

1). Then type ; python hummingbird.py  - this will create an 'output' folder , clone index.html of Target URL ,create iframe.html , open default browser = target.url //identified...

giving you eyes on your target url.

2). type ; python text.py - this will read the main text of the index.html output as 'text.txt' - run prior to mp3-create.py or mp3-create.py will have nothing to convert to audio.

3). type ; python mp3-create.py - this will generate an 'audio' folder in the output folder and create an mp3 consisting of the text content of index.html , so you can listen to the website

    while you work. 

    




