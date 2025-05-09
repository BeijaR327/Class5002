
import matplotlib.pyplot as plt
from db_connections import connect_to_bank
from db_queries import get_transactions_for_month

class DatabaseManager:

    def __init__(self, vault_file):
        self.vault_file = vault_file
        self.connection = connect_to_bank(vault_file)
        self.data_table = None

    def fetch_transactions(self, year, month):
        self.data_table = get_transactions_for_month(self.connection, year, month)
        return self.data_table

    def plot_transactions_by_day(self, year, month):
        df = self.fetch_transactions(year, month)
        if df is not None and df.iloc[0]["transaction_id"] != -1:
            df["day"] = pd.to_datetime(df["transaction_date"]).dt.day
            grouped = df.groupby("day")["amount"].sum()
            grouped.plot(kind="bar", title=f"Transactions in {month}/{year}")
            plt.xlabel("Day")
            plt.ylabel("Total Amount")
            plt.tight_layout()
            plt.show()
        else:
            print("No valid data available to plot.")
