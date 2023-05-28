import gcsfs
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

from utils import *

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    res, status_code = get_request_input(request, "content", "H")
    res += " another string"

    CSV_PATH = "gs://csv_urban_data_098765/POI_200.csv"
    fs = gcsfs.GCSFileSystem(project='my-project')
    with fs.open(CSV_PATH) as f:
        df = pd.read_csv(f)
        
    print(df.columns)
    columns_to_exclude = ["PLOT_ID", "X", "Y"]
    

    # Karim's preprocessing:
    df = df.drop(columns=columns_to_exclude)
    df = df.fillna(df.mean())
    scaler = MinMaxScaler()
    df = pd.DataFrame(scaler.fit_transform(df),columns=df.columns)

    # KMEANS
    km_model = KMeans(n_clusters=10,)
    km_model.fit(df)
    res = km_model.labels_# res is np.array

    # numpy array can not be sent back. 
    # It needs to be converted to a list of int first:
    res = [int(x) for x in res]  # list<int>
    
    return build_response(res, status_code)
