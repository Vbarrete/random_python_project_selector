# -*- coding: utf-8 -*-
#!/usr/bin/env python

import random
import urllib.request
import re
import webbrowser

r = random.randint(1, 100)
url = "https://github.com/search?l=&p="+ str(r) +"&q=language%3APython&ref=advsearch&type=Repositories&utf8=%E2%9C%93"
response = urllib.request.urlopen(url)
page_source = response.read()
r_url = re.compile('<a href="([^"]*)" class="v-align-middle">')
project = re.findall(r_url, str(page_source))
project_url = "https://github.com" + random.choice(project)
webbrowser.open(project_url)
