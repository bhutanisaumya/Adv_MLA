import pandas as pd
import seaborn as sns
import warnings
from datetime import datetime
from scipy.stats import skew
from sklearn.preprocessing import PowerTransformer
from sklearn.impute import SimpleImputer

class DataProcessor:
    def __init__(self):
        pass

    def load_data(self, train_url, test_url):
        # Load train and test data from URLs
        df_train = pd.read_csv(train_url)
        df_test = pd.read_csv(test_url)

        return df_train, df_test
    
    def process_data(self, train_url, test_url, stable=True):
        # Call load_data with the provided URLs
        df_train, df_test = self.load_data(train_url, test_url)
        self.explore_data(df_train)
        df_train_clean = self.preprocess(df_train)
        df_test_clean = self.preprocess(df_test)
        self.save_preprocessed_data(df_train_clean, df_test_clean)

    def explore_data(self, df):
        # Display basic data exploration for a given DataFrame
        print("First 5 rows:")
        print(df.head())

        print("\nLast 5 rows:")
        print(df.tail())

        print("\nDescriptive statistics:")
        print(df.describe())

        print("\nInfo:")
        print(df.info())

        print("\nShape:")
        print(df.shape)

        # Sum of null values in the dataframe
        print(df.isnull().sum())

    def convert_date_to_float(self, date_str):
        if isinstance(date_str, str):
            parts = date_str.split('-')
            if len(parts) == 2:
                try:
                    day = parts[0]
                    month = parts[1]

                    # Create a datetime object with a dummy year (e.g., 2023)
                    date_object = datetime.strptime(f"2023-{month}-{day}", "%Y-%b-%d")

                    # Convert the datetime object to a float representing 2/06/2023
                    float_date = float(date_object.strftime("%m.%d"))
                    return float_date
                except ValueError:
                    return None  # Handle non-convertible values here if needed
            else:
                return None  # Handle cases where the date format is not as expected
        else:
            return date_str  # Return the value as is if it's not a string

    def impute_missing_values(self, df):
        # List of selected features
        selected_features = ['Rec_Rank','ast_tov', 'rimmade', 'rimmade_rimmiss', 'midmade', 'midmade_midmiss',
                        'dunksmade', 'dunksmiss_dunksmade', 'pick', 'drtg', 'adrtg','dporpag', 'stops','bpm', 'obpm', 
                        'dbpm', 'gbpm','mp','ogbpm', 'dgbpm', 'oreb', 'dreb', 'treb', 'ast','stl', 'blk', 'pts']

        # Calculate skewness for each feature
        skewness = {}
        for feature in selected_features:
            skew_value = skew(df[feature].dropna())
            skewness[feature] = skew_value

        # Define a threshold for skewness to categorize features
        low_skewness_threshold = 1
        high_skewness_threshold = 2

        # Impute missing values based on skewness
        for feature in selected_features:
            # Identify the skewness category
            if abs(skewness[feature]) < low_skewness_threshold:
                # Low skewness: Impute with median
                imputer = SimpleImputer(strategy='median')
            elif abs(skewness[feature]) < high_skewness_threshold:
                # Moderate skewness: Apply a transformation (Yeo-Johnson) and impute with mean
                transformer = PowerTransformer(method='yeo-johnson', standardize=False)
                imputer = SimpleImputer(strategy='mean')
                df[feature] = transformer.fit_transform(df[feature].values.reshape(-1, 1))
            else:
                # High skewness: Apply a transformation (Yeo-Johnson) and impute with median
                transformer = PowerTransformer(method='yeo-johnson', standardize=False)
                imputer = SimpleImputer(strategy='median')
                df[feature] = transformer.fit_transform(df[feature].values.reshape(-1, 1))

            # Impute missing values for the feature
            df[feature] = imputer.fit_transform(df[feature].values.reshape(-1, 1))

        return df

    def preprocess(self, df):
        # Apply preprocessing and missing value imputation
        df = self.impute_missing_values(df)

        # Calculate ratio (rim_ratio, mid_ratio, dunks_ratio)
        rim_ratio_train = df['rimmade'] / df['rimmade_rimmiss']
        mid_ratio_train = df['midmade'] / df['midmade_midmiss']
        dunks_ratio_train = df['dunksmade'] / df['dunksmiss_dunksmade']

        # Impute the missing values with calculated ratios
        df['rim_ratio'] = df['rim_ratio'].fillna(rim_ratio_train)
        df['mid_ratio'] = df['mid_ratio'].fillna(mid_ratio_train)
        df['dunks_ratio'] = df['dunks_ratio'].fillna(dunks_ratio_train)

        # List of ratio columns
        ratio_columns = ['rim_ratio', 'mid_ratio', 'dunks_ratio']

        # Calculate the median of each ratio column
        mean_values = df[ratio_columns].median()

        # Replace NaN values with the mean for each column
        for col in ratio_columns:
            df[col].fillna(mean_values[col], inplace=True)

        # List of columns to drop
        to_drop = ['yr', 'num']
        # Drop the specified columns
        df.drop(columns=to_drop, inplace=True)

        # Handling 'ht' column
        # Apply the conversion function to the 'ht' column
        df['ht'] = df['ht'].apply(self.convert_date_to_float)

        # Replace NaN values in 'ht' column with the median of non-NaN values
        median_ht = df['ht'].median()
        df['ht'].fillna(median_ht, inplace=True)

        return df

    def save_preprocessed_data(self, df_train, df_test):
        df_train.to_csv('processed_train.csv', index=False)
        df_test.to_csv('processed_test.csv', index=False)

def main():
    # Set up warnings
    warnings.filterwarnings('ignore')
    
    # URLs for train and test data
    train_url = 'https://raw.githubusercontent.com/bhutanisaumya/AMLA/main/train.csv'
    test_url = 'https://raw.githubusercontent.com/bhutanisaumya/AMLA/main/test.csv'

    # Initialize the DataProcessor class
    data_processor = DataProcessor()

    # Process the data
    data_processor.process_data(train_url, test_url)

if __name__ == "__main__":
    main()
