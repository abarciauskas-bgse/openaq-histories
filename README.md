# How to generate data

1. Start local OpenAQ API:

```bash
export REQUEST_LIMIT=17000
npm run start
```

2. Query and download data

```bash
export LOCATION=Seattle-Beacon%20Hill
export URL="http://localhost:3004/v1/query?location=${LOCATION}&parameter=pm25&limit=20000"
export SEATTLE_S3=$(curl $URL | jq .results.s3Uri -r)

export LOCATION=Portland%20-%20SE%20Lafaye
export URL="http://localhost:3004/v1/query?location=${LOCATION}&parameter=pm25&limit=20000"
export PORTLAND_S3=$(curl $URL | jq .results.s3Uri -r)

export LOCATION=San%20Francisco
export URL="http://localhost:3004/v1/query?location=${LOCATION}&parameter=pm25&limit=20000"
export SF_S3=$(curl $URL | jq .results.s3Uri -r)

export LOCATION=Los%20Angeles%20-%20N.%20Mai
export URL="http://localhost:3004/v1/query?location=${LOCATION}&parameter=pm25&limit=20000"
export LA_S3=$(curl $URL | jq .results.s3Uri -r)

aws s3 cp $SEATTLE_S3 Seattle-Beacon_Hill.csv
aws s3 cp $PORTLAND_S3 Portland-SE_Lafaye.csv
aws s3 cp $SF_S3 San_Francisco.csv
aws s3 cp $LA_S3 Los_Angeles-N.Mai.csv
```

2. Run `create_timeseries.py`

```bash
python3 create_timeseries.py
```
