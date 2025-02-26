import os

# Basisconfiguratie voor pgAdmin
DATA_DIR = os.path.expanduser("~/.pgadmin/")

# Webserver configuratie
SERVER_MODE = False
DEFAULT_SERVER = '127.0.0.1'
DEFAULT_SERVER_PORT = 5050

# Wachtwoordbeveiliging
MASTER_PASSWORD_REQUIRED = False
