# CrawlerJobStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**status** | **str** |  | 
**progress** | **int** |  | 
**error** | **str** |  | 
**result_url** | **str** |  | 
**organisation** | **str** |  | 
**user_id** | **str** |  | 
**submitted_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from verity_ai_pyc.models.crawler_job_status_response import CrawlerJobStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlerJobStatusResponse from a JSON string
crawler_job_status_response_instance = CrawlerJobStatusResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlerJobStatusResponse.to_json())

# convert the object into a dict
crawler_job_status_response_dict = crawler_job_status_response_instance.to_dict()
# create an instance of CrawlerJobStatusResponse from a dict
crawler_job_status_response_from_dict = CrawlerJobStatusResponse.from_dict(crawler_job_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


