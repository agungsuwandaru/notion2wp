# Notice
this is for converting notion page into static html page. the idea is that to create notion as CMS and publish it on wordpress. so, you can have publish on wordpress without worrying about how much storage you use, and creating document is musch more simple becase you can just import from word doc into notion then into wordpress.

# Usage
make notion page public
share and copy notion link
put notion link into param
need to install chromedriver and put it inside PATH
command: python notion2wp.py notion-url output-file

# Features
get notion page html content (full rendered with JS and CSS) using selenium
get image url from notion page
create skeleton html page from potion-api.now.sh API
fill and repair image url from notion page into skeleton page because somehow potion-api.now.sh don't create valid image url if the notion page is imported from .doc
copy table of content from notion page and fill it into skeleton page
link table of content with heading 1, 2, 3
