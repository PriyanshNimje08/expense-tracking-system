import streamlit as st
import pandas as pd

def analytics_tab():
    st.subheader("Analytics")
    if "expenses" in st.session_state and st.session_state.expenses:
        all_data = []
        for date, exp_list in st.session_state.expenses.items():
            for exp in exp_list:
                all_data.append({"date": date, **exp})
        df = pd.DataFrame(all_data)
        st.write("Total Expenses:", df['amount'].sum())
        st.bar_chart(df[['date','amount']].set_index('date'))
    else:
        st.info("No expenses added yet!")
