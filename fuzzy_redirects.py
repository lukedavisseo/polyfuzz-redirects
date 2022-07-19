import advertools as adv
import pandas as pd
from polyfuzz import PolyFuzz

# This turns any sitemap into a Pandas DataFrame
sitemap_df = adv.sitemap_to_df('https://example.org/sitemap.xml')

# This extracts all the URLs and puts them into a list
url_list = sitemap_df['loc'].to_list()

# Here, you add all the broken URLs
broken_list = []

# You can specify a specific model but for a basic fuzzy match, you can use this
model = PolyFuzz().match(broken_list, url_list)

# This converts the matches into another DataFrame
df = model.get_matches()

# And this exports it to a CSV
df.to_csv('filename.csv', index=False)
