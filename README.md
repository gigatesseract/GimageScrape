# GimageScrape
A simple tool to scrape google images by simply specifying queries


## Instructions:
1. `git clone https://github.com/gigatesseract/GimageScrape.git`    
1. Install virtualenv (recommended) `pip install vitualenv`    
1. Create virtual environment `virtualenv env`   
1. Activate the virtual environment `source env/bin/activate` (You can deactivate it by `source deactivate`)    
1. Install requirements. `pip install -r requirements.txt`    
1. Populate _to_search.txt_ with your search queries. Make sure each query is in a new line. See _to_search.txt_ for more details. Currently doesnt support space separated queries.    
1. `cd googleScraper`   
1. In the _settings.py_ file, add the following line:   
   `IMAGES_STORE = "path/to/valid/dir"`
   where the value is a path to any valid directory    
1. `scrapy crawl search`    

Sit back and relax. Each searh query will create a new folder and populate it with 20 images. These folders will be created in the valid directoyr as mentioned in the `IMAGES_STORE` in `settings.py`

### License
[MIT](https://github.com/gigatesseract/GimageScrape/blob/master/LICENSE)
