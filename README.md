### school_manager
Using the Django Rest framework, build a simple student management system

**Steps to use school_manager-**  
1. Clone it to your machine-  
    git clone https://github.com/samCyan/school_manager.git  
2. create a virtual environment-  
```
virtual env  
source env/bin/activate  
```
3. Open the project using one of the IDE's or may be shell  
4. Install dependencies from requirements.txt
```
pip install -r requirements.txt
```
5. add <path to the downloaded source code>/image_downloader/src to $PYTHONPATH/sys.path-  
```
import os.path  
import sys  
sys.path.append(<path to the downloaded source code>)  
```
6. do the initial setup by calling following lines of code-  
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username <any username> --email <any email>
```
7. start school_manger-
```
python manage.py runserver
```

List of available end points available at-
```
http://127.0.0.1:8000/docs/
```

**Future book of work-**
write unite test cases
use viewsets instead of plain class based views
configure session and cookie based authentation and authorizations
auto generate api docs using Swagger
dockerize the whole thing
