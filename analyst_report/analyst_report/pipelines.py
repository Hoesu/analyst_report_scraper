# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline

class AnalystReportPipeline:
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name not in ['file_urls', 'files']:
                value = adapter.get(field_name)
                adapter[field_name] = value.strip()
        return item
    
class AnalystReportFilesPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None, *, item):
        file_name = request.url.split("=")[-1]
        file_name = f"{file_name}.pdf"
        return file_name