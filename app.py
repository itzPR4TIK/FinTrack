import streamlit as st
from utils.database import init_db, add_transaction, get_transactions, get_summary, delete_transaction
from utils.charts import spending_by_category, monthly_trends, income_vs_expenses

st.set_page_config(
    page_title="FinTrack",
    page_icon="💰",
    layout="wide",
)

init_db()

# Header
st.markdown("## FinTrack — Personal Finance Tracker")
st.markdown("---")

# Metrics row
summary = get_summary()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Balance", value=f"₹{summary['balance']:,.2f}")

with col2:
    st.metric(label="Total Income", value=f"₹{summary['income']:,.2f}")

with col3:
    st.metric(label="Total Expenses", value=f"₹{summary['expenses']:,.2f}")

st.markdown("---")

# Sidebar form
st.sidebar.markdown("## Add Transaction")
st.sidebar.markdown("---")

with st.sidebar.form("transaction_form"):
    trans_type = st.selectbox(
        "Type",
        ["expense", "income"]
    )

    category = st.selectbox(
        "Category",
        ["Food", "Transport", "Shopping", "Bills", "Health",
         "Entertainment", "Education", "Salary", "Freelance", "Other"]
    )

    amount = st.number_input(
        "Amount (₹)",
        min_value=0.0,
        step=0.5,
    )

    description = st.text_input("Description (optional)")

    date = st.date_input("Date")

    submitted = st.form_submit_button("+ Add Transaction", use_container_width=True)

if submitted:
    if amount > 0:
        add_transaction(
            trans_type,
            category,
            float(amount),
            description,
            str(date)
        )
        st.sidebar.success("Transaction added successfully!")
        st.rerun()
    else:
        st.sidebar.error("Amount must be greater than 0!")
# Charts
df = get_transactions()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Spending by Category")
    fig1 = spending_by_category(df)
    if fig1:
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.info("No expenses yet.")

with col2:
    st.markdown("### Income vs Expenses")
    fig3 = income_vs_expenses(df)
    if fig3:
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("No transactions yet.")

st.markdown("### Monthly Trends")
fig2 = monthly_trends(df)
if fig2:
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("No transactions yet.")

st.markdown("---")
# Transaction history
st.markdown("### Transaction History")

if df.empty:
    st.info("No transactions yet. Add one from the sidebar!")
else:
    for index, row in df.iterrows():
        col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 3, 1])

        with col1:
            if row["type"] == "income":
                st.markdown(f"🟢 **{row['type'].capitalize()}**")
            else:
                st.markdown(f"🔴 **{row['type'].capitalize()}**")

        with col2:
            st.write(row["category"])

        with col3:
            st.write(f"₹{row['amount']:,.2f}")

        with col4:
            st.write(row["description"] if row["description"] else "—")

        with col5:
            if st.button("Delete", key=f"del_{row['id']}"):
                delete_transaction(row["id"])
                st.rerun()

        st.markdown("---")