---
layout: page
title: Data Structure
permalink: /data_structure.html
ref: data_structure
order: 4
---

## DARWIN-1
### FoF/Galaxy Catalog
Each HDF5 file snapshot contains the three subgroups: **halo**(FoF halos), **sub**(substructures, or galaxies), and **unbound**(gravitationally unbounded members within FoF halos). Note that **sub** and **unbound** share exactly the same structure.

| Field | Dimensions | Units | Description |
|:----:|:----:|:---:|----|
| nsub (**halo**) | 1 | | Number of substructures in the given FoF halo |
| halo_index (**sub/unbound**) | 1 | | ID of the corresponding FoF halo (starting from 1) |
| ndm | 1 | | Number of dark matter (DM) particles |
| nstar | 1 | | Number of star particles |
| nMBH | 1 | | Number of massive black hole (MBH) particles |
| ngas | 1 | | Number of gas grids |
| npall | 1 | | ndm + nstar + nMBH + ngas |
| mtot | 1 | M<sub>sun</sub> | Total mass |
| mdm | 1 | M<sub>sun</sub> | DM mass |
| mgas | 1 | M<sub>sun</sub> | Gas mass |
| mMBH | 1 | M<sub>sun</sub> | massive black hole (MBH) mass |
| mstar | 1 | M<sub>sun</sub> | Stellar mass |
| pos | 3 | cMpc | Center-of-mass position of all member particles |
| vel | 3 | km/s | Mass-weighted peculiar velocity | 


### Substructure
Each HDF5 snapshot file contains multiple (usually 400) subgroups of **sub_[substructure ID]**. Each **sub_[substructure_ID]** contains **halo_index** (ID of the corresponding FoF halo), and four subgroups: **star** (stellar particles), **dm** (dark matter particles), **MBH** (massive black hole particles), and **gas** (gas grid).

| Field | Dimensions | Units | Description |
|:--:|:--:|:--:|----|
| pos | 3 | cMpc | Position |
| vel | 3 | km/s | Peculiar velocity |
| mass | 1 | M<sub>sun</sub> | Mass |
| id (**star/dm/MBH**) | 1 | | ID |
| chem (**star/gas**) | 3 | | Mass ratio of H, O, and Mg |
| tp (**star**) / tbirth (**MBH**) | 1 | Gyr | The time when a given particle was formed |
| zp (**star**) / metal (**gas**) | 1 |  | Metallicity |
| mass0 (**star**) | 1 | M<sub>sun</sub> | Initial stellar particle mass |
| angm (**MBH**) | 3 | cMpc km/s | Angular momentum |
| ang (**MBH**) | 3 | - | - |
| dmsmbh (**MBH**) | 1 | - | - |
| esave (**MBH**) | - | - | - |
| smag (**MBH**) | - | - | - |
| eps (**MBH**) | - | - | - |
| dx (**gas**) | 1 | | Grid size |
| density (**gas**) | 1 | M<sub>sun</sub>/cMpc<sup>3</sup> | Gas density |
| temp (**gas**) | 1 | K | Gas temperature |

Since the number and total size of the entire substructure data at each snapshot are very large, we do not provide a direct method to download all of it. Instead, we recommend that you use the following procedure:
1. Download the galaxy catalog and find a list of substructure IDs that you are interested in.
2. Download [download_sub.py](download_sub.py) and run: `python download_sub.py [snapshot id] [substructure ID]`.

## DARWIN-2
N/A

## DARWIN-3
N/A

[Go to the Data Access Page](data.html)
