import streamlit as st
import requests
import pandas as pd

def show():
    st.title("User Management")
    st.markdown("View and manage platform users.")
    
    headers = {}
    if "access_token" in st.session_state:
        headers["Authorization"] = f"Bearer {st.session_state.access_token}"

    res = requests.get("http://127.0.0.1:8000/admin/users", headers=headers)
    
    if res.status_code == 200:
        users = res.json().get("users", [])
        if users:
            df = pd.DataFrame(users)
            
            # Display the table
            st.dataframe(df[["id", "name", "email", "role"]], use_container_width=True)
            
            st.divider()
            st.subheader("Delete User")
            
            # Use string input since MongoDB ObjectIds are hashes
            user_id = st.text_input("Enter User ID to delete")
            
            if st.button("Delete User"):
                if user_id.strip():
                    del_res = requests.delete(f"http://127.0.0.1:8000/admin/users/{user_id}", headers=headers)
                    if del_res.status_code == 200:
                        st.success(f"User {user_id} deleted successfully.")
                        st.rerun()
                    else:
                        st.error(f"Failed to delete user: {del_res.text}")
                else:
                    st.warning("Please enter a User ID.")
                    
        else:
            st.info("No users registered.")
    else:
        st.error(f"Failed to load users: {res.text}")
