from . import DATA


def get_data():
    authors = DATA["df_authors"][
        ["gutenberg_author_id", "alias", "birthdate"]
    ].rename(columns={"alias": "author_alias"})

    metadata = DATA["df_metadata"][
        ["gutenberg_author_id", "author", "language"]
    ]

    data = authors.merge(
        metadata,
        on="gutenberg_author_id"
    )

    return data