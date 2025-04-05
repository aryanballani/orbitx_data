import geopandas as gpd
import numpy as np
from shapely.geometry import Point


def load_shapefile(path):
    """
    Load the shapefile and return a GeoDataFrame.
    """
    gdf = gpd.read_file(path)
    return gdf


def buffer_geometry(gdf, buffer_km):
    """
    Buffer the geometry by X kilometers.
    Assumes input GeoDataFrame is in geographic (lat/lon) coordinates.
    """
    # Convert degrees to meters by projecting to UTM first
    gdf_utm = gdf.to_crs(epsg=3395)  # World Mercator
    gdf_buffered = gdf_utm.buffer(buffer_km * 1000)  # buffer in meters
    gdf_buffered = gpd.GeoDataFrame(geometry=gdf_buffered).set_crs(epsg=3395)
    return gdf_buffered.to_crs(epsg=4326)  # back to lat/lon


def generate_grid_points(polygon, spacing_km):
    """
    Generate a grid of lat/lon points within a given polygon geometry.
    spacing_km: approximate grid spacing in kilometers
    """
    from shapely.geometry import box
    import math

    bounds = polygon.bounds
    minx, miny, maxx, maxy = bounds

    # Rough conversion of km to degrees
    lat_spacing = spacing_km / 110.574
    lon_spacing = spacing_km / (111.320 * np.cos(np.radians((miny + maxy) / 2)))

    x_vals = np.arange(minx, maxx, lon_spacing)
    y_vals = np.arange(miny, maxy, lat_spacing)

    points = [Point(x, y) for x in x_vals for y in y_vals if polygon.contains(Point(x, y))]
    return points


def points_to_geodf(points):
    return gpd.GeoDataFrame(geometry=points, crs="EPSG:4326")


# Example usage (will be triggered from main.py):
if __name__ == "__main__":
    shape_path = "data/POLYGON.shp"
    gdf = load_shapefile(shape_path)
    buffered = buffer_geometry(gdf, buffer_km=5)  # 5 km buffer
    all_points = generate_grid_points(buffered.geometry.iloc[0], spacing_km=5)
    grid_gdf = points_to_geodf(all_points)
    print(grid_gdf.head())
