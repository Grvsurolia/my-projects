import os

os.system("find ./apps/ -type d -name 'migrations'  -exec rm -rf {} +")
os.system("find ./apps/ -type d -name '__pycache__'  -exec rm -rf {} +")