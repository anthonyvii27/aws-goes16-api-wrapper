from datetime import datetime

import numpy as np


def convert_to_date(str_datetime):
    """
    Converts a string date to date

    :param str_datetime: Convert the date in string format to date
    :return: date
    """
    return datetime.strptime(str_datetime, '%Y-%m-%d')


def convert_to_datetime(str_datetime):
    """
    Converts a string date to datetime

    :param str_datetime: Convert the date in string format to datetime
    :return: datetime
    """
    return datetime.strptime(str_datetime, '%Y-%m-%d %H')


def convert_date_to_day_of_year(date):
    """
    Convert a date to day in year

    :param date: Date in datetime format
    :return: string
    """
    return date.strftime('%j')


def calc_latlon(ds):
    # The math for this function was taken from
    # https://makersportal.com/blog/2018/11/25/goes-r-satellite-latitude-and-longitude-grid-projection-algorithm

    x = ds.x
    y = ds.y
    goes_imager_projection = ds.goes_imager_projection

    x, y = np.meshgrid(x, y)

    r_eq = goes_imager_projection.attrs["semi_major_axis"]
    r_pol = goes_imager_projection.attrs["semi_minor_axis"]
    l_0 = goes_imager_projection.attrs["longitude_of_projection_origin"] * (np.pi / 180)
    h_sat = goes_imager_projection.attrs["perspective_point_height"]
    H = r_eq + h_sat

    a = np.sin(x) ** 2 + (np.cos(x) ** 2 * (np.cos(y) ** 2 + (r_eq ** 2 / r_pol ** 2) * np.sin(y) ** 2))
    b = -2 * H * np.cos(x) * np.cos(y)
    c = H ** 2 - r_eq ** 2

    r_s = (-b - np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    s_x = r_s * np.cos(x) * np.cos(y)
    s_y = -r_s * np.sin(x)
    s_z = r_s * np.cos(x) * np.sin(y)

    lat = np.arctan((r_eq ** 2 / r_pol ** 2) * (s_z / np.sqrt((H - s_x) ** 2 + s_y ** 2))) * (180 / np.pi)
    lon = (l_0 - np.arctan(s_y / (H - s_x))) * (180 / np.pi)

    ds = ds.assign_coords({
        "lat": (["y", "x"], lat),
        "lon": (["y", "x"], lon)
    })
    ds.lat.attrs["units"] = "degrees_north"
    ds.lon.attrs["units"] = "degrees_east"

    return ds


def get_xy_from_latlon(ds, lats, lons):
    # This function was taken from
    # https://lsterzinger.medium.com/add-lat-lon-coordinates-to-goes-16-goes-17-l2-data-and-plot-with-cartopy-27f07879157f

    lat1, lat2 = lats
    lon1, lon2 = lons

    lat = ds.lat.data
    lon = ds.lon.data

    x = ds.x.data
    y = ds.y.data

    x, y = np.meshgrid(x, y)

    x = x[(lat >= lat1) & (lat <= lat2) & (lon >= lon1) & (lon <= lon2)]
    y = y[(lat >= lat1) & (lat <= lat2) & (lon >= lon1) & (lon <= lon2)]

    return (min(x), max(x)), (min(y), max(y))
