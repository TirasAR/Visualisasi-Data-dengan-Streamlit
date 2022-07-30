import pandas as pd
import streamlit as st
import plotly.express as px 

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
total_penindakan = (
    df_selection.groupby(by=["wilayah"]).sum()[["total"]].sort_values(by="wilayah")
)
fig_product_sales = px.bar(
    total_penindakan,
    x="total",
    y=total_penindakan.index,
    orientation="h",
    title="<b>Total Penindakan Pelanggaran Lalu Lintas</b>",
    color_discrete_sequence=["#0083B8"] * len(total_penindakan),
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

# TOP KPI's
total_bap_tilang = int(df_selection["bap_tilang"].sum())
total_bap_polisi = int(df_selection["bap_polisi"].sum())
total_stop_operasi = int(df_selection["stop_operasi"].sum())
total_stop_operasi_polisi = int(df_selection["stop_operasi_polisi"].sum())
total_penderekan = int(df_selection["penderekan"].sum())
total_pengangkutan = int(df_selection["angkut_motor"].sum())
total_ocp_roda_dua = int(df_selection["ocp_roda_dua"].sum())
total_ocp_roda_empat = int(df_selection["ocp_roda_empat"].sum())

# BAP tilang [HISTOGRAM]
fig_bap_tilang = px.histogram(
    df,
    x='wilayah',
    y='bap_tilang',
    title=f"<b>Penindakan BAP Tilang</b><br>Total: {total_bap_tilang:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)

# BAP polisi [HISTOGRAM]
fig_bap_polisi = px.histogram(
    df,
    x='wilayah',
    y='bap_polisi',
    title=f"<b>Penindakan BAP Polisi</b><br>Total: {total_bap_polisi:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)

# stop operasi [HISTOGRAM]
fig_stop_operasi = px.histogram(
    df,
    x='wilayah',
    y='stop_operasi',
    title=f"<b>Penindakan Stop Operasi</b><br>Total: {total_stop_operasi:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)

# Stop Operasi Polisi [HISTOGRAM]
fig_stop_operasi_polisi = px.histogram(
    df,
    x='wilayah',
    y='stop_operasi_polisi',
    title=f"<b>Penindakan Stop Operasi Polisi</b><br>Total: {total_stop_operasi_polisi:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)

# Penderekan [HISTOGRAM]
fig_penderekan = px.histogram(
    df,
    x='wilayah',
    y='penderekan',
    title=f"<b>Penindakan Penderekan</b><br>Total: {total_penderekan:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)

# Pengangkutan [HISTOGRAM]
fig_pengangkutan = px.histogram(
    df,
    x='wilayah',
    y='angkut_motor',
    title=f"<b>Penindakan Angkut Motor</b><br>Total: {total_pengangkutan:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)


# OCP Roda Dua [HISTOGRAM]
fig_ocp_roda_dua = px.histogram(
    df,
    x='wilayah',
    y='ocp_roda_dua',
    title=f"<b>Penindakan OCP Roda Dua</b><br>Total: {total_ocp_roda_dua:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)

# OCP Roda Empat [HISTOGRAM]
fig_ocp_roda_empat = px.histogram(
    df,
    x='wilayah',
    y='ocp_roda_empat',
    title=f"<b>Penindakan OCP Roda Empat</b><br>Total: {total_ocp_roda_empat:,} Penindakan",
    color_discrete_sequence=['#0078AA'],
)

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
