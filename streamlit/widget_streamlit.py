import streamlit as st

# create image
st.image("int3.png")

# checkbox 
st.checkbox("login")

# button
st.button("button")

# radio widget
st.radio("pickup your gender",["male","female","other"])

# select box
st.selectbox("select",["ml","cs","it"])

# multiselect box
st.multiselect("multiple selct",["machine learning","computer science","information technology"])

# select slider
st.select_slider("rating",["bad","excilltent","good"])

# # select slider as number
st.slider("enter number",0,100)

# number input
st.number_input("enter input number",0,100)


# text inpput
st.text_input("enter email")

# date input
st.date_input("enter date")

# time input
st.time_input("enter theh time")



# upload file
st.file_uploader("enter the file")


# side bar

# side bar title
st.sidebar.title("welcome")
st.sidebar.text_input("email adress")
st.sidebar.text_input("password")