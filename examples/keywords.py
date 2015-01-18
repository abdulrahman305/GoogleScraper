"""
GoogleScraper will scrape the jobs according to the dictionaries below.

Passing the scrape_jobs to GoogleScraper is simple:

GoogleScraper --keyword-file keywords.py

"""

scrape_jobs = [
    {
        'query': 'hello world',
        'search_engine': 'google', # on which search engines this keyword should be searched.
        'proxy': 'socks5 localhost 9050', # which proxy to use for this keyword
        'num_pages': 10, # how many pages to scrape this keyword
        'scrapemethod': 'http'
    },

    {
        'query': 'blubb',
        'search_engine': 'yandex',
        'another option': 'some fancy value', # you can specify other (even senseless) options
        'scrapemethod': 'selenium'
    },

    {
        'query': 'mountina',
        'search_engine': 'baidu',
        'scrapemethod': 'http'
    },

    # ...
]