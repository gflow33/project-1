import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("Goupes")
content = """
At Goupes, we are dedicated to turning your digital dreams into reality. As a leading software company, we specialize in creating 
innovative and cutting-edge solutions that empower businesses and individuals to thrive in the ever-evolving digital landscape.
"""
st.write(content)
st.subheader("Our team")

column1, empty1, column2, empty2, column3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = pandas.read_csv('data2.csv')
# Add content to first column
with column1:
    # iterate over rows 1 to 4
    for index, row in df[:4].iterrows():
        # Add members first and last name
        st.subheader(row['first name'].title() + " " + row['last name'].title())
        # Add member's image
        st.image('images2/' + row['image'])
        # Add member's role in the company
        st.write(row['role'])

with column2:
     # iterate over rows 4 to 7
    for index, row in df[4:8].iterrows():
        # Add members first and last name
        st.subheader(row['first name'].title() + " " + row['last name'].title())
        # Add member's image
        st.image('images2/' + row['image'])
        # Add member's role in the company
        st.write(row['role'])

with column3:
    # iterate over rows 8 to 12
    for index, row in df[8:].iterrows():
        # Add members first and last name
        st.subheader(row['first name'].title() + " " + row['last name'].title())
        # Add member's image
        st.image('images2/' + row['image'])
        # Add member's role in the company
        st.write(row['role'])