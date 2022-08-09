from google.cloud import bigquery

# TODO : Change to your project id
PROJECT_ID = "massive-boulder-358319"
GCS_URI = "gs://batchloaddata/Games.csv".format(PROJECT_ID) # make sure you have a CSV file GCS bucket
TABLE_ID = "dataset1.gamestoday".format(PROJECT_ID)

client = bigquery.Client()

def load_gcs_to_bigquery_event_data(GCS_URI, TABLE_ID, table_schema):
    job_config = bigquery.LoadJobConfig(
        schema=table_schema,
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        write_disposition = 'WRITE_APPEND'
        )

    load_job = client.load_table_from_uri(
        GCS_URI, TABLE_ID, job_config=job_config
    )

    load_job.result()
    table = client.get_table(TABLE_ID)

    print("Loaded {} rows to table {}".format(table.num_rows, TABLE_ID))

bigquery_table_schema = [
    bigquery.SchemaField("field1", "STRING"),
    bigquery.SchemaField("field2", "INTEGER"),
    bigquery.SchemaField("field3", "TIMESTAMP"),
    bigquery.SchemaField("field4", "STRING"),
    bigquery.SchemaField("field5", "STRING"),
    bigquery.SchemaField("field6", "TIMESTAMP"),
    bigquery.SchemaField("field7", "STRING"),
    bigquery.SchemaField("field8", "STRING"),
    bigquery.SchemaField("field10", "STRING")
]