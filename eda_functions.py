import pandas as pd
import plotly.express as px
from pandas.api.types import is_numeric_dtype

def get_data_summary(df):
  summary = {
      "Shape": df.shape,
      "Columns": df.columns.tolist(),
      "Data Types": df.dtypes.to_dict(),
      "Missing Values": df.isnull().sum().to_dict(),
      "Unique Values": df.nunique().to_dict()
  }
  return summary

def get_column_details(df, column_name):
    """Calculates key metrics for a single column."""
    if column_name not in df.columns:
        return None
    
    missing_values = df[column_name].isnull().sum()
    missing_percent = (missing_values / len(df)) * 100
    
    details = {
        "Unique Values Count": df[column_name].nunique(),
        "Missing Values Count": missing_values,
        "Missing Values %": f"{missing_percent:.2f}%"
    }
    return details

def create_univariate_plot(df, column_name, plot_type="Histogram"):
    
    # For categorical columns, always use a bar chart
    if not pd.api.types.is_numeric_dtype(df[column_name]):
        counts = df[column_name].value_counts()
        fig = px.bar(x=counts.index, y=counts.values, title=f"Count of {column_name}",
                     labels={'x': column_name, 'y': 'Count'})
        return fig

    # For numeric columns, use the selected plot type
    if plot_type == "Histogram":
        # The 'histogram' in Plotly Express can show a Kernel Density Estimate (KDE) curve
        fig = px.histogram(df, x=column_name, marginal="box",
                           title=f"Histogram (with KDE) and Box Plot for {column_name}")
    elif plot_type == "Box Plot":
        fig = px.box(df, y=column_name, title=f"Box Plot for {column_name}")
    elif plot_type == "Violin Plot":
        # A violin plot is excellent for showing distribution and outliers
        fig = px.violin(df, y=column_name, box=True, points="all",
                        title=f"Violin Plot for {column_name} (Shows Distribution and Outliers)")
    else:
        # Default to histogram if plot_type is unknown
        fig = px.histogram(df, x=column_name, marginal="box",
                           title=f"Distribution of {column_name}")
                           
    return fig

def create_correlation_heatmap(df, method='pearson'):
  numeric_df = df.select_dtypes(include=['number'])
  corr_matrix = numeric_df.corr(method=method)
  fig = px.imshow(
    corr_matrix,
    aspect="auto",
    x=corr_matrix.columns,
    y=corr_matrix.columns,
    labels=dict(x="Variables", y="Variables", color="Correlation"),
    title="Correlation Heatmap",
    text_auto=".2f"
  )
  fig.update_layout(
      xaxis=dict(tickfont=dict(size=8)), 
      yaxis=dict(tickfont=dict(size=8)) 
  )
  return fig
    
def display_column_description(df, column_name):
  if column_name in df.columns:
    return df[column_name].describe()
  else:
    print(f"Warning: Column '{column_name}' not found in the DataFrame.")
    return None
