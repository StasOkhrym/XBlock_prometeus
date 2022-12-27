# Simple Collapsible XBlock with counter

Prometeus test task

### How to Start

1. Clone repository
```
https://github.com/StasOkhrym/XBlock_prometeus.git
```
2. Create and activate a virtual environment:  
```
python3 -m venv venv
source venv/bin/activate (Linux and macOS) or 
venv\Scripts\activate (Windows)
```

3. Download XBlock-SDK, change directory to sdk directory and install requirements:
```
git clone https://github.com/openedx/xblock-sdk.git

cd xblock-sdk
pip install -r requirements/base.txt
```
4. Apply migrations and install simplexblock
```
python manage.py migrate
cd ..
pip install -e simplexblock
```
5. Run local server 
```
python xblock-sdk/manage.py runserver
```