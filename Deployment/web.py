import streamlit as st
import joblib

# Loading the model
model = joblib.load('lr_model.pkl')

# Create input fields for each feature
area = st.text_input('Area', value='7420')
bedrooms = st.slider('Bedrooms', min_value=1, max_value=4)
bathrooms = st.slider('Bathrooms', min_value=1, max_value=4)
stories = st.slider('Stories', min_value=1, max_value=4)
mainroad = st.radio('Mainroad', ["no", "yes"])
guestroom = st.radio('Guestroom', ["no", "yes"])
basement = st.radio('Basement', ["no", "yes"])
hotwaterheating = st.radio('Hotwater Heating', ["no", "yes"])
airconditioning = st.radio('Air Conditioning', ["no", "yes"])
parking = st.slider('Parking', min_value=0, max_value=3)
prefarea = st.radio('Preferred Area', ["no", "yes"])
furnishingstatus = st.radio('Furnishing Status', ["unfurnished", "furnished"])

# Map binary values to 0 and 1
mainroad = 0 if mainroad == "no" else 1
guestroom = 0 if guestroom == "no" else 1
basement = 0 if basement == "no" else 1
hotwaterheating = 0 if hotwaterheating == "no" else 1
airconditioning = 0 if airconditioning == "no" else 1
prefarea = 0 if prefarea == "no" else 1

# Map furnishing status to 0 and 1
furnishingstatus = 0 if furnishingstatus == "unfurnished" else 1

# Make predictions using user inputs
prediction = model.predict([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus]])

st.write(f'Predicted Price: {prediction[0]}')
