# 75 Years of Toyota Parser
Python PDF parser for 75 years of Toyota website.

### Dependencies
You need to install these on your system first:

* [Python](https://www.python.org/downloads/)

These are the libraries from pip that the project requires:

* [requests](https://pypi.org/project/requests/)
* [bs4](https://pypi.org/project/beautifulsoup4/)
* [Pillow](https://pypi.org/project/Pillow/)

Also, requirements.txt file can be used to install necessary dependencies: \
``` pip insall -p ./requirements ``` .

### Usage
1. Install Python 3 in your system if it's not installed
2. Download Parser \
2.1 Using git \
``` git clone https://github.com/Umphi/Toyota75Parser ``` \
2.2 As zip from GitHub \
[Download](https://github.com/Umphi/Toyota75Parser/archive/refs/heads/master.zip) and extract archive into separate folder
3. Change directory to Toyota75Parser: \
Example after download using git clone
``` cd ./Toyota75Parser ```
4. Install dependencies: \
``` pip install -p ./requirements ```
5. Create settings.ini file with own configuration: \
``` cp ./settings.ini.example ./settings.ini ``` \
Car id can be found on right side of header of selected car page on [75 Years of Toyota](https://www.toyota-global.com/company/history_of_toyota/75years/vehicle_lineage/family_tree/index.html)
6. Start script: \
``` python ./main.py ```