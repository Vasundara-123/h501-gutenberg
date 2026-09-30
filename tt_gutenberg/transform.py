from . import DATA


def get_data():
    #Select required columns from authors dataset
    authors = DATA["df_authors"][
        ["gutenberg_author_id", "alias", "birthdate"]
    ].rename(columns={"alias": "author_alias"})
    # Selecting required columns from metadata dataset
    metadata = DATA["df_metadata"][
        ["gutenberg_author_id", "author", "language"]
    ]
    # Merge both the datasets based on author ID
    data = authors.merge(
        metadata,
        on="gutenberg_author_id"
    )

    return data