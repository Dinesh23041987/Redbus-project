import streamlit as st
import pandas as pd

# Load the data
chandigarh_data = pd.read_csv("Chandigarh_Data.csv")
westbengal_data = pd.read_csv("WestBengal_Data.csv")
andra_data = pd.read_csv("Andra_Data.csv")
punjab_data = pd.read_csv("Punjab_Data.csv")
kaac_data = pd.read_csv("KAAC_Data.csv")
southbengal_data = pd.read_csv("Southbengal_Data.csv")
telangana_data = pd.read_csv("Telangana_Data.csv")  # Load Telangana data
bihar_data = pd.read_csv("Bihar_Data.csv")          # Load Bihar data
jammu_data = pd.read_csv("Jammu_Data.csv")          # Load Jammu data
kerala_data = pd.read_csv("Kerala_Data.csv")        # Load Kerala data

# Combine the data into a single DataFrame
all_data = pd.concat([chandigarh_data, westbengal_data, andra_data, punjab_data, kaac_data, southbengal_data, telangana_data, bihar_data, jammu_data, kerala_data])

# Sidebar filters
st.sidebar.title('Filter Options')
route = st.sidebar.selectbox('Select Route', all_data['route_name'].unique())
bus_type = st.sidebar.selectbox('Select Bus Type', all_data['bustype'].unique())
star_rating = st.sidebar.slider('Select Star Rating', 0, 5, (0, 5))

# Filter data based on selections
filtered_data = all_data[
    (all_data['route_name'] == route) &
    (all_data['bustype'] == bus_type) &
    (all_data['star_rating'] >= star_rating[0]) &
    (all_data['star_rating'] <= star_rating[1])
]

# Display the filtered data
st.title('Bus Timings Data')
st.subheader('Filtered Bus Data')
st.dataframe(filtered_data)

# Display bus timings details
if not filtered_data.empty:
    st.subheader('Bus Timings')
    bus_name = filtered_data.iloc[0]['busname']
    departure_time = filtered_data.iloc[0]['departing_time']
    arrival_time = filtered_data.iloc[0]['reaching_time']
    
    st.markdown(f"**Bus Name:** {bus_name}")
    st.markdown(f"**Departure Time:** {departure_time}")
    st.markdown(f"**Arrival Time:** {arrival_time}")
else:
    st.write("No data available for the selected filters.")
