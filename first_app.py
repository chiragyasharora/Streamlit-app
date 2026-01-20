import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, world!")
st.header("This is a header")
st.subheader("This is a subheader")

if st.checkbox("show/hide"):
    st.text("showing the widget")
else:
    st.text("click the checkbox to show the widget")

status = st.radio("select your gender",   ("male","female","other"))

if status == "male":
    st.success("you selected male")

if st.button("click me"):
    st.text("you clicked the button")

square = lambda x: x**2
num = st.number_input("insert a number")


if st.button("compute square"):
    result = square(num)
    st.text(result)