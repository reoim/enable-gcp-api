# enable-gcp-api
Enable Google Cloud APIs at Org or Folder level

## Prerequisite
```
gcloud auth login
```
```
gcloud config set project PROJECT_ID
```

## Usage
Run help command to see example of usage
```
python enable-api.py --help

Output>
usage: enable-api.py [-h] -o ORG [-f FOLDER] -s SERVICE [SERVICE ...]

options:
  -h, --help            show this help message and exit
  -o ORG                Example) -o 302793038411
  -f FOLDER             Example) -f 112793038411
  -s SERVICE [SERVICE ...]
                        Example) -s "policyanalyzer.googleapis.com" "bigquery.googleapis.com"
```

**Enbable APIs at Organization level**: Run the script with org id and service names arguments
```
python enable-api.py -o ORG_ID -s SERVICES
```

**Enbable APIs at Folder level**: Run the script with org id, folder id and service names arguments
```
python enable-api.py -o ORG_ID -f FOLDER_ID -s SERVICES
```



