#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys      
import logging  
logging.basicConfig(stream=sys.stderr)  
sys.path.insert(0,"/var/www/digisol.agency/digisol.agency")     
from digisol import app as application  
application.secret_key = 'kQXNNq+bIj2v>H|~,=!Y2Sd&=QbbG0'
