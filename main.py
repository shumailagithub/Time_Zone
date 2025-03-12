# import required Libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of avaliable timeZones
TIME_ZONE = [
    "UTC",
    "Asia/Karachi",
    "America/New_york",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# App title
st.title("⏱️ Time Zone App")

# Craete a multiSelect widget for selecting timezones 
selected_timezone = st.multiselect("Select Timezones", TIME_ZONE, default=["UTC", "Asia/Karachi"])

# Display the selected timezones
st.subheader("Selected Timezones")
for tz in selected_timezone:
    
    # Get and format current time for each selected timezone with AM/PM
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    
    # Display the current time for each selected timezone
    st.write(f"**{tz}**: {current_time}")
    
    # Create a subheader for converting time between timezones
st.subheader("Convert Time Between Timezones")

# Create a time input widget for the current time
current_time = st.time_input("Current Time", value=datetime.now().time())

# create a selecbox for selecting the timezone to convert from
from_tz = st.selectbox("From Timezone", TIME_ZONE, index=0)

# create a selectbox for selectting the timezone to conver to
to_tz = st.selectbox("To Timezone", TIME_ZONE, index=1)
 
 # Create a button to trigger the time conversion
if st.button("Convert Time"):
    
    # Combine th current time with the selected timezone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    
    # Convert the time to the selected timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    
    # Display the converted time
    st.success(f"Convered Time in {to_tz}: {converted_time}")








#-------------INFO About time zone App ---------------------------

# -------Details of Time Zone App-----------
# Time Zone :  A simple Time Zone App using python, uv, and Streamlit

#A time is a region where people use the same time
# Different places have different time zones
# It is based on the Earth's rotation

#--------------UTC---Stands for----------------
#UTC (Coordinated Unversal Time)   is the world's standard time.


#--------------Diffrent Countries tine Diffrences------------------
# UTC + 0   ->   London
#UTC + 5    ->   Pakistan
#UTC - 5    ->   New York