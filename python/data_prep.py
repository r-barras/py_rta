import pandas as pd

file_path = '../pordata/road_traffic_accidents.xlsx'
prep_path = '../cleandata/clean_rta.csv'


def prepare_excel(path: str) -> pd.DataFrame:
    # Ingest data
    print(f'Reading excel from {path}')
    df = pd.read_excel(path)

    # Find the index of the first row that holds a value for C1
    first_row_index = df[df.iloc[:, 0].notnull()].index[0]

    # Set the first_row_index row as headers
    df.columns = df.iloc[first_row_index]

    # Filter out the first lines of the dataframe
    df = df.iloc[first_row_index+1:].reset_index(drop=True)

    # Find the index of the first row that holds a null for C1
    last_row_index = df[df.iloc[:, 0].isnull()].index[0]

    # Filter out all lines after the first null
    df = df.iloc[:last_row_index].reset_index(drop=True)

    # Drop columns with no values
    df = df.dropna(axis=1, how='all')

    # Standardize columns
    df.columns = df.columns.str.upper().str.split().str.join("_")
    df.columns.name = None

    print(f'Finished preparing dataframe.')

    return df


def write_csv(df: pd.DataFrame, path: str):
    # Simply write the dataframe to the prep_path folder
    print(f'Writing csv to {path}')
    df.to_csv(path)


def main():
    # Start by ingesting and cleaning the file
    df = prepare_excel(file_path)

    # Then write it to the clean data folder
    write_csv(df, prep_path)


if __name__ == '__main__':
    main()
