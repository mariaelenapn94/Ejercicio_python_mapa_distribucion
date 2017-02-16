# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:31:12 2017

@author: Maria Elena Pulido
"""

# INSTRUCCION
# Es necesario instalar el paquete Basemap desde Anaconda Navigator
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# MODIFICABLE
# Debeis ajustar las coordenadas del mapa a la localizacion de la especie
# La ayuda esta en: http://matplotlib.org/basemap/api/basemap_api.html#module-mpl_toolkits.basemap
map = Basemap(projection='mill', resolution='l', llcrnrlon=-10, llcrnrlat=-65, urcrnrlon=190, urcrnrlat=60)

# MODIFICABLE
# Opciones del mapa
# Muchas mas en: http://matplotlib.org/basemap/api/basemap_api.html#module-mpl_toolkits.basemap
map.drawcoastlines(linewidth=0.7)
map.drawcountries(linewidth=0.4)
map.fillcontinents(alpha=0.6)
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30), labels=[False, False, False, True], linewidth=0.1)
map.drawparallels(np.arange(-90, 90, 30), labels=[False, True, False, False], linewidth=0.1)

# INSTRUCCION
# Debeis descargaros un fichero csv con un conjunto de registros (records) de una especie
# desde la pagina del OBIS: http://www.iobis.org y leerla en un DataFrame de pandas
# Ese DataFrame se debe llamar specie

specieAvispa = pd.read_csv('Chironex_fleckeri.csv')
print(specieAvispa)
specieRaya =pd. read_csv('Raya.csv')
print(specieRaya)


# Datos de latitud y longitud de la especie
lonAvispa, latAvispa = map(list(specieAvispa['longitude']), list(specieAvispa['latitude']))
lonRaya, latRaya = map(list(specieRaya['longitude']), list(specieRaya['latitude']))

# MODIFICABLE
# Opciones de visualizacion de la especie
# Muchas mas en: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot

map.plot(lonAvispa, latAvispa, 'ro', markersize=4, markeredgecolor='none' , label='Chironex_fleckeri')
map.plot(lonRaya, latRaya, 'co', markersize=3.8, markeredgecolor='none', label='Gymnura_japonica')

# INSTRUCCION
# Debeis guardar la figura a un archivo pdf

plt.legend(loc='lower right', fontsize='small')
plt.title('Mapa_distribucion_especies_marinas')
plt.savefig("distribution_map_species.pdf")
