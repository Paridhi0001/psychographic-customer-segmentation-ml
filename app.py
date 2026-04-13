import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt


# Page config
st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")


# Load model
model = pickle.load(open('kmeans_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))


# Title
st.markdown("<h1 style='text-align:center;'>📊 Customer Segmentation & Analysis</h1>", unsafe_allow_html=True)
st.markdown("---")


# Layout: 3 columns
col1, col2, col3 = st.columns([1, 2, 1])


# ---------------- LEFT PANEL (INPUTS) ----------------
with col1:
   st.subheader("📥 Customer Input")


   recency = st.slider("Recency (days)", 0, 365, 30)
   frequency = st.slider("Frequency", 0, 50, 5)
   monetary = st.slider("Monetary (₹)", 0, 100000, 5000)


   predict = st.button("🚀 Predict", use_container_width=True)


# ---------------- CENTER PANEL (GRAPH + RESULT) ----------------
with col2:
   st.subheader("📈 Customer Behavior Graph")


   # Dummy graph (based on inputs)
   days = [10, 20, 30]
   values = [frequency*2, frequency*3, frequency*4]


   fig, ax = plt.subplots()
   ax.plot(days, values, marker='o')
   ax.set_xlabel("Time")
   ax.set_ylabel("Engagement Level")
   ax.set_title("Customer Activity Trend")


   st.pyplot(fig)


   if predict:


       input_data = np.array([[recency, frequency, monetary]])
       input_data = np.log1p(input_data)
       input_scaled = scaler.transform(input_data)


       cluster = int(model.predict(input_scaled)[0])


       def get_segment(cluster):
           mapping = {
               0: "Luxury Seeker 💎",
               1: "Budget Buyer 🛒",
               2: "Impulse Shopper ⚡"
           }
           return mapping.get(cluster, "Regular Customer 👤")


       segment = get_segment(cluster)


       st.markdown("### 🎯 Prediction Result")
       st.success(f"{segment}")


       st.metric("Cluster ID", cluster)


# ---------------- RIGHT PANEL (EXPLANATION) ----------------
with col3:
   st.subheader("📄 Insights & Explanation")


   st.write("""
   This dashboard analyzes customer behavior using:

   • **Recency** – How recently the customer purchased
   • **Frequency** – How often they purchase
   • **Monetary** – How much they spend

   Based on these, customers are grouped using **K-Means clustering**.
   """)


   if predict:
       st.markdown("### 🧠 Interpretation")


       st.write(f"""
       - Recency: {recency} days
       - Frequency: {frequency} purchases
       - Monetary: ₹{monetary}


       This customer is categorized as **{segment}**.
       """)


       st.markdown("### 💡 Business Strategy")


       if "Luxury" in segment:
           st.success("Focus on premium services and exclusive deals.")
       elif "Budget" in segment:
           st.success("Provide discounts and value offers.")
       elif "Impulse" in segment:
           st.success("Use urgency-based marketing like flash sales.")
       else:
           st.success("Maintain engagement with regular communication.")


# ---------------- BOTTOM SECTION ----------------
st.markdown("---")
st.subheader("📊 Summary Dashboard")


colA, colB, colC = st.columns(3)


colA.metric("Recency", f"{recency} days")
colB.metric("Frequency", frequency)
colC.metric("Monetary", f"₹{monetary}")


st.markdown("""
---
💡 **About Project:**
This system uses machine learning to segment customers based on behavioral patterns, helping businesses make smarter marketing decisions.
""")
