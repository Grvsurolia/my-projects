import os

os.system("find ./product -type d -name 'migrations'  -exec rm -rf {} +")
os.system("find ./users -type d -name 'migrations'  -exec rm -rf {} +")
os.system("find ./product -type d -name '__pycache__'  -exec rm -rf {} +")
os.system("find ./users -type d -name '__pycache__'  -exec rm -rf {} +")