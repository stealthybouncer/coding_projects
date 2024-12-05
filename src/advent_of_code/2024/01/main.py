import pandas as pd
import os

data_file = './data/raw/aoc/2024/01/input.txt'
expanded_path = os.path.expanduser(data_file)

def test_file_exists():
    assert os.path.exists(expanded_path) == True


def get_data_as_df() -> pd.DataFrame:
    df = pd.read_csv(expanded_path,
                     header=None,
                     delimiter='   ',
                     )
    return df

def get_sorted_df(numbs_df: pd.DataFrame) -> pd.DataFrame:
    sorted_df = pd.DataFrame()
    sorted_df['col1'] = numbs_df.iloc[:, 0].sort_values().values
    sorted_df['col2'] = numbs_df.iloc[:, 1].sort_values().values
    return sorted_df

def calc_sorted_dists(sorted_df: pd.DataFrame):
    sorted_df['dist'] = sorted_df['col2'].subtract(sorted_df['col1']).abs()


def get_similarity_df(sorted_df: pd.DataFrame) -> pd.DataFrame:
    similarity_df = pd.merge(sorted_df[['col1']],
                             sorted_df[['col2']],
                             left_on='col1',
                             right_on='col2',
                             how='inner')
    return similarity_df

data = get_data_as_df()
sorted_data = get_sorted_df(data)
print(data)
print(sorted_data)
calc_sorted_dists(sorted_data)
print(sorted_data)
print(sorted_data['dist'].sum())

similarity_df = get_similarity_df(sorted_data)
print(similarity_df['col2'].sum())