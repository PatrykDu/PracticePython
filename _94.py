file = open('urls.txt', 'r')
links = [link for link in file]
new_links = ['http:/' + link[6:] for link in links]
with open('urls2.txt', 'w') as file2:
    for link in new_links:
        file2.write(link)
