# CrawlerJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique ID for the crawler job. | 

## Example

```python
from verity_ai_pyc.models.crawler_job_response import CrawlerJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlerJobResponse from a JSON string
crawler_job_response_instance = CrawlerJobResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlerJobResponse.to_json())

# convert the object into a dict
crawler_job_response_dict = crawler_job_response_instance.to_dict()
# create an instance of CrawlerJobResponse from a dict
crawler_job_response_from_dict = CrawlerJobResponse.from_dict(crawler_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


