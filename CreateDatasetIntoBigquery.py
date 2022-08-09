from google.cloud import bigquery
from google.cloud.exceptions import NotFound


client = bigquery.Client()
datasets_name = ['Dataset1','Dataset10','Dataset13']
location = 'US'
project = 'massive-boulder-358319'
def create_bigquery_dataset(dataset_name,project):
    """Create bigquery dataset. Check first if the dataset exists
        Args:
            dataset_name: String
    """
    
    dataset_id = "{}.{}".format(project, dataset_name)
 
    try:
        client.get_dataset(dataset_id)
        print("Dataset {} already exists".format(dataset_id))
    except NotFound:
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = location
        dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
        print("Created dataset {}.{}".format(client.project, dataset.dataset_id))


for name in datasets_name:
    create_bigquery_dataset(name,project)