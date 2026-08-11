### CREATING A STREAMLIT FILE
### "streamlit" is an external Python MODULE.
### "as st" gives the imported module the shorter alias "st".
### "plotly.express" is a MODULE inside the Plotly package.
import streamlit as st
import pandas as pd
# import plotly.express as px

### These are all st functions that display text on the Streamlit page.
st.title("BAN 6005 Taxi Dashboard")
st.header("San Francisco Taxi Trip Data")
st.subheader("First Streamlit Demo")

### st.write() is a general-purpose Streamlit FUNCTION.
### Unlike print(), st.write() sends the output to the Streamlit page.
st.write("We will turn a pandas DataFrame into an interactive dashboard.")


### ============================================================
### IMPORTING A DATA FILE
### ============================================================

### pd.read_excel() is a FUNCTION provided by the pandas module. 
df = pd.read_excel("waymo_taxi_sample (2).xlsx")
st.subheader("Raw Taxi Data")

### st.dataframe() is a Streamlit FUNCTION that displays a pandas
### width="stretch" tells Streamlit to use the available horizontal space. 
st.dataframe(df, width="stretch")
st.write("Number of rows:", len(df))


### df.columns is an ATTRIBUTE of the DataFrame object. 
#st.write("Number of columns:", len(df.columns))

### pd.to_datetime() is a pandas FUNCTION.
### It receives the Series as an argument and converts its values
### into pandas datetime values.
#df["start_time_local"] = pd.to_datetime(df["start_time_local"])


### Create three new DataFrame columns 
#df["trip_distance_miles"] = df["trip_distance_meters"] / 1609.34
#df["trip_duration_minutes"] = df["fare_time_milliseconds"] / 60000


### ============================================================
### CREATING DASHBOARD METRICS
### ============================================================

### Display a heading for the dashboard summary section.
#st.subheader("Summary")

### st.columns(4) returns four Streamlit CONTAINER OBJECTS.
#col1, col2, col3, col4 = st.columns(4)

### metric() is a METHOD available on that container object.
#col1.metric("Number of Trips", f"{len(df):,}")
#col2.metric("Average Fare", f"${df['total_fare_amount'].mean():.2f}")
#col3.metric("Average Distance", f"{df['trip_distance_miles'].mean():.2f} miles")
#col4.metric("Average Duration", f"{df['trip_duration_minutes'].mean():.2f} min")


### Display the updated DataFrame after adding the three new columns.
#st.subheader("Raw Taxi Data with Additional Columns")
#st.dataframe(df, width="stretch")


### ============================================================
### SIDEBAR FILTERS
### ============================================================

### st.sidebar refers to Streamlit's sidebar CONTAINER OBJECT.
### header() is a METHOD that places the heading inside the sidebar
#st.sidebar.header("Filters")


### hail_options is a VARIABLE that refers to a list.
#hail_options = sorted(df["hail_type"].dropna().unique())


### st.sidebar.multiselect() creates an interactive multiselect widget
### selected_hail is a variable referring to that returned list.
#selected_hail = st.sidebar.multiselect( "Hail type:", hail_options, default=None)


### st.sidebar.checkbox() creates a checkbox widget.
### A checkbox RETURNS a BOOLEAN value:
#sfo_only = st.sidebar.checkbox("SFO pickups only")
#paratransit_only = st.sidebar.checkbox("Paratransit trips only")


### ============================================================
### APPLYING THE CATEGORY AND CHECKBOX FILTERS
### ============================================================

### This line creates a separate copy of the filtered DataFrame.
#filtered_df = df[df["hail_type"].isin(selected_hail)].copy()


### If sfo_only value is True, Python executes the indented block. Otherwise, it skips the block.
#if sfo_only: 
#    filtered_df = filtered_df[filtered_df["sfo_pickup"] == 1]
### Similarly, if paratransit_only value is True, Python executes the indented block. Otherwise, it skips the block.
#if paratransit_only:
#    filtered_df = filtered_df[filtered_df["paratransit"] == 1]


### ============================================================
### DATE-RANGE FILTER WIDGETS
### ============================================================

### .date extracts only the date portion from each datetime value
#min_date = df["start_time_local"].dt.date.min()
#max_date = df["start_time_local"].dt.date.max()


