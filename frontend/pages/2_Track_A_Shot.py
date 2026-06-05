import streamlit as st
import requests

# Backend API URL
FASTAPI_URL = "http://127.0.0.1:8000"


@st.cache_data(ttl=600) # Caches results for 10 minutes
def get_unique_users(table_name):
    try:
        params = {'table_name':table_name}
        response = requests.get(f"{FASTAPI_URL}/shot_data/users", params=params)
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        st.error("Could not fetch users from database: {e}")
        return []


users_list = get_unique_users(table_name = 'shots')




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
    
    user_selection = st.pills(
        label="Select user already established in database:",
        options= users_list,
        default = None,
        selection_mode="single",
        help="Select who just hit the ball. If this is a new user and the name is not listed here, type your name below",
        )

    custom_user = st.text_input(label = 'Or type the name of the new user here...', placeholder = 'new user...')

    submitted = st.form_submit_button(
        label="Upload Shot to Database",
        help="Click here to save this shot into your golf database.",
        )
    
    if submitted:

        final_user = custom_user if user_selection is None else user_selection
        if not final_user:
            st.error("Please select or enter a user.")

        payload = {
            "club": club_selected,
            "accuracy": accuracy,
            "target_distance": target_distance, 
            "actual_distance": actual_distance,
            "user": final_user}
        
        # Change this endpoint to whatever your actual upload POST route path is!
        response = requests.post(f"{FASTAPI_URL}/shot_data/upload", json=payload)
        
        if response.status_code in [200, 201]:
            st.success(f"{final_user}, successfully saved your {actual_distance}-yard {club_selected} shot!")
        else:
            st.error("Failed to upload shot. Check backend logs.")



if st.button("🔄 Refresh User List"):
    st.cache_data.clear() 
    st.rerun() 
