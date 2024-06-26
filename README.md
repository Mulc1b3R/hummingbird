# hummingbird

A comprehensive data exfiltration suite consisting of 23 python scripts . Extracts all possible file types.

Internal and external links , css , javascript , metadata , whois lookup , ssl cert , ip address , mp3's , mp4's , xml , swf ,

blog posts and articles , all image types, favicons , reddit and wikipedia mentions, web manifest , rss feeds , e.c.t.

Hummingbird provides a surgical method for precise data extraction of a 'Target Url'. Allowning for a full or selective extraction proccess.

![hb](hummingbird.gif)

# method

Requires python3 installed locally . Clone the repo , fork it or download the .zip , depending on preference.

Main = hummingbird.py : 

Choose a 'target url' and enter it into your example.env file, rename file '.env' , (delete the word 'example') + save as .env (txt).     e.g (TARGET_URL=https://psicodata.io).

(.env files are invisible on some operating systems due to the fact that they contain sensitive data such as api keys ).

Hummingbird should be os and browser 'agnostic' , this is for windows but all you need change is the syntax of yr commands if you are running on something else.

create a folder called 'archive'. 

In root dir (your folder name) . type ; pip install -r requirements.txt

This will load all the dependencies.

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

10). type ; python posts.py   similar to above , but may enable deeper penetration and will grab anything that it's sister code missed.

11). posts2mp3.py requires output from 'posts.py'    zero output= zero mp3.

12). patchwork.py      creates 'patchwork.html'    containing a patchwork of grabbed images ,hypertext linked if applicable.

13). media.py creates media_files folder and puts mp3's and mp4's inside if present. (may need to examine 'int-links.py' and re target for deeper penetration.

this is really good for audio books and videos.

14). exotic.py   grabs all  pdf, xml, zip, doc ,xls , docx , htm ,xlsx  files ; no result if nothing present.

15). search.py   creates a "SEARCH ENGINES LIST " using 'template2.html' , puts it in 'output' folder as 'engines.html' ,then 'hummingbird 

creates an iframe giving you a selection of search engines to choose from...

16). swf.py for use when grabbing old school flash games , it will download everyfile present to ; output/downloaded_swf_files .download as many flash games as you like , use ruffle browser extension

CLICK HERE to download your swf arcade player:  https://psicodata.io/CDN/swf-arcade.zip and get your own swf game arcade.

17).txt2html converts txt 2 html.

18) wiki.py creates an 'organisation info txt '.consisting of mentions on 'reddit and wikipedia' returns null if null.

19).  xtra.py get you any web manifest , rss feeds , and fonts.

20). whois.py serves the same purpose as running an whois search on the web , returnd DNS info regarding DOMAIN NAME of target url.

21). After running the whois , change target url in .env file to DOMAIN NAME (strip it of the https://www so that TARGET_URL=example.com ) the exact domain name will be in whois file you just created.

22). ssl-ip.py returns data regarding the ssl certificate and ip address. (having changed to domain name first).

23). record.py will .zip everything you just grabbed and move it from the output folder to the 'archive folder ,ready for your next operation. 

24). you can cancell any script from running , if you hit a heavy 'payload' using 'ctrl + c' . 

To target a differnt url just change the url in the .env

To Eradicate any messy files in the archive use 'xxx.py'  this will destroy everything exept python and .zip files. in the location.

If you haven't got it by now , thats because it doesn't exist.......................

                                                                                      

```In Memory of George Mellor , William Thorpe & Thomas Smith , Executed by hanging 9.00 a.m. on Friday 8th January 1813, York Castle , instigators of the 'LUDDITE' Uprising.```


                                                                                                                                              MADE IN YORKSHIRE
    




