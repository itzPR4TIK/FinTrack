import plotly.express as px
import pandas as pd
def spending_by_category(df):
    expenses = df[df["type"] == "expense"]
    
    if expenses.empty:
        return None
    grouped = expenses.groupby("category")["amount"].sum().reset_index()
    
    fig = px.pie(
        grouped,
        names="category",
        values="amount",
        title="Sepending by Category",
        hole=0.4,
    ) 
    fig.update_traces(textposition= "inside", textinfo="percent+label")
    fig.update_layout(showlegend=True)
    return fig
def monthly_trends(df):
    if df.empty:
        return None
    
    df = df.copy()
    df["month"] = df["date"].str[:7]
    
    monthly = df.groupby(["month", "type"])["amount"].sum().reset_index()
    
    fig = px.line(
        monthly,
        x="month",
        y="amount",
        color="type",
        title="Monthly Income vs Expenses",
        markers=True,
        color_discrete_map={"income": "#22c55e", "expense": "#ef4444"}
    )
    
    fig.update_layout(xaxis_title="Month", yaxis_title="Amount (₹)")
    
    return fig
def income_vs_expenses(df):
    if df.empty:
        return None
    
    summary = df.groupby("type")["amount"].sum().reset_index()
    
    fig = px.bar(
        summary,
        x="type",
        y="amount",
        title="Income vs Expenses",
        color="type",
        color_discrete_map={"income": "#22c55e", "expense": "#ef4444"},
        text="amount",
    )
    
    fig.update_traces(texttemplate="%{text:,.0f}", textposition="outside")
    fig.update_layout(showlegend=False, yaxis_title="Amount (₹)", xaxis_title="")
    
    return fig