import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def revenue_trends(df):
    df['month'] = df['arrival_date'].dt.to_period('M')
    revenue_by_month = df.groupby('month')['adr'].sum().reset_index() if 'adr' in df.columns else None
    if revenue_by_month is not None:
        revenue_by_month['month'] = revenue_by_month['month'].dt.to_timestamp()
    return revenue_by_month

def cancellation_rate(df):
    total = len(df)
    canceled = df['is_canceled'].sum()
    rate = (canceled / total) * 100
    return rate

def geographical_distribution(df):
    distribution = df['country'].value_counts().reset_index()
    distribution.columns = ['country', 'bookings']
    return distribution

def lead_time_distribution(df):
    return df['lead_time']

def plot_revenue_trends(revenue_by_month):
    if revenue_by_month is not None:
        plt.figure(figsize=(10,6))
        sns.lineplot(x='month', y='adr', data=revenue_by_month, marker='o')
        plt.title('Revenue Trends Over Time (using ADR)')
        plt.xlabel('Month')
        plt.ylabel('Revenue (ADR sum)')
        plt.tight_layout()
        plt.savefig('revenue_trends.png')
        plt.close()
