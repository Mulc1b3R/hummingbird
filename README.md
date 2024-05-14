# hummingbird

A comprehensive data exfiltration suite consisting of 23 python scripts . Extracts all possible file types.

Internal and external links , css , javascript , metadata , whois lookup , ssl cert , ip address , mp3's , mp4's , xml , swf ,

blog posts and articles , all image types, favicons , reddit and wikipedia mentions, web manifest , rss feeds , e.c.t.

Hummingbird provides a surgical method for precise data extraction of a 'Target Url'. Allowning for a full or selective extraction proccess.

# method

Requires python3 installed locally . Clone the repo , fork it or download the .zip , depending on preference.

Main = hummingbird.py : 

Choose a 'target url' and enter it into you .env file + save. (TARGET_URL=https://psicodata.io).

In root dir (your folder name) . type ; pip install -r requirements.txt

This will load all the dependeccies .

1). Then type ; python hummingbird.py  - this will create an 'output' folder , clone index.html of Target URL ,create iframe.html , open default browser = target.url //identified...

giving you eyes on your target url.

2). type ; python text.py - this will read the main text of the index.html output as 'text.txt' - run prior to mp3-create.py or mp3-create.py will have nothing to convert to audio.

3). type ; python mp3-create.py - this will generate an 'audio' folder in the output folder and create an mp3 consisting of the text content of index.html , so you can listen to the website

while you work.

4). type ; python css-extractor.py this will  create a  'styles' folder in 'output' folder grab all css file related 2 Target.url and store them in the folder.

5). type ; python js-extractor.py this will create a 'js_files' folder in 'output' folder + grab all .js files / both external and internal.

6). type ; python int-links.py   this produces an exhaustive list of internal links as 'int-links.html' to output folder providing information regarding the internal structure of the target url.

7). type ; python ex-links.py   this int-links.py produces an exhaustive list of internal links as ex-links.html to output. The links are 'clickable' enabling a view of all links to 'outside'.

8). type ; python favicon.py   favicon.py creates an 'img' folder includes favicon if present within the folder.

9). type ; python articles.py  creates img folder and grabs present images related to 'articles , may not produce a result if the url is not a blog. if BLOG , creates psudoRSS in html form.

(results produced in a grid format). hypertext linked.

10). type ; python posts.py   similar to above , but may enable deeper penetration.

    




