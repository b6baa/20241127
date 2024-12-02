import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import geopandas as gpd

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

        # 初始化地圖
        m = leafmap.Map(center=[24.1477, 120.6736], zoom=12)

        # 讀取 Shapefile 並轉換為 GeoJSON
        gdf = gpd.read_file("台中市區界_TWD97-1.shp")
        regions_geojson = gdf.to_json()
        m.add_geojson(regions_geojson, layer_name="臺中市區界")

        # 讀取公車站牌資料
        cities = pd.read_csv("臺中市市區公車站牌資料.csv")

        # 將站牌資料加入地圖
        m.add_points_from_xy(
            cities,
            x="經度",
            y="緯度",
            color_column="region",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)
