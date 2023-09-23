import pandas as pd

file_path = '../cleandata/clean_rta.csv'
processed_path = '../processed_data/rta.csv'


def ingest_data(path: str) -> pd.DataFrame:
    print(f'Ingesting data from {path}')
    df = pd.read_csv(path, header=0, dtype=int, index_col=0)

    return df


def victims_per_accident(df: pd.DataFrame) -> pd.DataFrame:
    # In this simple function we will simply calculate the average of victims per accident, considering that
    # deaths and injuries are not intersectable
    print('Calculating number of victims per accident.')
    df['VICTIMS_PER_ACCIDENT'] = (df.INJURIES + df.DEATHS) / df.ACCIDENTS_WITH_VICTIMS

    # I want this data to be represented in 0.00 format.
    df.VICTIMS_PER_ACCIDENT = df.VICTIMS_PER_ACCIDENT.round(2)

    return df


def accidents_cumulative(df: pd.DataFrame) -> pd.DataFrame:
    # In this function I want to create ways to shows me a trend: if accidents have increased or decreased
    print('Calculating trend.')
    df['PERCENTAGE_INCREASE_IN_ACCIDENTS'] = df.ACCIDENTS_WITH_VICTIMS.pct_change().fillna(0).round(2)
    df['PERCENTAGE_INCREASE_IN_INJURIES'] = df.INJURIES.pct_change().fillna(0).round(2)
    df['PERCENTAGE_INCREASE_IN_DEATHS'] = df.DEATHS.pct_change().fillna(0).round(2)

    return df


def main():
    df = ingest_data(file_path)

    df = victims_per_accident(df)

    df = accidents_cumulative(df)

    print(f'Writing csv to {processed_path}')
    df.to_csv(processed_path)


if __name__ == '__main__':
    main()