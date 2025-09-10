import pandas as pd
import re

def extract_data_from_text(text: str) -> list[dict]:
    """
    Extracts key data points from the article text using regular expressions.

    Args:
        text (str): The aggregated text content from all articles.

    Returns:
        list[dict]: A list of dictionaries, each containing a data point.
    """
    if not text:
        return

    # Regex patterns to find specific data points
    patterns = {
        'total_consumption_2019': r"5,?071 million DDDs",
        'per_capita_did_2019': r"10.3 DIDs|10.4 DDD/1000/day",
        'who_access_target': r"at least 60%",
        'access_share_2019': r"Access contributed 27.0%",
        'watch_share_2019': r"Watch contributed 54.9%",
        'private_sector_dominance': r"private sector accounts for 85%–90%",
        'azithromycin_most_consumed': r"azithromycin 500mg tablet.*?\(7.6\s?percent\)",
        'cefixime_second_consumed': r"cefixime 200\s?mg tablet.*?\(6.5\s?percent\)",
        'unapproved_formulations_share': r"unapproved formulations contributed 47.1%",
    }

    data_points =
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            data_points.append({
                'Metric': key,
                'Value': match.group(0)
            })
            
    return data_points

def structure_data(data_points: list[dict]) -> pd.DataFrame:
    """
    Converts the list of data points into a structured pandas DataFrame.

    Args:
        data_points (list[dict]): A list of dictionaries from extract_data_from_text.

    Returns:
        pd.DataFrame: A structured DataFrame of the extracted data.
    """
    if not data_points:
        return pd.DataFrame()
        
    df = pd.DataFrame(data_points)
    
    # Clean up the 'Value' column to extract numerical data
    df['NumericValue'] = df['Value'].str.extract(r'(\d+\.?\d*)').astype(float)
    
    return df
