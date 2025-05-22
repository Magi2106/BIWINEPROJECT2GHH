# /src/pca_transform.py

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def apply_pca(df, n_components=3):
    numeric_df = df.select_dtypes(include=['float64', 'int64']).drop(columns=['quality'], errors='ignore')
    
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_df)

    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(scaled_data)

    columns = [f"PC{i+1}" for i in range(n_components)]
    pca_df = pd.DataFrame(data=principal_components, columns=columns)
    
    if 'quality' in df.columns:
        pca_df['quality'] = df['quality'].values

    return pca_df, pca.explained_variance_ratio_

def print_sample(df, n=10):
    print(df.sample(n))
