def map_dtypes_names(column_name:str, dtype: str):
    lower_case_dtype = dtype.lower()
    lower_case_col_name = column_name.lower()
    numeric_symbols = ['int', 'float']
    indications_to_ignore = ['id']
    for item_to_ignore in indications_to_ignore:
        if item_to_ignore in lower_case_col_name:
            return lower_case_dtype
    for item in numeric_symbols:
        if item in lower_case_dtype:
            return 'number'
    if lower_case_dtype == 'object':
        return 'str_or_mixed'
    else:
        return lower_case_dtype


def map_dtypes(df):
    dtypes = {}
    for col_name in df.columns:
        col = df[col_name]
        col_dtype = map_dtypes_names(col_name, str(col.dtype))
        if col_dtype not in dtypes:
            dtypes[col_dtype] = []
        dtypes[col_dtype].append(col_name)
    return dtypes
