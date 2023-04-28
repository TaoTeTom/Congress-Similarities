#File for installing packages to virtual env
!pip install --user virtualenv
from cdg_client import CDGClient  # make it available

api_key = 'EGIsSFuWCOu3Vd50Ci5xsNssppc85hokcHefdxph'

client = CDGClient(api_key)  # pass the key, response_format="xml" if needed

# use requests args and kwargs below modify the request:
print(client)