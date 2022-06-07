# SoftDesk API
***********************************************************************************************************************
###### SoftDesk provides an API allowing to manage issue tracking.<br/>This solution is aimed at B2B customers. 

## Configure the application

### Clone repository
1) In your terminal, move to the folder of your choice:<br/>```cd path_of_your_choice```
2) Clone the repository into this folder:<br/> 
```git clone git@github.com:karnex/SoftDesk.git```

### Windows system configuration

5) Create a virtual environment:<br/> 
```python -m venv env```
6) Enable the virtual environment:<br/> 
```env\Scripts\activate```
7) Install all useful dependencies for the project:<br/>
```pip install -r requirements.txt```

### Unix system configuration

5) Create a virtual environment:<br/> 
```python3 -m venv env```
6) Enable the virtual environment:<br/> 
```source env/bin/activate```
7) Install all useful dependencies for the project:<br/> 
```pip3 install -r requirements.txt```

## Run and use application

**1) Run the application**

- From a Windows device:<br/> 
```python manage.py runserver```
- From a Unix device:<br/> 
```python3 manage.py runserver```

**2) Use it**

- You can now send HTTP requests to it<br/>
[Postman documentation](https://documenter.getpostman.com/view/20832173/UyxnEQrg)

Have fun ! 😏

------------------------------------------------------------
### Using Flake8

##### Install Flake8 and its html report generation plugin

- From a Windows device:<br/>
```pip install flake8 flake8_html```

- From a Unix device:<br/>
```pip3 install flake8 flake8_html```

#### Configuration file

The configuration of flake8 is managed here through the setup.cfg file which is located at the root of the project.

#### Generate a flake8-html report

```flake8 --format=html --htmldir=flake8_rapport```

