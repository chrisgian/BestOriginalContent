
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re


# In[ ]:



def get_wiki(wiki_loc):
    
    wiki_requested = requests.get(wiki_loc)
    wiki_extract = wiki_requested.text
    wiki_extract = wiki_extract.replace("/wiki/","")

    wiki_soup = BeautifulSoup(wiki_extract,'html5lib')
    wiki_tables = wiki_soup.find_all('table',{'class':'wikitable sortable'})

    wiki_row_collected = []
    for table in wiki_tables:
        wiki_rows = table.find_all('tr')

    for row in wiki_rows:
        row = row.find_all('a')
        row = [re.sub(r"_\(.+?\)","", i.get('href').lower()) for i in row if '#' not in i.get('href')]
        wiki_row_collected += [row]

    return wiki_row_collected


# In[ ]:


test_1 = get_wiki(wiki_loc='https://en.wikipedia.org/wiki/List_of_original_programs_distributed_by_Hulu')
test_2 = get_wiki(wiki_loc='https://en.wikipedia.org/wiki/List_of_original_programs_distributed_by_Netflix')
test_3 = get_wiki(wiki_loc='https://en.wikipedia.org/wiki/List_of_programs_broadcast_by_HBO')
test_4 = get_wiki(wiki_loc = 'https://en.wikipedia.org/wiki/List_of_original_programs_distributed_by_Amazon')

