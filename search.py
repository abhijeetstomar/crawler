# Created by Abhijeet Singh
import crawler
import web_index

# crawl seed page for links recursively
def build_web_index(seed, maxPages, maxDepth):
	tocrawl = [seed] # list of pages left to crawl
	crawled = [] # list of pages crawled
	nextDepth = [] # to keep track of depth
	depth = 0 # initial depth
    index = [] # our web index

	# we crawl till there's nothing left to crawl or till we've reached a specified depth
	while tocrawl and depth <= crawler.maxDepth:
		page = tocrawl.pop()
		# we only crawl the page if we haven't already and if we haven't reached the limit specified
		if page not in crawled and len(crawled) < crawler.maxPages:
            content = crawler.get_page(page)

            web_index.add_page_to_index(index, page, content)

			crawler.union(nextDepth, crawler.get_all_links(content))
			crawled.append(page)
		# once tocrawl is empty, we transfer the elements of nextDepth to tocrawl and empty nextDepth for next iteration
		if not tocrawl:
			tocrawl, nextDepth = nextDepth, []
			depth += 1
			print("Processing depth", depth)
	
	return crawled

# Main program
if __name__ == "__main__":
	seed = input("Input url: ")
	print("\nReachable links:")
	crawled = build_web_index(seed, crawler.maxPages, crawler.maxDepth)
	for i in crawled:
		print(i)