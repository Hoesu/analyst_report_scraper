
# Analyst Report Webscraper

증권사 애널리스트 리포트를 웹스크레이핑으로 가져와서 Amazon S3 Bucket에 담아보자.
## Installation

This repo was built using python 3.11 conda environment.
```bash
  conda env create --name YOUR_ENV_NAME --file environment.yaml
  conda activate YOUR_ENV_NAME
```
## Deployment

currently active spiders: hk_consensus
```python
  cd analyst_report
  scrapy crawl SPIDER_NAME
```
## Author

- [@Hoesu Chung](https://github.com/Hoesu)
## Acknowledgements

 - [Scrapy](https://scrapy.org/)