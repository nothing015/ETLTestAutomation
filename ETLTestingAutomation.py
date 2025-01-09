import pytest
import pandas as pd

def test_duplicates():
    """Check for duplicate records in target CSV file.
    Fails if any duplicates are found."""
    targetdf = pd.read_csv("target.csv", sep=",")
    count = targetdf.duplicated().sum()
    assert count == 0, "Duplicate found -- Please verify the target"

def test_DataCompleteness():
    """Verify target CSV file is not empty.
    Fails if file contains no data."""
    target_df = pd.read_csv("target.csv")
    assert not target_df.empty, "Target file is empty -- Please verify the ETL process"

def test_deptNoForNullValueCheck():
    """Check for NULL values in department number column.
    Fails if any NULL values found in deptno."""
    target_df = pd.read_csv("target.csv")
    isDepthNoNull = target_df["deptno"].isnull().any()
    assert isDepthNoNull == False, "Dept.No has NULL value -- Please check"

def test_enoNoForUniqueValueCheck():
    """Verify employee numbers are unique.
    Fails if any duplicate eno values found."""
    target_df = pd.read_csv("target.csv")
    # Compare total count vs unique count
    totalcount = target_df["eno"].count()
    deptNoUniqueValueCount = len(target_df["eno"].unique())
    assert totalcount == deptNoUniqueValueCount, "eno column values are not unique -- Please check"