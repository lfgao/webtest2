#!/usr/bin/python
activate_this = '/var/www/webtest2/webtest2/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/webtest2/")

from webtest2 import app as application
application.secret_key = 'Addyoursecretkey'

