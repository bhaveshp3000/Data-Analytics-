#!D:\code\dataScienceDemo\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'free-tls-certificates==0.1.6','console_scripts','free_tls_certificate'
__requires__ = 'free-tls-certificates==0.1.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('free-tls-certificates==0.1.6', 'console_scripts', 'free_tls_certificate')()
    )
