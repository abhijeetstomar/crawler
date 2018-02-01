# Web crawler to recursively extract all the links reachable from a seed webpage
# This web crawler follows depth first search for finding links.
# Created by Abhijeet Singh. 01-Feb-2018.
# Testcase: https://xkcd.com/353/
# Example: seed = 'https://udacity.github.io/cs101x/index.html'

seed = input()

# get source text url as return value
def get_page(url): 
	try: 
		import urllib.request
		return urllib.request.urlopen(url).read().decode("utf8")
	except: return

# return link url and get position of next link
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

# return all links in a webpage as list
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

# add disjoint elements of q to p
def union(p,q):
	for i in q:
		if i not in p:
			p.append(i)

# crawl seed page for links recursively
def crawl_web(seed):
	tocrawl = [seed] # list of pages left to crawl
	crawled = [] # list of pages crawled

	while tocrawl:
		page = tocrawl.pop()
		# we only crawl the page if we haven't already
		if page not in crawled:
			union(tocrawl, get_all_links(get_page(page)))
			crawled.append(page)
	
	return crawled

# Main program
print("\nReachable links:")
crawled = crawl_web(seed)
for i in crawled:
	print(i)