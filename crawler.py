# Web crawler to recursively extract all the links from a webpage
# Created by Abhijeet Singh. 01-Feb-2018.

def get_page(url): 
	try: 
		import urllib.request
		return urllib.request.urlopen(url).read().decode("utf8")
	except: return

def get_next_target(page):
	start_link = page.find('<a href=')

	# If link sequence is not found
	if start_link == -1:
		return None, 0

	start_quote = page.find('"', start_link)
	start_quote += 1 # Since we don't want to include the quote
	end_quote = page.find('"', start_quote)
	url = page[start_quote : end_quote]
	# [a:b] returns index a to b-1
	return url, end_quote

def get_all_links(page):
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links

get_all_links(get_page('https://udacity.github.io/cs101x/index.html'))
# https://xkcd.com/353/

tocrawl = [] # list of pages left to crawl
crawled = [] # list of pages crawled