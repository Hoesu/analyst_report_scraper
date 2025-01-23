# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class AnalystReportItem(scrapy.Item):
    """
    Represents an analyst report item with key fields extracted from the source website.
    """
    title = scrapy.Field(
        serializer=str, 
        metadata={"description": "제목"}
    )
    date = scrapy.Field(
        serializer=str, 
        metadata={"description": "작성일"}
    )
    category = scrapy.Field(
        serializer=str, 
        metadata={"description": "분류"}
    )
    author = scrapy.Field(
        serializer=str, 
        metadata={"description": "작성자"}
    )
    source = scrapy.Field(
        serializer=str, 
        metadata={"description": "제공출처"}
    )
    id = scrapy.Field(
        serializer=int, 
        metadata={"description": "파일ID"}
    )
    files = scrapy.Field()
    file_urls = scrapy.Field()