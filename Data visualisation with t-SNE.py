import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE

def load_data(filepath):
    """
    Load dataset from CSV or Excel file
    
    Parameters:
    filepath (str): Path to the dataset file
    
    Returns:
    tuple: (feature matrix, optional labels)
    """
    # Determine file type
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format. Use CSV or Excel.")
    
    return df

def prepare_tsne_data(df, feature_columns, label_column=None):
    """
    Prepare data for t-SNE visualization
    
    Parameters:
    df (pandas.DataFrame): Input dataframe
    feature_columns (list): Columns to use as features
    label_column (str, optional): Column to use for coloring
    
    Returns:
    tuple: (features, optional labels)
    """
    # Extract features
    X = df[feature_columns].values
    
    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Get labels if specified
    y = df[label_column].values if label_column else None
    
    return X_scaled, y

def tsne_visualization(X, y=None, perplexity=30):
    """
    Perform t-SNE and create visualization
    
    Parameters:
    X (numpy.ndarray): Scaled feature matrix
    y (numpy.ndarray, optional): Labels for coloring
    perplexity (int): t-SNE perplexity parameter
    """
    # Perform t-SNE
    tsne = TSNE(
        n_components=2, 
        random_state=42, 
        perplexity=min(perplexity, len(X)-1)
    )
    X_tsne = tsne.fit_transform(X)
    
    # Create visualization
    plt.figure(figsize=(10, 8))
    
    if y is not None:
        # Scatter plot with labels
        scatter = plt.scatter(
            X_tsne[:, 0], 
            X_tsne[:, 1], 
            c=y, 
            cmap='viridis', 
            alpha=0.7
        )
        plt.colorbar(scatter, label='Class')
        plt.title('t-SNE Visualization with Labels')
    else:
        # Scatter plot without labels
        plt.scatter(X_tsne[:, 0], X_tsne[:, 1], alpha=0.7)
        plt.title('t-SNE Visualization')
    
    plt.xlabel('t-SNE Dimension 1')
    plt.ylabel('t-SNE Dimension 2')
    plt.tight_layout()
    plt.show()

def main():
    # User inputs
    filepath = input("Enter the path to your dataset (CSV/Excel): ")
    
    # Load data
    df = load_data(filepath)
    
    # Print available columns
    print("\nAvailable columns:")
    print(df.columns.tolist())
    
    # Get feature columns
    feature_input = input("\nEnter feature column names (comma-separated): ")
    feature_columns = [col.strip() for col in feature_input.split(',')]
    
    # Optional: Get label column
    label_column = input("\nEnter label column name (press Enter to skip): ").strip() or None
    
    # Prepare and visualize
    X_scaled, y = prepare_tsne_data(df, feature_columns, label_column)
    tsne_visualization(X_scaled, y)

if __name__ == '__main__':
    main()