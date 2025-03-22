import pandas as pd

def load_and_clean_data(csv_path):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    print("Columns in CSV:", df.columns.tolist())

    if 'is_canceled' not in df.columns:
        raise KeyError("Column 'is_canceled' not found in CSV. Please verify your CSV headers.")
    
    df['is_canceled'] = df['is_canceled'].astype(int)
    
    if 'reservation_status_date' in df.columns:
        df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'], errors='coerce')
    
    if all(col in df.columns for col in ['arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month']):
        df['arrival_date'] = pd.to_datetime(
            df['arrival_date_year'].astype(str) + '-' +
            df['arrival_date_month'] + '-' +
            df['arrival_date_day_of_month'].astype(str),
            errors='coerce'
        )
    else:
        df['arrival_date'] = pd.NaT

    df = df.dropna(subset=['arrival_date', 'lead_time'])
    
    return df

if __name__ == '__main__':
    csv_path = 'hotel_bookings.csv'
    df = load_and_clean_data(csv_path)
    print(df.head())
