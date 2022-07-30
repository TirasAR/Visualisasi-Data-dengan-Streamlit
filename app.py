from turtle import title
from matplotlib.pyplot import axis
import pandas as pd
import streamlit as st
import plotly.express as px 
import plotly.figure_factory as ff

st.set_page_config(page_title = "Sales Dashboard",
                   page_icon = ":bar_chart:",
                   layout = "wide"
                   )
# ---- READ EXCEL ----

    
df = pd.read_excel(
    io = "data-penindakan-pelanggaran-lalu-lintas-dan-angkutan-jalan-tahun-2021-bulan-juli.xlsx",
    engine = 'openpyxl',
    )

# Membuat kolom total 
data = ['bap_tilang', 'stop_operasi', 'bap_polisi', 'stop_operasi_polisi', 'penderekan', 'ocp_roda_dua', 'ocp_roda_empat', 'angkut_motor']
df['total'] = df[data].sum(axis=1)

# ----SIDEBAR----
st.sidebar.header("Please Filter Here:")
wilayah = st.sidebar.multiselect(
    "Pilih Wilayah:",
    options=df["wilayah"].unique(),
    default=df["wilayah"].unique()
)

# customer_type = st.sidebar.multiselect(
#     "Select the Customer Type:",
#     options=df["Customer_type"].unique(),
#     default=df["Customer_type"].unique(),
# )

# gender = st.sidebar.multiselect(
#     "Select the Gender:",
#     options=df["Gender"].unique(),
#     default=df["Gender"].unique()
# )& Customer_type ==@customer_type & Gender == @gender

df_selection = df.query(
    "wilayah == @wilayah "
)

# ---- MAINPAGE ----
st.header(":bar_chart: Data Penindakan Pelanggaran Lalu Lintas dan Angkutan Jalan Tahun 2021 Bulan Juli")
st.markdown("##")



