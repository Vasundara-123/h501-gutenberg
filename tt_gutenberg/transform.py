from . import DATA


def get_data():
    authors = DATA["df_authors"]
    metadata = DATA["df_metadata"]

    data = authors.merge(
        metadata,
        on="gutenberg_author_id"
    )

    return data