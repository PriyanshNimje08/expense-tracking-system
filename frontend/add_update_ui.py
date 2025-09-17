import streamlit as st
from datetime import datetime
import pandas as pd

if "expenses" not in st.session_state:
    st.session_state.expenses = {}


def add_update_tab():
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1))
    date_str = str(selected_date)

    existing_expenses = st.session_state.expenses.get(date_str, [])

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")

        expenses = []
        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input("", value=amount, key=f"amount_{i}")
            with col2:
                category_input = st.selectbox("", options=categories, index=categories.index(category),
                                              key=f"category_{i}")
            with col3:
                notes_input = st.text_input("", value=notes, key=f"notes_{i}")

            expenses.append({'amount': amount_input, 'category': category_input, 'notes': notes_input})

        if st.form_submit_button("Save"):
            filtered = [exp for exp in expenses if exp['amount'] > 0]
            st.session_state.expenses[date_str] = filtered
            st.success("Expenses updated!")

    if st.session_state.expenses.get(date_str):
        st.table(pd.DataFrame(st.session_state.expenses[date_str]))