st.markdown("""---""")
st.dataframe(df_selection)
st.markdown("""---""")
# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = (
    df_selection.groupby(by=["wilayah"]).sum()[["total"]].sort_values(by="wilayah")
)
fig_product_sales = px.bar(
    sales_by_product_line,
    x="total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Total Penindakan Pelanggaran Lalu Lintas</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
st.plotly_chart(fig_product_sales, use_container_width=True)
total = int(df_selection["total"].sum())
st.subheader(f"Total Penidakan : {total:,} Penindakan")
st.markdown("""---""")

# # SALES BY PRODUCT LINE & RATING [PIE CHART]
# fig_total = px.pie(
#     df,
#     names='total',
#     values='total',
#     title="<b>Total Penindakan</b>",
#     hole=0.05, color_discrete_sequence=['#0078AA'],
# )
# st.plotly_chart(fig_total, use_container_width=True)

# # Add histogram data
# x1 = 'ocp_roda_dua'
# x2 = 'ocp_roda_empat'
# x3 = 'penderekan'

# # Group data together
# hist_data = [x1, x2, x3]

# group_labels = ['OCP Roda Dua', 'OCP Roda Empat', 'Penderekan']

# # Create distplot with custom bin_size
# fig = ff.create_distplot(
#          hist_data, group_labels, bin_size=[.1, .25, .5])

# # Plot!
# st.plotly_chart(fig, use_container_width=True)

# TOP KPI's
total_bap_tilang = int(df_selection["bap_tilang"].sum())
total_bap_polisi = int(df_selection["bap_polisi"].sum())
total_stop_operasi = int(df_selection["stop_operasi"].sum())
total_stop_operasi_polisi = int(df_selection["stop_operasi_polisi"].sum())
total_penderekan = int(df_selection["penderekan"].sum())
total_pengangkutan = int(df_selection["angkut_motor"].sum())
total_ocp_roda_dua = int(df_selection["ocp_roda_dua"].sum())
total_ocp_roda_empat = int(df_selection["ocp_roda_empat"].sum())

# left_column, middle_column, right_column = st.columns(3)
# with left_column:
#     st.subheader("Total Penindakan BAP Tilang:")
#     st.subheader(f"{total_bap_tilang:,} Penindakan")
# with middle_column:
#     st.subheader("Total Penindakan BAP Polisi:")
#     st.subheader(f"{total_bap_polisi:,} Penindakan")

# BAP tilang [HISTOGRAM]
fig_bap_tilang = px.histogram(
    df,
    x='wilayah',
    y='bap_tilang',
    labels='bap_tilang',
    title=f"<b>Penindakan BAP Tilang</b><br>Total: {total_bap_tilang:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)
# st.plotly_chart(fig_bap_tilang, use_container_width=True)

# BAP polisi [HISTOGRAM]
fig_bap_polisi = px.histogram(
    df,
    x='wilayah',
    y='bap_polisi',
    labels='bap_polisi',
    title=f"<b>Penindakan BAP Polisi</b><br>Total: {total_bap_polisi:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)
# st.plotly_chart(fig_bap_polisi, use_container_width=True)

# stop operasi [HISTOGRAM]
fig_stop_operasi = px.histogram(
    df,
    x='wilayah',
    y='stop_operasi',
    labels='stop_operasi',
    title=f"<b>Penindakan Stop Operasi</b><br>Total: {total_stop_operasi:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)
# st.plotly_chart(fig_stop_operasi, use_container_width=True)

# Stop Operasi Polisi [HISTOGRAM]
fig_stop_operasi_polisi = px.histogram(
    df,
    x='wilayah',
    y='stop_operasi_polisi',
    labels='stop_operasi_polisi',
    title=f"<b>Penindakan Stop Operasi Polisi</b><br>Total: {total_stop_operasi_polisi:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)
# st.plotly_chart(fig_stop_operasi_polisi, use_container_width=True)

# Penderekan [HISTOGRAM]
fig_penderekan = px.histogram(
    df,
    x='wilayah',
    y='penderekan',
    labels='penderekan',
    title=f"<b>Penindakan Penderekan</b><br>Total: {total_penderekan:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)
# st.plotly_chart(fig_penderekan, use_container_width=True)

# Pengangkutan [HISTOGRAM]
fig_pengangkutan = px.histogram(
    df,
    x='wilayah',
    y='angkut_motor',
    title=f"<b>Penindakan Angkut Motor</b><br>Total: {total_pengangkutan:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)
# st.plotly_chart(fig_pengangkutan, use_container_width=True)


# OCP Roda Dua [HISTOGRAM]
fig_ocp_roda_dua = px.histogram(
    df,
    x='wilayah',
    y='ocp_roda_dua',
    title=f"<b>Penindakan OCP Roda Dua</b><br>Total: {total_ocp_roda_dua:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)
# st.plotly_chart(fig_ocp_roda_dua, use_container_width=True)

# OCP Roda Empat [HISTOGRAM]
fig_ocp_roda_empat = px.histogram(
    df,
    x='wilayah',
    y='ocp_roda_empat',
    title=f"<b>Penindakan OCP Roda Empat</b><br>Total: {total_ocp_roda_empat:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)
# st.plotly_chart(fig_ocp_roda_empat, use_container_width=True)



#Membuat kolom
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.plotly_chart(fig_bap_tilang, use_container_width=True)
    st.plotly_chart(fig_bap_polisi, use_container_width=True)

with col2:
    st.plotly_chart(fig_stop_operasi, use_container_width=True)
    st.plotly_chart(fig_stop_operasi_polisi, use_container_width=True)

with col3:
    st.plotly_chart(fig_penderekan, use_container_width=True)
    st.plotly_chart(fig_pengangkutan, use_container_width=True)

with col4:
    st.plotly_chart(fig_ocp_roda_dua, use_container_width=True)
    st.plotly_chart(fig_ocp_roda_empat, use_container_width=True)


# ---- HIDE STREAMLIT STYLE ----

hide_st_style = """
                <style>
                footer{visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style,unsafe_allow_html = True)       