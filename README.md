# Notice
this is for converting notion page into static html page. the idea is that to create notion as CMS and publish it on wordpress. so, you can have publish on wordpress without worrying about how much storage you use, and creating document is musch more simple becase you can just import from word doc into notion then into wordpress.<br/>

# Usage
make notion page public<br/>
share and copy notion link<br/>
put notion link into param<br/>
need to install chromedriver and put it inside PATH<br/>
command: python notion2wp.py notion-url output-file<br/>

# Features
get notion page html content (full rendered with JS and CSS) using selenium<br/>
get image url from notion page<br/>
create skeleton html page from potion-api.now.sh API<br/>
fill and repair image url from notion page into skeleton page because somehow potion-api.now.sh don't create valid image url if the notion page is imported from .doc<br/>
copy table of content from notion page and fill it into skeleton page<br/>
link table of content with heading 1, 2, 3<br/>
