#! D:\PersonalProjs\Govtech AI Course\07 streamlit\customer_svc\Scripts\python.exe
# Set up and run this Streamlit App
import streamlit as st
from logics import customer_query_handler

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Streamlit App")

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

def process_user_message(user_input):
        delimiter = "```"

        # Process 1: If Courses are found, look them up
        category_n_course_name = customer_query_handler.CustomerQueryHandler.identify_category_and_courses(user_input)
        print("category_n_course_name : ", category_n_course_name)

        # Process 2: Get the Course Details
        course_details = customer_query_handler.CustomerQueryHandler.get_course_details(category_n_course_name)

        # Process 3: Generate Response based on Course Details
        reply = customer_query_handler.CustomerQueryHandler.generate_response_based_on_course_details(user_input, course_details)

        # Process 4: Append the response to the list of all messages
        return reply

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    response = process_user_message(user_prompt)
    st.write(response)
    print(f"User Input is {user_prompt}")