#!/usr/bin/env python
# encoding: utf-8
"""
indexdmap.py

Created by Nils Domrose on 2014-07-26.
"""

import os
import sys
import random
import json
import argparse
import ConfigParser
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import rgb2hex
from mpl_toolkits.basemap import Basemap



cfg = {}
args = None

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

"""
Helper function to validate the existence of a given directory.
This function can be used by the arg parser to validate a custom type.
"""
def valid_directory_name(dir_name):
    if os.path.isdir(dir_name):
        return dir_name
    else:
        msg = "%s is not a valid directory" % dir_name
        raise argparse.ArgumentTypeError(msg)

"""
Helper function to validate the existence of a given file.
This function can be used by the arg parser to validate a custom type.
"""
def valid_file_name(file_name):
    if os.path.isfile(file_name):
        return file_name
    else:
        msg = "%s is not a valid file" % file_name
        raise argparse.ArgumentTypeError(msg)

"""
Helper function to validate the existence of a set of shape files for a
given prefix. The shapefiles can be downloaded from naturalearthdata.com. 
This function can be used by the arg parser to validate a custom type.
"""
def valid_shape_prefix(file_name):
    for suffix in 'shp', 'shx', 'dbf':
        if not os.path.isfile("{file_name}.{suffix}".format(file_name=file_name, suffix=suffix)):
            msg = "{file_name}.{suffix} is not a valid file".format(file_name=file_name, suffix=suffix)
            raise argparse.ArgumentTypeError(msg)

    return file_name


"""
Helper funtion to parse config in a given file and return an dict.
"""
def parse_config(file_name):
    config = ConfigParser.RawConfigParser()
    config.read(file_name)
    cfg = {}
    cfg['output_prefix'] = config.get('defaults', 'output_prefix')
    cfg['image_height'] = config.getint('defaults', 'map_height')
    cfg['image_width'] = config.getint('defaults', 'map_width')
    cfg['dpi'] = config.getint('defaults', 'dpi')
    cfg['bg_color'] = config.get('defaults', 'map_background_color')
    cfg['draw_bounds'] = config.getboolean('defaults', 'map_draw_borders')
    cfg['auto_fill_country'] = config.getboolean('defaults', 'map_auto_fill_country')
    cfg['fill_overwrites'] = config.getboolean('defaults', 'map_fill_overwrites')
    cfg['color_random'] = config.getboolean('defaults', 'map_color_random')
    cfg['color_step'] = config.getfloat('defaults', 'color_step')
    cfg['color_overwrites'] = json.loads(config.get('mappings', 'color_overwrites').replace("'", "\""), encoding='utf-8')
    cfg['country_color_map'] = json.loads(config.get('mappings', 'country_color_map').replace("'", "\""), encoding='utf-8')
    cfg['iso_atwo_fixes'] = json.loads(config.get('mappings', 'iso_atwo_fixes').replace("'", "\""), encoding='utf-8')
    return cfg

"""
Create the figure used for our plot.
"""
def get_figure():
    global cfg
    fig = plt.figure(figsize=(float(cfg['image_width'])/cfg['dpi'], float(cfg['image_height'])/cfg['dpi']))
    ax = plt.Axes(fig, [0.,0.,1,1])
    ax.set_axis_bgcolor(cfg['bg_color'])
    fig.add_axes(ax)
    return fig

"""
create a world map (-90 to 90 and -180 to 180 degrees) and load
the shape file
"""
def get_map(shapefile):
    global cfg
    m = Basemap(resolution='i',projection='cyl', llcrnrlat=-90,urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180)
    m.drawmapboundary()
    m.readshapefile(shapefile, 'countries', drawbounds=cfg['draw_bounds'])
    return m

"""
process data and plot map
"""
def plot_countries(m, ax):
    global cfg
    global args
    colors = {}
    countries = []
    country_index = []

    # create temp color index and country index
    for ncountry, shapedict in enumerate(m.countries_info):
        country_name = shapedict['NAME'].decode('utf-8')
        if country_name in cfg['iso_atwo_fixes'].keys():
            country_code = cfg['iso_atwo_fixes'][country_name]
        else:
            country_code = shapedict['ISO_A2']

        if cfg['color_random']:
            colors[country_code] = rgb2hex((random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
        else:
            colors[country_code] = rgb2hex(cm.gray(cfg['country_color_map'].get(country_code, 255) * cfg['color_step']))

        if cfg['country_color_map'].get(country_code, 255) == 255:
            if args.verbose:
                print "cannot map {country_name}({country_code})".format(country_name= country_name, country_code=country_code)

        if country_code not in countries:
            if args.verbose:
                print "adding {country_name}({country_code}) using color {country_color} ({country_color_raw}) to index.".format(country_name=country_name, country_code=country_code, country_color=colors[country_code], country_color_raw=cfg['country_color_map'].get(country_code, 255))
            countries.append(country_code)
        country_index.append(country_code)

    if args.verbose:
        print "added {country_count} countries to index.".format(country_count=len(countries))

    # plot countries
    for cindex, cc in enumerate(country_index):
        xx,yy = zip(*m.countries[cindex])
        if cc in cfg['color_overwrites'].keys():
            color = cfg['color_overwrites'][cc]
            if cfg['fill_overwrites']:
                ax.fill(xx,yy,color,edgecolor=color)
        else:
            color = colors[cc]
            if cfg['auto_fill_country']:
                ax.fill(xx,yy,color,edgecolor=color)
"""
write the figure to image file
"""
def write_image(fig, filename):
    fig.savefig(filename ,dpi=cfg['dpi'], bbox_inches='tight', pad_inches=0)

def main():
    global cfg
    global args
    parser = argparse.ArgumentParser(description='Process args')
    parser.add_argument('-v', '--verbose',
        help='turn on verbose logging', action="store_true" )
    parser.add_argument('-c', '--config', type=valid_file_name,
        help='config file', required=False,
        default='indexedmap.ini')
    parser.add_argument('-s', '--shapeprefix', type=valid_shape_prefix,
        help='shape file prefix pointing to a shape set', required=False,
        default='shapes/ne_10m_admin_0_sovereignty')
    parser.add_argument('-o', '--output', type=valid_directory_name,
        help='output directory', required=False,
        default='output')

    try:
        args = parser.parse_args()
        cfg = parse_config(args.config) 
        my_fig = get_figure()
        my_map = get_map(args.shapeprefix)
        my_ax = my_fig.get_axes()[0]
        plot_countries(my_map, my_ax)
        write_image(my_fig, os.path.join(args.output, "{filename}.png".format(filename=cfg['output_prefix'])))

    except parser.error, msg:
        raise Usage(msg)



if __name__ == "__main__":
    sys.exit(main())

