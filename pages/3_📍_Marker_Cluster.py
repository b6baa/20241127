import streamlit as st
import leafmap.foliumap as leafmap
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
        #gdf = gpd.read_file("https://github.com/b6baa/20241127ex2/raw/3edcd55cd41bc1238004abe6d58e0ecf6fefac32/%E5%8F%B0%E4%B8%AD%E5%B8%82%E5%8D%80%E7%95%8C_TWD97-1.shp")
        #regions_geojson = gdf.to_json()

        m = leafmap.Map(center=[40, -100], zoom=4)
        #bus_stop = "https://github.com/b6baa/20241127ex2/raw/3edcd55cd41bc1238004abe6d58e0ecf6fefac32/%E8%87%BA%E4%B8%AD%E5%B8%82%E5%B8%82%E5%8D%80%E5%85%AC%E8%BB%8A%E7%AB%99%E7%89%8C%E8%B3%87%E6%96%99.csv"
        url = "https://data.tainan.gov.tw/dataset/bf7eb079-8b9f-4248-a4a2-877962258763/resource/9072b1a5-7657-406e-8278-a8073167ddb0/download/f0006.json"
        
        #m.add_geojson(regions_geojson, layer_name="臺中市區界")
        m.add_geojson(url, layer_name="新化斷層活動斷層地質敏感區")
        #m.add_points_from_xy(
            #bus_stop,
            #x="經度",
            #y="緯度",
            #icon_names=["gear", "map", "leaf", "globe"],
            #spin=True,
            #add_legend=True,
        #)

m.to_streamlit(height=700)
