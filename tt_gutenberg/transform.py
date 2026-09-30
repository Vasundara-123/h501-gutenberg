import pandas as pd
from . import DATA


def get_data():
    authors = pd.read_csv(
        f"{DATA}/gutenberg_authors.csv"
    )

    metadata = pd.read_csv(
        f"{DATA}/gutenberg_metadata.csv"
    )

    metadata = metadata.drop(columns=["author"])

    data = pd.merge(
        authors,
        metadata,
        on="gutenberg_author_id"
    )

    return data