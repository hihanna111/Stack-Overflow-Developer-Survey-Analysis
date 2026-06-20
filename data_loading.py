import pandas as pd
import gdown


def load_data():
    """
    Download and load survey datasets.
    """

    file_id = "1sWvTthFAMt2Hn-9hpO4MebnbtiOVDnsB"
    schema_id = "1DqogmP4X7iStjzZpAhuMeRxNXjiZq1p3"

    survey_url = f"https://drive.google.com/uc?id={file_id}"
    schema_url = f"https://drive.google.com/uc?id={schema_id}"

    survey_file = "data/survey_results.csv"
    schema_file = "data/survey_schema.csv"

    gdown.download(survey_url, survey_file, quiet=False)
    gdown.download(schema_url, schema_file, quiet=False)

    survey_df = pd.read_csv(survey_file)
    schema_df = pd.read_csv(schema_file)

    return survey_df, schema_df
