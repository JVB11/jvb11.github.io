#!/usr/bin/env python3

import calendar
import requests
import json
import re
from datetime import datetime
from urllib.parse import urlencode
from os import environ

# variables used during update
my_orcid = environ['ORCID']
my_token = environ['ADS_API']
adsabs_url_base = "https://api.adsabs.harvard.edu/v1"
ads_library_url = environ['ADS_LIB']
markdown_path = "_pages/publications.md"

# Regular expression for arXiv formatting
arxiv_regex = re.compile(r"(https\:\/\/arxiv\.org\/abs\/)arXiv\:(\d+\.\d+)")
date_regex = re.compile(r", ([0,1]\d)\/(20\d{2}),")

# first get list of bibcodes of 5 latest papers associated with my orcid
last_5_papers_query = urlencode({"q": f"orcid:{my_orcid} property:article", "fl": "bibcode", "sort": "date desc", "rows": 5})
last_5_papers_response = requests.get(
    f"{adsabs_url_base}/search/query?{last_5_papers_query}",
    headers={"Authorization": f"Bearer {my_token}"}
)
list_last_5_papers_bibcodes = [b['bibcode'] for b in last_5_papers_response.json()["response"]["docs"]]

# now retrieve the necessary bibliographic information and generate the export string
spacer = '&nbsp;' * 16
bottom_line_formatting = fr'{spacer}*DOI: <a href="https://doi.org/%d">%d</a>, NASA ADS: %U, arXiv: https://arxiv.org/abs/%X*\n'
payload = {
    "bibcode": list_last_5_papers_bibcodes,
    "sort": "date desc",
    "format": fr'%ZEncoding:markdown + %8.3g, %T, %D, %q, %V, %p (Nr. of citations: %c)\n\n{bottom_line_formatting}'
}
bibliography_response = requests.post(f"{adsabs_url_base}/export/custom", headers={'Authorization': f"Bearer {my_token}"}, data=json.dumps(payload))
export_string: str = bibliography_response.json()['export']
formatted_export_string = date_regex.sub(
    lambda x: fr", {calendar.month_name[int(x.group(1))]} {x.group(2)},", 
    arxiv_regex.sub(r'<a href="\1\2">\2</a>', export_string.replace("Van Beeck J.", "**Van Beeck J.**"), count=5), 
    count=5
)

# retrieve and format the date of adjustment
my_date_stamp = datetime.now().strftime('%d %B %Y')

# load the markdown file
with open(markdown_path, "r") as f:
    my_markdown = f.readlines()
# change the content
## find location of headers that indicate which part of the markdown file to edit
i1 = my_markdown.index("## Check out my five most recent publications\n")
i2 = my_markdown.index(f"## Check out my key works (view the full publication list in my [ADS library]({ads_library_url}))\n")
## create a list of the export string
my_split = [f"{x}\n" for x in formatted_export_string.split("\n")]
## now generate the new markdown file content
md_content = my_markdown[:i1+1] + ["\n"] + my_split + [f"(Last update: {my_date_stamp})\n", "\n"] + my_markdown[i2:]
# write/edit the markdown file
with open(markdown_path, "w") as f:
    f.writelines(md_content)
