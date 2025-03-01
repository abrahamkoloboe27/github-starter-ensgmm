import pandas as pd
import plotly.express as px
def get_data(path):
    df = pd.read_csv(path)
    return df

def plot_ventes(df):
    fig = px.bar(
        df,
        x="Date",
        y="Total Ventes",
        title = "Évolution des ventes au cours du temps"
    )
    fig.show()
    