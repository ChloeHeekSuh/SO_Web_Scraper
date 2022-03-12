# Job posts Web Scraper
A web scraper for scraping job posts in Stack Overflow

## Table of contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Setup](#setup)
* [Demo](#demo)

## Introduction
This project is a web scraper for scraping job posts regards Python(Keyword can be changed) in Stack Overflow using Python, Beautiful Soup, Boto3.
	
## Technologies
Project is created with:
* beautifulsoup4 = 4.10.0
* boto3 = 1.20.22
* requests = 2.26.0
* urllib3 = 1.26.7
	
## Setup
To run this project, go to the current directory where you want the cloned directory to be added.\
Use the git clone command along with the copied URL.

```
$ git clone https://github.com/ChloeHeekSuh/SO_Web_Scraper.git
```

And install all requirements if you want to run it in the same environment. \
For that locally using pip:

```
$ pip install -r requirements.txt
```

## Demo
Run the code, then this will save the data to CSV file.
\
![DIAGRAM](https://github.com/ChloeHeekSuh/SO_Web_Scraper/blob/main/screenshot/scraper_2.png)
\
What will you do with this CSV file is depends on you.\
For now, let's simply use this CSV file to analyze the data or apply for the jobs easily with the link with Google Sheets.
\
![DIAGRAM](https://github.com/ChloeHeekSuh/SO_Web_Scraper/blob/main/screenshot/scraper_3.png)
\
Go to 'File' > 'import'\
Change the separator type to 'Comma' and import the data.
\
![DIAGRAM](https://github.com/ChloeHeekSuh/SO_Web_Scraper/blob/main/screenshot/scraper_4.png)
