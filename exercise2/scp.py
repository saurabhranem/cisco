import subprocess
import os
my_file = "<path>" # or "foo.bar"
destination = "<destination path>"
p = subprocess.Popen(["scp", my_file, destination])
sts = os.waitpid(p.pid, 0) 
# -- process id and exit status
# ------------------------------
# ------------------------------

import subprocess
subprocess.run(["scp", my_file, "USER@SERVER:destination-path"])
#e.g. subprocess.run(["scp", "foo.bar", "joe@srvr.net:/path/to/foo.bar"])


## -------------------------------
