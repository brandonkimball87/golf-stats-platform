import streamlit as st
import requests

# Backend API URL
FASTAPI_URL = "http://127.0.0.1:8000"

#st.set_page_config(page_title="🎯 Get Club Recommendation", page_icon="🏌️‍♂️", layout = 'wide')
st.title("🎯 Club Recommendation")


distance_input = st.number_input(
    label="Enter Rangefinder Distance (yards):", 
    # min_value=-10,
    #   max_value=800,
    value=None,
    step=1,
    help="Type the yardage from your rangefinder here. Only accpets a whole number from 1 to 300",
    placeholder="example: 150"
    )
    
if st.button("Recommend a Club", type="primary"):
    # Make a GET request to your FastAPI router
    response = requests.get(f"{FASTAPI_URL}/caddie/rec_avg", params={"rangefinder_distance": distance_input})
    
    if response.status_code == 200:
        data = response.json()
        st.success(data["message"])
    elif response.status_code == 400:
        st.warning(response.json()["detail"])
    elif response.status_code == 404:
        st.info(response.json()["detail"])
    else:
        st.error("Something went wrong on the server.")
