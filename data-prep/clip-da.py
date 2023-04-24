import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon, MultiPolygon, GeometryCollection

da = gpd.read_file("gtha-da-2021.geojson")

clip = gpd.read_file("data/green.geojson")
clip = clip[clip.geometry.apply(lambda x: isinstance(x, (Polygon, MultiPolygon)))]

da = gpd.overlay(da, clip, how='difference', keep_geom_type = True)

del clip

clip = gpd.read_file("data/water.geojson")
clip = clip[clip.geometry.apply(lambda x: isinstance(x, (Polygon, MultiPolygon)))]

da = gpd.overlay(da, clip, how='difference', keep_geom_type = True)

del clip

clip = gpd.read_file("data/built-non-res.geojson")
clip = clip[clip.geometry.apply(lambda x: isinstance(x, (Polygon, MultiPolygon)))]

da = gpd.overlay(da, clip, how='difference', keep_geom_type = True)

# da.to_file('gtha-da-2021-clipped.geojson', driver='GeoJSON')

# da = gpd.read_file("gtha-da-2021-clipped.geojson")

dap = da[da.geometry.apply(lambda x: isinstance(x, (Polygon, MultiPolygon)))]

dag = da[da.geometry.apply(lambda x: isinstance(x, (GeometryCollection)))]
dag = dag.explode()
dag = dag[dag.geometry.apply(lambda x: isinstance(x, (Polygon, MultiPolygon)))]
dag = dag.dissolve('DAUID', as_index = False)

da = pd.concat([dap, dag], ignore_index=True)

da.to_file('gtha-da-2021-clipped.geojson', driver='GeoJSON')
