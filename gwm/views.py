from django.shortcuts import render
import os
import geopandas as gpd
from django.http import JsonResponse,HttpResponse
from django.conf import settings

import json
import rasterio
import numpy as np
import geopandas as gpd
from rasterio.plot import show
from rasterio.mask import mask
from shapely.geometry import LineString

   



def groundwater(request):
  return render(request,"groundwater.html")




def get_raster_file(request):
    year = request.GET.get("year")
    monsoon = request.GET.get("monsoon")

    if not year or not monsoon:
        return JsonResponse({"error": "Year and monsoon type are required."}, status=400)

    # Construct the file path
    file_name = f"{monsoon}_{year}.tif"
    raster_folder = os.path.join(settings.BASE_DIR, 'gwm', 'tif_files', year, monsoon)
    raster_path = os.path.join(raster_folder, file_name)

    if not os.path.exists(raster_path):
        return JsonResponse({"error": "Raster file not found."}, status=404)

    # Return the GeoTIFF file as binary response
    with open(raster_path, 'rb') as f:
        return HttpResponse(f.read(), content_type="image/tiff")


