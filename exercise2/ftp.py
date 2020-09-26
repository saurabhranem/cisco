import urllib

# ---------------------------------------------------
# --------------- downloading -------------------

urllib.urlretrieve('ftp://server/path/to/file', 'file')
# if you need to pass credentials:
#   urllib.urlretrieve('ftp://username:password@server/path/to/file', 'file')

# ---------------------------------------------------
# --------------- copying -------------------

import shutil
from urllib.request import URLopener
opener = URLopener()
url = 'ftp://ftp_domain/path/to/the/file'
store_path = 'path//to//your//local//storage'
with opener.open(url) as remote_file, open(store_path, 'wb') as local_file:
    shutil.copyfileobj(remote_file, local_file)

