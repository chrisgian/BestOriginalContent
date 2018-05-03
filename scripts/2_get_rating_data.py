
# coding: utf-8

# Purpose:
# 
# Rate Content from Wiki Data

# In[1]:


import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
import seaborn as sns
import tqdm
import matplotlib.pyplot as plt


# In[2]:


def get_rotten(rotten_loc):
    finder = re.compile('[0-9]{1,3}')
    missing = re.compile('Tomatometer Not Available...')

  # Scrape
    rotten_requested = requests.get(rotten_loc)
    rotten_extract = rotten_requested.text
    rotten_soup = BeautifulSoup(rotten_extract,'html5lib')

    # Check 404
    if rotten_soup.find('h1').get_text().strip() == '404 - Not Found':
        return {'url':rotten_loc, 'critic':'-', 'audience':'-','status':'404'}

    else:
    # Critic
        try:
            crit = rotten_soup.find('div',{'id':'all-critics-numbers'})
            # Check if Missing
            if missing.search(crit.get_text()):
                crit = '-'
            # Extract critic if not missing
            else:
                crit = finder.search(crit.get_text()).group(0)
            # if fail
        except:
            crit = '-'

# Extract Audience
    try: 
        aud = rotten_soup.find('div',{'class':'audience-score meter'})
        aud = finder.search(aud.get_text()).group(0)
    # If Fail
    except:
        aud = '-'                     
    return {'url':rotten_loc, 'critic':crit, 'audience':aud,'status':'success'}
  


# In[ ]:


regex = re.compile('[^a-zA-Z_0-9]')

test_2_clean = []
for i in test_2:
    if len(i) ==4:
        
        content = i[0]
        content = regex.sub('_',content)
        content = content.replace("__","_")
        url = "https://www.rottentomatoes.com/tv/" + content
        test_2_clean += [[content, url, 'netflix']]
    else:
        continue
netflix = pd.DataFrame(test_2_clean, columns = ['Title','URL','Source'])
collected = []

for oc in tqdm.tqdm(netflix.iterrows()):
    time.sleep(np.random.uniform(0,4,1))
    collected += [get_rotten(oc[1]['URL'])]
    

