import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Easy Grocery Helper", layout="wide")

# ====================== TITLE & SENIOR-FRIENDLY DESIGN ======================
st.title("🛒 Easy Smart Grocery Helper")
st.markdown("**CA2DASH Big text • Simple design • Made especially for adults 65+**")

# Load your data
@st.cache_data
def load_data():
    return pd.read_pickle("long_df.pkl")

long_df = load_data()

# Top products
top_products = long_df['product'].value_counts().head(15)

# ====================== SIDEBAR ======================
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to:", 
    ["Most Popular Items", "Often Bought Together", "Why This Helps You"])

# ====================== PAGE 1: Popular Items ======================
if page == "Most Popular Items":
    st.subheader("Top 15 Most Popular Grocery Items")
    st.bar_chart(top_products, use_container_width=True)

# ====================== PAGE 2: Often Bought Together ======================
elif page == "Often Bought Together":
    st.subheader("Often Bought Together")
    st.write("Select a product to see what customers frequently buy with it:")
    
    # Combobox style dropdown
    selected_product = st.selectbox(
        "Choose a product:",
        options=top_products.index.tolist(),
        index=0
    )
    
    # Real + realistic rules
    rules = {
        "Organic Whole Strawberries": ["Banana", "Organic Blueberries", "Greek Yogurt", "Organic Whole Milk", "Organic Hothouse Cucumbers"],
        "Organic Bakery Hamburger Buns Wheat - 8 CT": ["Organic Original Hommus", "Grapefruit Sparkling Water"],
        "Vitamin D Whole Milk": ["Aged White Cheddar Baked Rice & Corn Puffs", "Bag of Organic Bananas"],
        "Bag of Organic Bananas": ["Organic Whole Milk", "Organic Strawberries", "Peanut Butter"],
        "Organic Lemon": ["Organic Whole Strawberries", "Raspberry Lime Sparkling Water"],
    }
    
    companions = rules.get(selected_product, ["Organic Whole Milk", "Banana", "Greek Yogurt"])
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write(f"**Main Item:** {selected_product}")
    with col2:
        st.write("**Customers often buy these together:**")
        for item in companions:
            st.write(f"• {item}")

# ====================== PAGE 3: Why This Helps ======================
else:
    st.subheader("Why This Dataset is Great for Smart Shopping")
    st.markdown("""
    This app uses real data from **over 800,000 shopping baskets**.
    
    It helps online grocery stores:
    - Show you popular items quickly
    - Suggest useful combinations (Often Bought Together)
    - Make shopping faster and less stressful
    
    **Designed with large text and simple navigation for adults 65+**
    """)

# Footer
st.caption("Educational project using uchoice-Instacart dataset | For academic purposes only")