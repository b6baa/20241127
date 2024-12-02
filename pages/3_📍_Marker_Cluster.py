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
        gdf = gpd.read_file("台中市區界_TWD97-1.shp")
        regions_geojson = gdf.to_json()

        m = leafmap.Map(center=[40, -100], zoom=4)
        bus_stop = "臺中市市區公車站牌資料.csv"
        
        m.add_geojson(regions_geojson, layer_name="臺中市區界")
        m.add_points_from_xy(
            bus_stop,
            x="經度",
            y="緯度",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)
