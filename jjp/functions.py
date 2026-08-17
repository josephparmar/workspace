import pandas as pd


def sort_dataframe(data : str, sort : str):
    '''
    Converts the input csv to a pandas dataframe, 
    converts all the data types to their auto types (str, int etc.),
    and sorts the data by the user defined header

    Args:
        data (str or path): Path to input csv file, with headers. 
        header (str or None): name of header you want to sort by. Use None for no sorting.

    Returns:
        df : sorted pandas dataframe. Turn column into numpy array by using df["header"].to_numpy()
    '''
    df = pd.read_csv(data)
    df.convert_dtypes()
    if sort != None:
        df.sort_values(by=[sort], inplace=True, ignore_index=True)
    return df 