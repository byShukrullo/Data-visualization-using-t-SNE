# t-SNE Visualization Tool

## Overview

This Python script provides a flexible tool for performing t-SNE (t-Distributed Stochastic Neighbor Embedding) visualization on your datasets. t-SNE is a powerful technique for dimensionality reduction and visualizing high-dimensional data in a 2D space.

# Example output visualization 

![Data-visualisation-using-t-SNE](/images/output123.png)

## Features

- Support for CSV and Excel file formats
- Automatic feature scaling
- Optional data labeling
- Interactive column selection
- Customizable t-SNE parameters

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7+
- pip (Python package manager)

## Installation

1. Install required dependencies:
```bash
pip install numpy pandas matplotlib scikit-learn
```

## Usage

### Preparing Your Dataset

Your dataset should be in CSV or Excel format:

#### Example Without Labels
```csv
feature1,feature2,feature3
0.1,0.2,0.3
0.4,0.5,0.6
0.7,0.8,0.9
```

#### Example With Labels
```csv
feature1,feature2,feature3,class
0.1,0.2,0.3,A
0.4,0.5,0.6,B
0.7,0.8,0.9,A
```

The script will prompt you to:
1. Enter the path to your dataset
2. Select feature columns
3. Optionally select a label column for visualization

### Example Inputs

```
Enter the path to your dataset (CSV/Excel):
```

## Customization

You can modify the script to:
- Change perplexity value
- Adjust visualization parameters
- Add more preprocessing steps

## Troubleshooting

- Ensure all feature columns are numeric
- Check for missing or invalid data
- Verify file paths and permissions

## Example Datasets

Suggested datasets for testing:
- Iris Dataset
- Wine Quality Dataset
- Breast Cancer Dataset

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact

Your Name - @byshukrullo in all social
