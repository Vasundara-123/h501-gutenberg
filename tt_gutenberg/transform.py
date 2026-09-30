import pandas as pd


def get_data():
    authors = pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    )

    metadata = pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"
    )

    metadata = metadata.drop(columns=["author"])

    data = pd.merge(
        authors,
        metadata,
        on="gutenberg_author_id"
    )

    return data