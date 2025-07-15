import streamlit as st
import langchain_helper
st.title("Restaurant Name generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian", "Italian", "Mexican","Chinese"))




if cuisine:
      response= langchain_helper.generate_restaurant_name_and_items(cuisine)
      st.header(response['restaurant_name']).strip()
      Menu_items= response['Menu_Item'].split(",")
      st.write("**Menu Items**")
      for item in Menu_items:
        st.write("-", item)