### st.sidebar.date_input() creates an interactive date widget.
### This first date widget returns the user-selected starting date.
#start_date = st.sidebar.date_input(
#    "Start date:",
#    min_date,
#    min_value=min_date,
#    max_value=max_date
#)
### This second date widget returns the user-selected ending date.
#end_date = st.sidebar.date_input(
#    "End date:",
#    max_date,
#    min_value=min_date,
#    max_value=max_date
#)


### pd.to_datetime() converts the Python date object into a pandas
#start_date = pd.to_datetime(start_date)
#end_date = pd.to_datetime(end_date)


### ============================================================
### APPLYING THE DATE FILTER
### ============================================================

### Calling pd.Timedelta(days=1) creates a Timedelta OBJECT representing a duration of one day.
### So the second condition becomes: filtered_df["start_time_local"] < end_date + one day
#filtered_df = filtered_df[
#    (filtered_df["start_time_local"] >= start_date) &
#    (filtered_df["start_time_local"] < end_date + pd.Timedelta(days=1))
#]


### In case we do not have any matching records
#if len(filtered_df) == 0:
#    st.warning("No trips match the selected filters.")
#    st.stop()

### Display a heading for the filtered table.
#st.subheader("Filtered Trip Records")


#display_columns = [
#    "driver_id",
#    "start_time_local",
#    "hail_type",
#    "sfo_pickup",
#    "paratransit",
#    "total_fare_amount",
#    "tip",
#    "trip_distance_miles",
#    "trip_duration_minutes"
#]

#st.dataframe(
#    filtered_df[display_columns],
#    width="stretch"
#)


### ============================================================
### SCATTER PLOT
### ============================================================

### Display a heading before the scatter plot.
#st.subheader("Distance and Fare")


### px.scatter() is a FUNCTION in the Plotly Express module.
### In the dictionary:
### - each original DataFrame column name is a key
#fig_scatter = px.scatter(
#    filtered_df,
#    x="trip_distance_miles",
#    y="total_fare_amount",
#    color="hail_type",
#    hover_data=["driver_id"],
#    title="Trip Distance vs. Total Fare",
#    labels={
#        "trip_distance_miles": "Trip Distance (miles)",
#        "total_fare_amount": "Total Fare ($)",
#        "hail_type": "Hail Type"
#    }
#)


### Plotly creates the chart object.
### Streamlit displays the chart object.
#st.plotly_chart(fig_scatter, width="stretch")


### ============================================================
### BAR CHART
### ============================================================

### This returns the grouped result (mean)
### reset_index() is a METHOD that converts the grouped result
#avg_fare_df = filtered_df.groupby("hail_type")["total_fare_amount"].mean().reset_index()

# px.bar() is a Plotly Express FUNCTION.
#fig_bar = px.bar(
#    avg_fare_df,
#    x="hail_type",
#    y="total_fare_amount",
#    title="Average Fare by Hail Type",
#    labels={
#        "hail_type": "Hail Type",
#        "total_fare_amount": "Average Total Fare ($)"
#    }
#)


# Display the Plotly Figure object
#st.plotly_chart(fig_bar, width="stretch")


### ============================================================
### LINE PLOT
### ============================================================

### .dt is the datetime accessor.
### .date extracts the date from each datetime value and returns it.
#filtered_df["trip_date"] = filtered_df["start_time_local"].dt.date


### THis line returns a Series object containing the number of trips for each date.
### reset_index(name="trips") returns a DataFrame object with two columns: "trip_date" and "trips".
#daily_trips = (
#    filtered_df
#    .groupby("trip_date")
#    .size()
#    .reset_index(name="trips")
#)


### px.line() is a Plotly Express FUNCTION.
#fig_line = px.line(
#    daily_trips,
#    x="trip_date",
#    y="trips",
#    title="Number of Trips Over Time",
#    labels={
#        "trip_date": "Date",
#        "trips": "Number of Trips"
#    }
#)


#st.plotly_chart(fig_line, width="stretch")


### ============================================================
### PICKUP MAP
### ============================================================

### Select two columns from the filtered DataFrame before creating the map.
#map_df = (filtered_df[["pickup_location_latitude","pickup_location_longitude"]].dropna())


### st.map() is a Streamlit FUNCTION.
#st.map(
#    map_df,
#    latitude="pickup_location_latitude",
#    longitude="pickup_location_longitude"
#)
