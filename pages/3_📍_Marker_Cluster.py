import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import requests

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map(center=[40, -100], zoom=4)
        bus_stop = gpd.read_file("https://github.com/b6baa/20241127ex2/raw/refs/heads/main/%E8%87%BA%E4%B8%AD%E5%B8%82%E5%B8%82%E5%8D%80%E5%85%AC%E8%BB%8A%E7%AB%99%E7%89%8C%E8%B3%87%E6%96%99.csv")
        
        m.add_points_from_xy(
            bus_stop,
            x="經度",
            y="緯度",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)
