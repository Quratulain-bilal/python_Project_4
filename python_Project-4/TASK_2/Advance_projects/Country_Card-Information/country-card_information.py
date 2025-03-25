import streamlit as st  # 📌 Streamlit for Web UI
import requests         # 📌 Requests to Fetch API Data

# 🎨 Set Dark Mode Theme
st.set_page_config(page_title="Country Info", layout="centered")
st.markdown("<h1 style='text-align: center;'>🌍 Country Information App</h1>", unsafe_allow_html=True)

# ✏️ User Input for Country Name
country_name = st.text_input("Enter Country Name", "").strip()

if country_name:  # ✅ Check if input is not empty
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:  # ✅ Country Found
        data = response.json()[0]  # First matching country

        # 🎯 Extract Required Details
        flag = data["flags"]["png"]
        name = data["name"]["common"]
        capital = data.get("capital", ["N/A"])[0]  # Some countries may not have capitals
        population = f"{data['population']:,}"  # Format number with commas
        currency = ", ".join(data.get("currencies", {}).keys())
        languages = ", ".join(data.get("languages", {}).values())
        region = data["region"]
        subregion = data.get("subregion", "N/A")
        area = f"{data['area']:,} km²"

        # 📌 Display Data in Card Format
        st.image(flag, width=200)  # Show Flag
        st.markdown(f"### 🌍 {name}")
        st.write(f"🏛 **Capital:** {capital}")
        st.write(f"👥 **Population:** {population}")
        st.write(f"💰 **Currency:** {currency}")
        st.write(f"🗣 **Languages:** {languages}")
        st.write(f"🌍 **Region:** {region}, {subregion}")
        st.write(f"📏 **Area:** {area}")

        # 🌍 Google Maps Button (Bonus Feature)
        maps_url = f"https://www.google.com/maps/search/{name.replace(' ', '+')}"
        st.markdown(f"[📍 View on Google Maps]({maps_url})", unsafe_allow_html=True)

    else:
        st.error("❌ Country Not Found! Try Again.")

# 📝 Footer
st.markdown("<br><hr><p style='text-align:center;'>Made with ❤️ by Quratulain Shah</p>", unsafe_allow_html=True)
