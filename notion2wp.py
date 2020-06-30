from os import strerror
import os
import sys
import copy
import re	

def heading1(line):
	pattern = '^([# ]+)'
	return '<h1>' + re.split(pattern,line)[-1][:-1] + '</h1>'

def heading2(line):
	pattern = '^([## ]+)'
	return '<h2>' + re.split(pattern,line)[-1][:-1] + '</h2>'
	
def heading3(line):
	pattern = '^([### ]+)'
	return '<h3>' + re.split(pattern,line)[-1][:-1] + '</h3>'

def imgsrc(line):
	pattern = '!\[.*\]'
	return '<img src="https://www.notion.so/image/' + re.findall(pattern,line)[0][2:-1].replace('/','%2F').replace(':','%3A') + '">'
	
def quote(line):
	pattern = '^>'
	return '<blockquote>' + re.split(pattern,line)[-1][:-1] + '</blockquote>'

def code(lines):
	returnCode = '<pre><code class="language-' + lines[0][3:-1] + '">'
	for line in lines[1:]:
		returnCode += line
	returnCode += '</code></pre>\n'
	return returnCode	
	
notion_file = sys.argv[1]
wordpress_file = sys.argv[2]
#md_file = os.path.splitext(notion_file)[0] + '.' + "md"
#html_file = os.path.splitext(wordpress_file)[0] + '.' + "hmtl"
print("Processing file ", notion_file, " to ", wordpress_file)
streamWrite = open(wordpress_file, 'w')
streamRead = open(notion_file, 'r')
line = streamRead.readline()
while line != '':
	if line.startswith('# '):
		line = heading1(line)
	if line.startswith('## '):
		line = heading2(line)
	if line.startswith('### '):
		line = heading3(line)
	if line.startswith('!['):
		line = imgsrc(line)
	if line.startswith('> '):
		line = quote(line)
	if re.search('```', line ):
		list = []
		while not re.search('^```$', line):
			list.append(line)
			line = streamRead.readline()
		line = streamRead.readline()
		line = code(list)
	streamWrite.write(line)
	line = streamRead.readline()
	
	
#streamWrite.write('Java.perform(function() {\n\n')