import os

while True:
    try:
        import numpy as np
        import flask
        import pandas as pd
        import pymysql as SQL
        break
    except:
        module_list = "numpy flask pandas pymysql".split()
        for i in module_list:
            os.system("pip install {}".format(i))