import webbrowser

search_terms = input('Enter your Google query: ')
url = 'https://www.google.com/search?q={}'.format(search_terms)
# webbrowser.open_new_tab(url)
webbrowser.open(url)
