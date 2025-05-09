
import pandas as pd

def get_transactions_for_month(connection, year, month):
    """
    Fetches transactions for a given month and year, excluding account_id.

    Parameters:
        connection: psycopg2 connection object.
        year (int): Year of the transactions.
        month (int): Month of the transactions.

    Returns:
        pd.DataFrame: DataFrame with transaction_id, amount, transaction_date.
    """
    try:
        query = f"""
            SELECT transaction_id, amount, transaction_date
            FROM transactions
            WHERE EXTRACT(YEAR FROM transaction_date) = {year}
            AND EXTRACT(MONTH FROM transaction_date) = {month};
        """
        df = pd.read_sql_query(query, connection)
        if df.empty:
            print("No transactions found for the specified month and year.")
            return pd.DataFrame({
                "transaction_id": [-1],
                "amount": [-1],
                "transaction_date": [None]
            })
        return df
    except Exception as e:
        print(f"❌ Error: {e}")
        return pd.DataFrame({
            "transaction_id": [-1],
            "amount": [-1],
            "transaction_date": [None]
        })
