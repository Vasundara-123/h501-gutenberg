from .transform import get_data


def list_authors(by_languages=False, alias=False):
    data = get_data()

    if alias:
        name_column = "author_alias"
    else:
        name_column = "author"

    data = data.dropna(subset=[name_column])

    if by_languages:
        language_counts = (
            data.groupby(name_column)["language"]
            .nunique()
            .sort_values(ascending=False)
        )

        return language_counts.index.tolist()

    return data[name_column].drop_duplicates().tolist()