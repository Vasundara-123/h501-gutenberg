from .transform import get_data


def list_authors(by_languages=False, alias=False):
    data = get_data()
# Choose to use either author name or pseudonym
    if alias:
        name_column = "author_alias"
    else:
        name_column = "author"
# Exclude rows that lack the chosen name

    data = data.dropna(subset=[name_column])

    if by_languages:
# Count the number of unique languages per author
        language_counts = (
            data.groupby(name_column)["language"]
            .nunique()
            .sort_values(ascending=False)
        )
# Order authors by number of languages, descending
        return language_counts.index.tolist()
# Return list of distinct author names
    return data[name_column].drop_duplicates().tolist()