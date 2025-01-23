import scrapy
from analyst_report.items import AnalystReportItem

class HkConsensusSpider(scrapy.Spider):
    sdate = "2025-01-01"
    edate = "2025-01-22"
    pagenum = "80"
    name = "hk_consensus"
    allowed_domains = ["consensus.hankyung.com"]
    start_urls = [f"https://consensus.hankyung.com/analysis/list?&sdate={sdate}&edate={edate}&order_type=&pagenum={pagenum}"]
    
    custom_settings = {
        "FEEDS" : {
            "s3://analyst-report/hk_consensus/metadata.jsonl": {"format": "jsonlines", "overwrite": True}
        }
    }
 
    def parse(self, response):
        reports = response.css('tr')
        for report in reports[1:]:
            analyst_report_item = AnalystReportItem()
            analyst_report_item['title']     = report.css('.text_l a::text').get()
            analyst_report_item['date']      = report.css('td::text').getall()[0]
            analyst_report_item['category']  = report.css('td::text').getall()[1]
            analyst_report_item['author']    = report.css('td::text').getall()[5]
            analyst_report_item['source']    = report.css('td::text').getall()[6]
            file_url = f"https://consensus.hankyung.com{report.css('.text_l a').attrib['href']}"
            analyst_report_item['file_urls'] = [file_url]
            analyst_report_item['id']        = file_url.split("=")[-1]
            yield analyst_report_item

        next_page = response.xpath('//div[@class="paging"]/span/following-sibling::a[1]')
        if next_page.xpath('./@class').get() == "btn last":
            return
        else:
            next_page_url = next_page.xpath('./@href').get()
            yield response.follow(next_page_url, callback = self.parse)