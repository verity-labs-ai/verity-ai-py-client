# CrawlerJobRequestPublic

Public model for creating a crawler job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Root domain for crawling. | [optional] 
**urls** | **List[str]** | List of URLs to crawl. | [optional] 
**include_types** | **List[str]** | Content types to include. | 
**url_paths** | **List[str]** | Specific URL paths to crawl. | [optional] 
**js_flag** | **bool** | Enable JavaScript rendering for SPA sites. | [optional] [default to False]

## Example

```python
from verity_ai_pyc.models.crawler_job_request_public import CrawlerJobRequestPublic

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlerJobRequestPublic from a JSON string
crawler_job_request_public_instance = CrawlerJobRequestPublic.from_json(json)
# print the JSON string representation of the object
print(CrawlerJobRequestPublic.to_json())

# convert the object into a dict
crawler_job_request_public_dict = crawler_job_request_public_instance.to_dict()
# create an instance of CrawlerJobRequestPublic from a dict
crawler_job_request_public_from_dict = CrawlerJobRequestPublic.from_dict(crawler_job_request_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


