from .data import get_authors, get_language_counts


def list_authors(by_languages=False, alias=False):
    authors = get_authors()

    if alias:
        authors = authors.dropna(subset=["alias"])
        name_column = "alias"
    else:
        name_column = "author"

    if by_languages:
        language_counts = get_language_counts()

        authors = authors.merge(
            language_counts,
            on="gutenberg_author_id",
            how="left"
        )

        authors["language_count"] = authors["language_count"].fillna(0)

        authors = authors.sort_values(
            "language_count",
            ascending=False
        )

    return authors[name_column].tolist()