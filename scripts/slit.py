import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def main():
    plt.rc('xtick', labelsize=8)
    st.title("EDA")
    st.subheader("1. Share Split Effect")
    st.markdown("We started our EDA with a simple graph time against strike "
            "and encountered an interesting situation when the graph accidentaly "
            "drops at a significant ratio. By diving deep into details we investigated "
            "that it is related to a share split performed by Tesla in observed period")
    
    # Load data from insight_1.csv
    df1 = pd.read_csv("./output/insight_1.csv")

    # Convert x column to datetime format
    df1["x"] = pd.to_datetime(df1["x"], unit="s")

    # Calculate y difference between adjacent rows
    df1["y_diff"] = df1["y"].diff()

    # Find indices where y difference is less than -50
    drop_indices = df1.index[df1["y_diff"] < -200].tolist()

    # Plot line chart for df1 with red regions around significant drops
    fig, ax = plt.subplots()
    ax.plot(df1["x"], df1["y"])
    for index in drop_indices:
        ax.axvspan(
            df1.loc[index - 20, "x"],
            df1.loc[index + 20, "x"],
            alpha=0.2,
            color="red",
        )
    start_date = df1["x"].min().to_pydatetime().replace(day=1)
    end_date = df1["x"].max().to_pydatetime().replace(day=1) + timedelta(
        days=31
    )
    x_ticks = pd.date_range(start=start_date, end=end_date, freq="MS")
    ax.set_xticklabels([x.strftime("%b %Y") for x in x_ticks], rotation=75)
    ax.set_xlabel("Date")
    ax.set_xticks(x_ticks)
    ax.set_ylabel("Value")
    fig.tight_layout()
    st.pyplot(fig)

    # +++++++++++++++++++++++++++++++++++++++++++++++ 

    df2 = pd.read_csv("./output/insight_2.csv")

    # Convert x column to datetime format
    df2["x"] = pd.to_datetime(df2["x"], unit="s")

    st.subheader("2. Similarities in dynamics of features")
    fig, ax = plt.subplots()
    for column in df2.columns[1:]:
        ax.plot(df2["x"], df2[column], label=column)
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.legend()

    # Find x ticks for every month
    start_date = df2["x"].min().to_pydatetime().replace(day=1)
    end_date = df2["x"].max().to_pydatetime().replace(day=1) + timedelta(
        days=31
    )
    #x_ticks = pd.date_range(start=start_date, end=end_date, freq="MS")
    ax.set_xticks(x_ticks)
    ax.set_xticklabels([x.strftime("%b %Y") for x in x_ticks], rotation=75)
    fig.tight_layout()
    st.pyplot(fig)

    # ++++++++++++++++++++++++++++++++++++++

    df3 = pd.read_csv('./output/insight_3.csv')
    
    st.subheader("3. Correlation matrix")
    # compute the correlation matrix
    corr_matrix = df3.corr()

    # create a heatmap using matplotlib
    fig, ax = plt.subplots()
    heatmap = ax.pcolor(corr_matrix, cmap='coolwarm')

    # add a colorbar legend
    cbar = plt.colorbar(heatmap)

    # set the ticks and tick labels for the x-axis and y-axis
    ticks = np.array(range(len(corr_matrix.columns)))
    ax.set_xticks(ticks + 0.5)
    ax.set_yticks(ticks + 0.5)
    ax.set_xticklabels(corr_matrix.columns, rotation=90)
    ax.set_yticklabels(corr_matrix.columns)
    fig.tight_layout()
    # display the heatmap using Streamlit
    st.pyplot(fig)
    # +++++++++++++++++++++++++++
    st.subheader("4. Lifetime periods of the Options")

    df4 = pd.read_csv('./output/insight_4.csv')
    df4 = df4[df4['lifetime_days'] > 0]
    fig, ax = plt.subplots()
    ax.bar(df4['lifetime_days'].astype(np.int32), df4['num_options'].astype(np.int32))
    ax.set_ylabel('Number of Options')
    ax.set_xlabel('Lifetime (days)')
    ax.set_title('Number of Options vs Lifetime')

    fig.tight_layout()
    # Show the plot in Streamlit
    st.pyplot(fig)
    # ++++++++++++++++++++++++++
    
    st.subheader("5. Relation between average strike price of the option and its' lifetime")
    df5 = pd.read_csv('./output/insight_5.csv')
    df5 = df5[df5['lifetime_days'] > 0]
    fig, ax = plt.subplots()
    ax.bar(df5['lifetime_days'].astype(np.int32), df5['avg_strike'].astype(np.int32))
    ax.set_ylabel('Avg. Strike Price')
    ax.set_xlabel('Lifetime (days)')
    ax.set_title('Avg. Strike Price vs Lifetime')

    fig.tight_layout()
    st.pyplot(fig)

    # Show the plot in Streamlit

    st.title("Predictions")

    lr_preds = pd.read_csv("./output/lr_pred.csv")

    st.subheader("Linear Regression")

    # TODO: Explain

    st.dataframe(lr_preds)

    st.subheader("Random Forest")

    # TODO: Explain

    rf_preds = pd.read_csv("./output/rf_pred.csv")
    st.dataframe(rf_preds)

    st.title("Evaluation")

    st.markdown("To evaluate our models we adapted Root Mean Squared "
            "Error (RMSE) metric. Here are results for out models")

    r = open("./output/rmse.txt")
    st.text("".join(r.readlines()[-2:]))


if __name__ == "__main__":
    main()

