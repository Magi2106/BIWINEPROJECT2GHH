# /src/eda.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def load_and_combine(red_path, white_path):
    red_df = pd.read_excel(red_path)
    white_df = pd.read_excel(white_path)
    red_df['type'] = 'red'
    white_df['type'] = 'white'
    return pd.concat([red_df, white_df], ignore_index=True)

def encode_categorical(df):
    return pd.get_dummies(df, columns=['type'], drop_first=True)

def descriptive_statistics(df):
    return df.describe()

def check_normal_distribution(df, column):
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.show()

def quality_comparison(df):
    fig = px.box(df, x="type", y="quality", color="type", points="all", title="Wine Quality Comparison")
    fig.show()

def correlation_matrix(df):
    numeric = df.select_dtypes(include=['float64', 'int64'])
    corr = numeric.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()
    return corr

def bin_ph(df, bins=5):
    labels = [f"Bin {i+1}" for i in range(bins)]
    df['pH_bin'] = pd.cut(df['pH'], bins=bins, labels=labels)
    return df

def remove_outliers(df, column, z_thresh=3):
    from scipy.stats import zscore
    df['zscore'] = zscore(df[column])
    cleaned_df = df[abs(df['zscore']) < z_thresh]
    return cleaned_df.drop(columns='zscore')
