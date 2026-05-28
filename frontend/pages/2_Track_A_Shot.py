import streamlit as st
import requests

# Backend API URL
FASTAPI_URL = "http://127.0.0.1:8000"

#st.set_page_config(page_title="📝 Log a New Shot", page_icon="🏌️‍♂️", layout = 'wide')
st.title("📝 Track A Shot")


with st.form("shot_form", clear_on_submit=True):
    club_selected = st.selectbox(
        label="Select Club Used",
        options=['Driver','2-hybrid','3-hybrid', '4-hybrid','5-iron','6-iron','7-iron','8-iron','9-iron','pitching-wedge','gap-wedge'],
        index=None,
        #format_func=lambda x: f"🏌️‍♂️ {x}",
        help="Select the specific club you just used.",
        placeholder="Choose a club...",
        )
    
    accuracy = st.pills(
        label="Select Shot Accuracy:",
        options=['center', 'left', 'right', 'long', 'short'],
        default = None,
        selection_mode="single",
        help="Select which direction the ball went.",
        )

    target_distance = st.number_input(
        label="Enter Rangefinder Distance (yards):", 
        value=None,
        step=1,
        help="Type the yardage from your laser rangefinder here. Only accepts a whole number from 1 to 300",
        placeholder="example: 150"
        )
    
    actual_distance = st.number_input(
        label="Enter The Distance You Just Hit (yards):", 
        value=None,
        step=1,
        help="Type the yardage you just hit the ball. Only accepts a whole number from 1 to 300",
        placeholder="example: 150"
        )


    submitted = st.form_submit_button(
        label="Upload Shot to Database",
        help="Click here to save this shot into your golf database.",
        )
    
    if submitted:
        payload = {"club": club_selected, "accuracy": accuracy, "target_distance": target_distance,  "actual_distance": actual_distance}
        
        # Change this endpoint to whatever your actual upload POST route path is!
        response = requests.post(f"{FASTAPI_URL}/shot_data/upload", json=payload)
        
        if response.status_code in [200, 201]:
            st.success(f"Successfully saved your {actual_distance}-yard {club_selected} shot!")
        else:
            st.error("Failed to upload shot. Check backend logs.")