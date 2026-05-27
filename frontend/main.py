import streamlit as st
import requests

# 1. Setup the Backend API URL
FASTAPI_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Caddie & Stats Platform", page_icon="🏌️‍♂️")
st.title("⛳ My Golf Caddie & Stats")

# Create two clean visual tabs on the screen
tab1, tab2 = st.tabs(["🎯 Get Club Recommendation", "📝 Log a New Shot"])

# --- TAB 1: CLUB RECOMMENDATION ---
with tab1:
    st.header("Ask the Caddie")
    
    # Simple integer input box
    distance_input = st.number_input(
        "Enter Rangefinder Distance (yards):", 
        min_value=-10, max_value=800, value=150, step=1
    )
    
    if st.button("Recommend a Club", type="primary"):
        # Make a GET request to your FastAPI router
        response = requests.get(f"{FASTAPI_URL}/caddie/rec_avg", params={"rangefinder_distance": distance_input})
        
        if response.status_code == 200:
            data = response.json()
            st.success(data["message"])  # Beautiful green success alert
        elif response.status_code == 400:
            st.warning(response.json()["detail"])  # Yellow validation warning
        elif response.status_code == 404:
            st.info(response.json()["detail"])  # Blue informational alert
        else:
            st.error("Something went wrong on the server.")

# --- TAB 2: LOG A SHOT ---
with tab2:
    st.header("Track a Shot")
    
    # Form layout for input fields
    with st.form("shot_form", clear_on_submit=True):
        club_selected = st.selectbox("Select Club Used:", ['Driver','2-hybrid','3-hybrid', '4-hybrid','5-iron','6-iron','7-iron','8-iron','9-iron','pitching-wedge','gap-wedge'])
        shot_dist = st.number_input("Actual Shot Distance (yards):", min_value=1, max_value=400, value=150)

        submitted = st.form_submit_button("Upload Shot to Database")
        
        if submitted:
            # Prepare data payload for your upload function route
            payload = {"club": club_selected, "actual_distance": shot_dist}
            
            # Change this endpoint to whatever your actual upload POST route path is!
            response = requests.post(f"{FASTAPI_URL}/shots/upload", json=payload)
            
            if response.status_code in [200, 201]:
                st.success(f"Successfully saved your {shot_dist}-yard {club_selected} shot!")
            else:
                st.error("Failed to upload shot. Check backend logs.")