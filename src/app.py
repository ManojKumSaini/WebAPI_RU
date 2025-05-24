import streamlit as st
import pandas as pd
import requests

# Set app title
st.title("Space Dashboard")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Who is in Space?", "ISS Location"])

# Fetch data
space_response = requests.get("http://api.open-notify.org/astros.json")
loc_response = requests.get("http://api.open-notify.org/iss-now.json")
space_data = space_response.json()
loc_data = loc_response.json()

# Function to get astronaut info
def get_people_in_space(data):
    messages = []
    for person in data['people']:
        messages.append(f"Astronaut {person['name']} is currently in space.")
    count_message = f"Total {len(data['people'])} people are currently in space."
    return count_message, messages

# Function to get ISS location
def get_location(data):
    lat = float(data['latitude'])
    lon = float(data['longitude'])
    df = pd.DataFrame({
        'lat': [lat],
        'lon': [lon],
        'size': [500],
        'color': [[1, 0, 0, 0.8]] 
    })
    return df

if page == "Who is in Space?":
    st.subheader("Discover who is currently exploring outer space.")
    count_msg, astronaut_msgs = get_people_in_space(space_data)
    st.subheader(count_msg)
    st.write("Here is the list of astronauts:")
    for msg in astronaut_msgs:
        st.markdown(f"- {msg}")
        st.divider()

elif page == "ISS Location":
    st.subheader("Live location of the International Space Station (ISS)")
    location_data = get_location(loc_data['iss_position'])
    st.map(location_data, latitude="lat", longitude="lon", size="size", color="color")
    st.caption("The marker shows where the ISS is currently located.")