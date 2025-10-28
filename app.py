import streamlit as st
import pandas as pd
from eda_functions import (
    get_data_summary, 
    create_univariate_plot, 
    create_correlation_heatmap, 
    get_column_details,
    display_column_description
)

st.set_page_config(layout="wide")
st.title("Automated Exploratory Data Analysis")

# 1. File Uploader
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])


if uploaded_file is not None:
    # Updated data loading function to handle both file types
    @st.cache_data
    def load_data(file):
        """Loads data from CSV or Excel file."""
        # To read Excel files, you might need to install the 'openpyxl' library:
        # pip install openpyxl
        try:
            if file.name.endswith('.csv'):
                return pd.read_csv(file)
            else:
                return pd.read_excel(file)
        except Exception as e:
            st.error(f"Error loading file: {e}")
            return None

    df = load_data(uploaded_file)
    
    # Proceed only if the dataframe was loaded successfully
    if df is not None:
        st.success("File uploaded successfully!")

        # --- Sidebar for Options ---
        st.sidebar.header("Analysis Options")

        # --- Main Page Display ---
        st.header("1. Data Overview")
        if st.sidebar.checkbox("Show Data Summary", True):
            st.subheader("Data Summary")
            summary = get_data_summary(df)
            st.json(summary, expanded=False)
            
            st.subheader("Data Preview")
            st.dataframe(df.head())


        st.header("2. Univariate Analysis")
        if st.sidebar.checkbox("Show Univariate Analysis", True):
            # Let user select a column from a dropdown
            selected_column = st.sidebar.selectbox(
                "Select a column for univariate analysis:", df.columns, key="univariate_column"
            )
            
            plot_choice = "Bar Chart"
            # Only show plot type options if the column is numeric
            if pd.api.types.is_numeric_dtype(df[selected_column]):
                plot_choice = st.sidebar.radio(
                    "Select plot type:",
                    ("Histogram", "Box Plot", "Violin Plot"),
                    key="plot_type"
                )

            # Display the plot
            st.subheader(f"{plot_choice} for '{selected_column}'")
            fig_uni = create_univariate_plot(df, selected_column, plot_type=plot_choice)
            st.plotly_chart(fig_uni, use_container_width=True)

            st.subheader(f"Detailed Analysis of '{selected_column}'")
            col1, col2 = st.columns(2)
            with col1:
                st.write("#### Statistical Description")
                description = display_column_description(df, selected_column)
                if description is not None:
                    st.write(description)
            with col2:
                st.write("#### Key Metrics")
                details = get_column_details(df, selected_column)
                if details:
                    st.metric(label="Unique Values", value=details["Unique Values Count"])
                    st.metric(label="Missing Values", value=f"{details['Missing Values Count']} ({details['Missing Values %']})")


        st.header("3. Correlation Analysis")
        if st.sidebar.checkbox("Show Correlation Heatmap", True):
            corr_method = st.sidebar.radio(
                "Select correlation method:", ("Pearson", "Spearman"), key="corr"
            )
            fig_corr = create_correlation_heatmap(df, method=corr_method.lower())
            if fig_corr is not None:
                st.plotly_chart(fig_corr, use_container_width=True)
            else:
                st.warning("Not enough numeric columns in the data to generate a correlation heatmap.")

else:
    st.info("Awaiting for a file to be uploaded.")
