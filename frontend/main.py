# # Creating two tabs on the screen
# tab1, tab2 = st.tabs(["🎯 Get Club Recommendation", "📝 Log a New Shot"])

# # Club Recommendation Tab
# with tab1:
#     st.header("Ask the Caddie")
    


import streamlit as st

st.set_page_config(page_title="Caddie & Stats Platform", page_icon="🏌️‍♂️", layout="wide")

st.title("⛳ My Golf Caddie & Stats")
st.write("### Select a tool from the sidebar to get started:")

st.info("🎯 **Get Club Recommendation:** Get a club recommendation based on distance.")
st.info("📝 **Track a Shot:** Log your practice shots to improve your data.")