import streamlit as st

st.set_page_config(page_title="Spaza Stock App", page_icon="🛒")
st.title("🛒 Spaza Stock App")
st.write("For small shops in Soweto - track stock, sales and low stock.")

# Start with some example stock if empty
if "products" not in st.session_state:
    st.session_state.products = [
        {"name": "Bread", "price": 18.00, "qty": 10},
        {"name": "Milk 1L", "price": 28.00, "qty": 5},
        {"name": "Eggs 6s", "price": 25.00, "qty": 2},
        {"name": "Coke 500ml", "price": 20.00, "qty": 15},
    ]

# Show totals at top
total_value = sum(p["price"] * p["qty"] for p in st.session_state.products)
low_stock = [p for p in st.session_state.products if p["qty"] <= 3]

st.metric("Total Stock Value", f"R {total_value:.2f}")
if low_stock:
    st.warning(f"Low stock! {', '.join([p['name'] for p in low_stock])} - time to restock")
else:
    st.success("Stock levels are good")

st.divider()

# Add new product
st.subheader("Add New Product")
with st.form("add_form"):
    name = st.text_input("Product Name")
    price = st.number_input("Price (R)", min_value=0.0, step=1.0)
    qty = st.number_input("Quantity", min_value=0, step=1)
    submitted = st.form_submit_button("Add Product")
    if submitted and name:
        st.session_state.products.append({"name": name, "price": price, "qty": qty})
        st.success(f"{name} added!")
        st.rerun()

st.divider()

# Show stock list with Sell button
st.subheader("Current Stock")
for i, p in enumerate(st.session_state.products):
    col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
    col1.write(f"**{p['name']}**")
    col2.write(f"R {p['price']:.2f}")
    col3.write(f"Qty: {p['qty']}")
    if col4.button("Sell 1", key=f"sell_{i}"):
        if p["qty"] > 0:
            st.session_state.products[i]["qty"] -= 1
            st.rerun()
        else:
            st.error("Out of stock!")

    if p["qty"] == 0:
        st.write("❌ OUT OF STOCK")

st.divider()
st.write("Built by Lethabo Mphahlele - FNB App Academy Capstone")