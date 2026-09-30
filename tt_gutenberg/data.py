import pandas as pd


def get_authors():
    return pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    )


def get_metadata():
    return pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"
    )


def get_languages():
    return pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv"
    )
def get_language_counts():
    metadata = get_metadata()
    languages = get_languages()

    merged = metadata[
        ["gutenberg_id", "gutenberg_author_id"]
    ].dropna(subset=["gutenberg_author_id"])

    merged = merged.merge(
        languages[["gutenberg_id", "language"]],
        on="gutenberg_id"
    )

    counts = (
        merged.groupby("gutenberg_author_id")["language"]
        .nunique()
        .reset_index(name="language_count")
    )

    return counts