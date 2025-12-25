import streamlit as st
import pandas as pd


# CONFIG

st.set_page_config(
    page_title="Kosting Gym Outfit",
    page_icon="💪",
    layout="wide"
)

# =====================================
# SESSION STATE

if "page" not in st.session_state:
    st.session_state.page = "home"
if "cart" not in st.session_state:
    st.session_state.cart = []


# UTIL

def rupiah(x):
    return f"Rp {x:,}".replace(",", ".")

def set_page(p):
    st.session_state.page = p

def add_to_cart(product, size, qty):
    for item in st.session_state.cart:
        if item["Produk"] == product["name"] and item["Ukuran"] == size:
            item["Qty"] += qty
            item["Subtotal"] += product["price"] * qty
            return

    st.session_state.cart.append({
        "Produk": product["name"],
        "Kategori": product["gender"],
        "Ukuran": size,
        "Harga": product["price"],
        "Qty": qty,
        "Subtotal": product["price"] * qty
    })


# DATA PRODUK (20 PRODUK)

PRODUCTS = [
    # ========= WANITA (10) =========
    {"name": "Sports Bra PowerFit", "price": 179000, "gender": "Wanita", "image": "https://m.media-amazon.com/images/I/718agTsvtyL._AC_UY1100_.jpg"},
    {"name": "Sports Bra Seamless", "price": 189000, "gender": "Wanita", "image": "https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full//95/MTA-90661432/sports_sport-bra-wanita-model-push-up-seamless-untuk-olahraga-yoga-gym-f_full01.jpg"},
    {"name": "Legging High Waist Pro", "price": 229000, "gender": "Wanita", "image": "https://down-id.img.susercontent.com/file/id-11134207-7r98s-lwy31jgoy1h9dc"},
    {"name": "Legging Compression", "price": 239000, "gender": "Wanita", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRni2Np5m3GThHnNvNfSsKbatCIN0aeDvY0vw&s"},
    {"name": "Crop Top Gym", "price": 159000, "gender": "Wanita", "image": "https://image.made-in-china.com/202f0j00VifbgNlKAdot/Womens-Yoga-Workout-Crop-Top-Gym-Fitness-Vest-Yoga-Sports-Bra-Padded-Crop-Women-Cropped-Tank-Top.webp"},
    {"name": "Tank Top Women", "price": 149000, "gender": "Wanita", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnL8Pc5F76dnmTWT1UNqPKG_deH8VHyy-PdQ&s"},
    {"name": "Jaket Gym Ladies", "price": 269000, "gender": "Wanita", "image": "https://down-id.img.susercontent.com/file/id-11134207-7r98o-lkry47dz7ci2be"},
    {"name": "Short Pants Women", "price": 169000, "gender": "Wanita", "image": "https://m.media-amazon.com/images/I/41RQAuT8EEL._AC_.jpg"},
    {"name": "Yoga Pants Premium", "price": 249000, "gender": "Wanita", "image": "https://hiaeverywear.com/cdn/shop/files/Premiumleggingbisaseries_3_5adab89c-0125-428b-a364-bf3ce676534c_800x.png?v=1702289980"},
    {"name": "Set Gym Wanita", "price": 329000, "gender": "Wanita", "image": "https://down-id.img.susercontent.com/file/0431ad3a34d827834726bdec8e63806a"},

    # ========= PRIA (10) =========
    {"name": "T-Shirt Dry Fit Pro", "price": 169000, "gender": "Pria", "image": "https://img.ncrsport.com/img/storage/large/DD1993-010-1.jpg"},
    {"name": "T-Shirt Training", "price": 159000, "gender": "Pria", "image": "https://www.atalon.id/cdn/shop/files/Running-TS-Catalog_50b8e44c-fd24-491c-af31-6d948836cd83.jpg?v=1686287185&width=1024"},
    {"name": "Tank Top Muscle", "price": 149000, "gender": "Pria", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXmwEYulY8Loc56fUswNyw-VfugjbyTxvZYg&s"},
    {"name": "Celana Pendek Training", "price": 189000, "gender": "Pria", "image": "https://down-id.img.susercontent.com/file/e2b21319b64ea1c4bd75de98113ea640"},
    {"name": "Jogger Gym Men", "price": 239000, "gender": "Pria", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsxoCGc9qWCyB4wsLyjk5VoydWTjBwmCtR7Q&s"},
    {"name": "Hoodie Gym Men", "price": 289000, "gender": "Pria", "image": "https://gymgeneration.ch/cdn/shop/products/gym-hoodie-off-white-essential-gym-generation-model-front.jpg?v=1736345860&width=1946"},
    {"name": "Compression Shirt", "price": 199000, "gender": "Pria", "image": "https://athflex.com/cdn/shop/files/Hustle-Highneck-compression.jpg?v=1748339340"},
    {"name": "Compression Pants", "price": 219000, "gender": "Pria", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmXXgpgNoQkyQyD_ry9m5VT2mj77i75RVrwg&s"},
    {"name": "Jacket Windbreaker", "price": 279000, "gender": "Pria", "image": "https://www.atalon.id/cdn/shop/files/DEN00116.jpg?v=1725616675&width=2324"},
    {"name": "Set Gym Pria", "price": 349000, "gender": "Pria", "image": "https://down-id.img.susercontent.com/file/f1c503d0e924130f01710ba4a1e5f750"},
]

SIZE_MAP = {
    "Wanita": ["S", "M", "L", "XL"],
    "Pria": ["M", "L", "XL", "XXL"]
}


# PAGE: HOME
def home_page():
    st.markdown("<h1 style='text-align:center'>Kosting Gym Outfit</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center'>Premium Gym Wear for Men & Women</h4>", unsafe_allow_html=True)
    st.divider()
    st.image("https://images.unsplash.com/photo-1554284126-aa88f22d8b74", width=11000)
    st.button("🛍 Mulai Belanja", on_click=set_page, args=("products",))


# PAGE: PRODUCTS

def products_page():
    st.header("🛍 Katalog Produk")
    filter_gender = st.selectbox("Filter Produk", ["Semua", "Wanita", "Pria"])

    cols = st.columns(4)
    i = 0

    for product in PRODUCTS:
        if filter_gender != "Semua" and product["gender"] != filter_gender:
            continue

        with cols[i % 4]:
            st.image(product["image"], width=150)
            st.subheader(product["name"])
            st.caption(product["gender"])
            st.write(rupiah(product["price"]))

            size = st.selectbox("Ukuran", SIZE_MAP[product["gender"]], key=f"s_{product['name']}")
            qty = st.number_input("Jumlah", 1, 10, 1, key=f"q_{product['name']}")

            if st.button("🛒 Tambah", key=f"b_{product['name']}"):
                add_to_cart(product, size, qty)
                st.success("Ditambahkan")

        i += 1


# PAGE: CART

def cart_page():
    st.header("🛒 Keranjang")
    if not st.session_state.cart:
        st.info("Keranjang kosong")
        return

    df = pd.DataFrame(st.session_state.cart)
    st.dataframe(df, hide_index=True)
    total = df["Subtotal"].sum()
    st.subheader("Total: " + rupiah(total))

    if st.button("🧾 Lanjut ke Rincian"):
        set_page("summary")

# PAGE: SUMMARY

def summary_page():
    st.header("🧾 Rincian Pemesanan")
    st.dataframe(pd.DataFrame(st.session_state.cart), hide_index=True)
    total = sum(i["Subtotal"] for i in st.session_state.cart)
    st.subheader("Total Bayar: " + rupiah(total))
    st.success("Pesanan berhasil dibuat 🎉")
    st.session_state.cart = []

 
# SIDEBAR

with st.sidebar:
    st.markdown("## Kosting Gym Outfit")
    st.button("🏠 Beranda", on_click=set_page, args=("home",))
    st.button("🛍 Produk", on_click=set_page, args=("products",))
    st.button(f"🛒 Keranjang ({len(st.session_state.cart)})", on_click=set_page, args=("cart",))
    st.button("🧾 Rincian", on_click=set_page, args=("summary",))


# ROUTING

if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "products":
    products_page()
elif st.session_state.page == "cart":
    cart_page()
elif st.session_state.page == "summary":
    summary_page()
