# redix-client

Python client for Redix Healthcare Data Conversion REST API.

## Install

```sh
pip install redix-client
```

## Usage

```python
from redix_client import RedixClient, ConversionFlag, FileType, WarningLevel

client = RedixClient(api_url="http://localhost:8000", api_key="YOUR_API_KEY")
# Start batch
batch = client.batch_convert_folder(Input_Subfolder="myfolder", Config_Profile="x12_837P_default_profile")
# Check status
status = client.batch_status(batch['job_id'])
# Upload file
up_result = client.upload_to_staging("myfile.txt")
# Convert uploaded file
conv_result = client.convert_staging_file(Staged_Filename=up_result.filename)
# Download file
client.download_file(File_Type=FileType.OUTPUT, Filename="yourfile.txt")
# View file
view = client.view_file(File_Type=FileType.OUTPUT, Filename="yourfile.txt")
print(view.content)
# Error handling
try:
    client.batch_status("invalid_id")
except RedixAPIError as e:
    print(e)
```

## Endpoints Supported

- Batch processing (submit, status, list, logs, file details, summary)
- File upload/download/view/delete (staging, shared, etc.)
- Listing (form options, files, staging files/profiles, server files)
- Conversions (file upload, staging file)
- Health and engine info

## Error Handling

All API errors raise `RedixAPIError` with status code and message.

## License

MIT