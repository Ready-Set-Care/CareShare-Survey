def get_segmentation(segment_name, df):
    """
    Parameters
    ----------
        segment_name: the name of segment
        df: the entire dataframe

    Output
    ------
    Python dict:
        Keys -> name of each segment within the segmentation
        Values -> the code that goes inside df.loc[____] to access
    """

    SEGMENTATIONS = {
        "Provider or Receiver": {
            "Provider": df.loc[df["Q18"] == "provide financial help for caregiving costs to a family member"],
            "Receiver": df.loc[df["Q18"] == "ask for financial help from other family members for caregiving costs"]
        },
        "More or less fair": {
            "Not fair at all": df.loc[df["Q9"] == 1],
            "Somewhat unfair":  df.loc[df["Q9"] == 2],
            "Neutral":  df.loc[df["Q9"] == 3],
            "Somewhat fair":  df.loc[df["Q9"] == 4],
            "Very fair":  df.loc[df["Q9"] == 5]
        }
    }

    return SEGMENTATIONS.get(segment_name, 'Not Found') # if not presemt, return 'Not found'