---
layout: page
title: Data Access - DARWIN-1
permalink: /data_darwin1.html
ref: data_darwin1
order: 5
---

## Simulation Overview
Please see [Simulation Overview](data.html) for details.

| Boxsize | Minimum Resolution | Minimum DM Particle Mass | Minimum Stellar Particle Mass | Chemical Species |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| 65Mpc | 500pc | 9x10<sup>5</sup>M<sub>sun</sub> | 10<sup>5</sup>M<sub>sun</sub> | H, Fe, O |


## Data Access
**The DARWIN-1 simulation run has reached redshift 0.19 (snapshot \#1001; look-back time 2.4 Gyr).**

Only the galaxy/halo catalogs in the HDF5 format are available on this page.
Please [contact us](contact.md) to access other data.

<!-- DataTables CSS 및 Cayman 테마 디자인 보정 -->
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
<style>
.dataTables_wrapper {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: #606c71;
  margin: 1.5rem 0;
}
.dataTables_wrapper .dataTables_length select,
.dataTables_wrapper .dataTables_filter input {
  border: 1px solid #e1e4e8;
  border-radius: 6px;
  padding: 5px 8px;
  outline: none;
}
.dataTables_wrapper .dataTables_filter input:focus {
  border-color: #159957;
  box-shadow: 0 0 0 3px rgba(21, 153, 87, 0.15);
}
.dataTables_wrapper .dataTables_paginate .paginate_button.current {
  background: #159957 !important;
  color: #ffffff !important;
  border: 1px solid #159957 !important;
  border-radius: 4px;
}
.dataTables_wrapper .dataTables_paginate .paginate_button:hover {
  background: #155799 !important;
  color: #ffffff !important;
  border: 1px solid #155799 !important;
  border-radius: 4px;
}
.table-responsive-wrapper {
  overflow-x: auto;
}
table.dataTable {
  width: 100% !important;
  border-collapse: collapse !important;
  margin: 10px 0 !important;
  display: table !important; /* Cayman 테마의 display: block 무효화 */
  table-layout: fixed !important; /* 내용물 크기 대신 100% 비율을 강제 적용 */
}
table.dataTable thead th {
  background-color: #f6f8fa;
  color: #159957;
  border-bottom: 2px solid #e1e4e8 !important;
}
/* 각 4개 열의 너비 비율을 명시적으로 지정 */
table.dataTable th:nth-child(1) { width: 15% !important; } /* Snapshot # */
table.dataTable th:nth-child(2) { width: 20% !important; } /* Redshift */
table.dataTable th:nth-child(3) { width: 35% !important; } /* Lookback Time [Gyr] */
table.dataTable th:nth-child(4) { width: 30% !important; } /* FoF/Galaxy Catalog */
</style>

<div class="table-responsive-wrapper" markdown="1">

| Snapshot # | Redshift | Lookback Time [Gyr] | FoF/Galaxy Catalog |
| ------: | ------: | ------: | :------: |
| 2 | 15.998911 | 13.550491 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0002/catalog_0002.hdf5) |
| 3 | 15.602071 | 13.541624 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0003/catalog_0003.hdf5) |
| 4 | 15.215489 | 13.532463 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0004/catalog_0004.hdf5) |
| 5 | 14.836473 | 13.522934 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0005/catalog_0005.hdf5) |
| 6 | 14.466837 | 13.513078 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0006/catalog_0006.hdf5) |
| 8 | 13.754278 | 13.492316 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0008/catalog_0008.hdf5) |
| 9 | 13.409886 | 13.481353 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0009/catalog_0009.hdf5) |
| 10 | 13.072511 | 13.469962 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0010/catalog_0010.hdf5) |
| 11 | 12.744228 | 13.458202 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0011/catalog_0011.hdf5) |
| 12 | 12.424252 | 13.446044 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0012/catalog_0012.hdf5) |
| 13 | 12.111511 | 13.433441 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0013/catalog_0013.hdf5) |
| 14 | 11.804870 | 13.420331 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0014/catalog_0014.hdf5) |
| 15 | 11.506161 | 13.406785 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0015/catalog_0015.hdf5) |
| 16 | 11.214418 | 13.392749 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0016/catalog_0016.hdf5) |
| 17 | 10.930043 | 13.378241 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0017/catalog_0017.hdf5) |
| 18 | 10.651324 | 13.363153 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0018/catalog_0018.hdf5) |
| 19 | 10.379637 | 13.347557 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0019/catalog_0019.hdf5) |
| 20 | 10.113751 | 13.331362 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0020/catalog_0020.hdf5) |
| 21 | 9.854635 | 13.314625 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0021/catalog_0021.hdf5) |
| 22 | 9.601074 | 13.297248 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0022/catalog_0022.hdf5) |
| 23 | 9.353641 | 13.279262 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0023/catalog_0023.hdf5) |
| 24 | 9.112143 | 13.260642 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0024/catalog_0024.hdf5) |
| 25 | 8.876398 | 13.241360 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0025/catalog_0025.hdf5) |
| 26 | 8.645826 | 13.221361 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0026/catalog_0026.hdf5) |
| 27 | 8.421075 | 13.200677 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0027/catalog_0027.hdf5) |
| 28 | 8.201312 | 13.179234 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0028/catalog_0028.hdf5) |
| 29 | 7.986427 | 13.156985 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0029/catalog_0029.hdf5) |
| 30 | 7.776735 | 13.133963 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0030/catalog_0030.hdf5) |
| 31 | 7.572019 | 13.110119 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0031/catalog_0031.hdf5) |
| 32 | 7.372070 | 13.085420 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0032/catalog_0032.hdf5) |
| 33 | 7.176583 | 13.059806 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0033/catalog_0033.hdf5) |
| 34 | 6.985889 | 13.033305 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0034/catalog_0034.hdf5) |
| 35 | 6.799279 | 13.005799 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0035/catalog_0035.hdf5) |
| 36 | 6.617302 | 12.977343 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0036/catalog_0036.hdf5) |
| 37 | 6.439672 | 12.947891 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0037/catalog_0037.hdf5) |
| 38 | 6.266124 | 12.917363 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0038/catalog_0038.hdf5) |
| 39 | 6.096578 | 12.885746 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0039/catalog_0039.hdf5) |
| 40 | 5.931068 | 12.852999 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0040/catalog_0040.hdf5) |
| 41 | 5.769260 | 12.819057 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0041/catalog_0041.hdf5) |
| 42 | 5.611431 | 12.783937 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0042/catalog_0042.hdf5) |
| 43 | 5.457164 | 12.747538 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0043/catalog_0043.hdf5) |
| 44 | 5.306400 | 12.709812 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0044/catalog_0044.hdf5) |
| 45 | 5.159218 | 12.670750 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0045/catalog_0045.hdf5) |
| 46 | 5.015389 | 12.630275 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0046/catalog_0046.hdf5) |
| 47 | 4.875216 | 12.588438 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0047/catalog_0047.hdf5) |
| 48 | 4.738032 | 12.545033 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0048/catalog_0048.hdf5) |
| 49 | 4.604179 | 12.500107 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0049/catalog_0049.hdf5) |
| 50 | 4.473532 | 12.453630 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0050/catalog_0050.hdf5) |
| 51 | 4.345704 | 12.405398 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0051/catalog_0051.hdf5) |
| 52 | 4.220746 | 12.355419 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0052/catalog_0052.hdf5) |
| 53 | 4.103052 | 12.305548 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0053/catalog_0053.hdf5) |
| 54 | 3.991432 | 12.255546 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0054/catalog_0054.hdf5) |
| 55 | 3.885824 | 12.205619 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0055/catalog_0055.hdf5) |
| 56 | 3.785387 | 12.155603 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0056/catalog_0056.hdf5) |
| 57 | 3.690060 | 12.105674 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0057/catalog_0057.hdf5) |
| 58 | 3.598919 | 12.055530 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0058/catalog_0058.hdf5) |
| 59 | 3.512253 | 12.005520 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0059/catalog_0059.hdf5) |
| 60 | 3.429723 | 11.955651 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0060/catalog_0060.hdf5) |
| 61 | 3.350716 | 11.905711 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0061/catalog_0061.hdf5) |
| 65 | 3.275096 | 11.855770 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0065/catalog_0065.hdf5) |
| 69 | 3.202547 | 11.805793 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0069/catalog_0069.hdf5) |
| 73 | 3.133094 | 11.755911 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0073/catalog_0073.hdf5) |
| 77 | 3.066178 | 11.705860 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0077/catalog_0077.hdf5) |
| 81 | 3.002028 | 11.655946 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0081/catalog_0081.hdf5) |
| 85 | 2.940164 | 11.605918 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0085/catalog_0085.hdf5) |
| 89 | 2.880847 | 11.556110 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0089/catalog_0089.hdf5) |
| 92 | 2.823425 | 11.506074 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0092/catalog_0092.hdf5) |
| 96 | 2.768031 | 11.456049 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0096/catalog_0096.hdf5) |
| 100 | 2.714672 | 11.406138 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0100/catalog_0100.hdf5) |
| 104 | 2.663184 | 11.356270 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0104/catalog_0104.hdf5) |
| 107 | 2.613324 | 11.306346 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0107/catalog_0107.hdf5) |
| 111 | 2.565029 | 11.256350 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0111/catalog_0111.hdf5) |
| 115 | 2.518287 | 11.206374 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0115/catalog_0115.hdf5) |
| 118 | 2.473016 | 11.156410 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0118/catalog_0118.hdf5) |
| 122 | 2.429183 | 11.106506 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0122/catalog_0122.hdf5) |
| 125 | 2.386633 | 11.056537 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0125/catalog_0125.hdf5) |
| 128 | 2.345323 | 11.006588 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0128/catalog_0128.hdf5) |
| 132 | 2.305214 | 10.956630 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0132/catalog_0132.hdf5) |
| 137 | 2.266213 | 10.906606 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0137/catalog_0137.hdf5) |
| 143 | 2.228284 | 10.856559 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0143/catalog_0143.hdf5) |
| 148 | 2.191366 | 10.806496 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0148/catalog_0148.hdf5) |
| 154 | 2.155577 | 10.756603 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0154/catalog_0154.hdf5) |
| 159 | 2.120809 | 10.706812 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0159/catalog_0159.hdf5) |
| 164 | 2.086860 | 10.656902 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0164/catalog_0164.hdf5) |
| 169 | 2.053649 | 10.606767 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0169/catalog_0169.hdf5) |
| 174 | 2.021308 | 10.556681 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0174/catalog_0174.hdf5) |
| 178 | 1.990001 | 10.506964 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0178/catalog_0178.hdf5) |
| 183 | 1.959296 | 10.456978 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0183/catalog_0183.hdf5) |
| 187 | 1.929194 | 10.406759 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0187/catalog_0187.hdf5) |
| 191 | 1.900093 | 10.357023 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0191/catalog_0191.hdf5) |
| 195 | 1.871607 | 10.307173 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0195/catalog_0195.hdf5) |
| 199 | 1.843463 | 10.256766 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0199/catalog_0199.hdf5) |
| 203 | 1.816464 | 10.207304 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0203/catalog_0203.hdf5) |
| 208 | 1.789709 | 10.157147 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0208/catalog_0208.hdf5) |
| 212 | 1.763635 | 10.107161 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0212/catalog_0212.hdf5) |
| 216 | 1.738203 | 10.057308 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0216/catalog_0216.hdf5) |
| 220 | 1.713138 | 10.007117 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0220/catalog_0220.hdf5) |
| 224 | 1.688825 | 9.957393 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0224/catalog_0224.hdf5) |
| 228 | 1.664850 | 9.907269 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0228/catalog_0228.hdf5) |
| 232 | 1.641544 | 9.857553 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0232/catalog_0232.hdf5) |
| 236 | 1.618482 | 9.807340 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0236/catalog_0236.hdf5) |
| 240 | 1.596111 | 9.757590 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0240/catalog_0240.hdf5) |
| 244 | 1.573982 | 9.707442 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0244/catalog_0244.hdf5) |
| 248 | 1.552496 | 9.657755 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0248/catalog_0248.hdf5) |
| 252 | 1.531176 | 9.607452 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0252/catalog_0252.hdf5) |
| 256 | 1.510559 | 9.557908 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0256/catalog_0256.hdf5) |
| 261 | 1.489986 | 9.507476 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0261/catalog_0261.hdf5) |
| 265 | 1.470153 | 9.457997 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0265/catalog_0265.hdf5) |
| 270 | 1.450296 | 9.407464 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0270/catalog_0270.hdf5) |
| 276 | 1.431204 | 9.358048 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0276/catalog_0276.hdf5) |
| 281 | 1.412194 | 9.307876 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0281/catalog_0281.hdf5) |
| 286 | 1.393614 | 9.258020 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0286/catalog_0286.hdf5) |
| 292 | 1.375382 | 9.208168 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0292/catalog_0292.hdf5) |
| 297 | 1.357272 | 9.157806 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0297/catalog_0297.hdf5) |
| 302 | 1.339790 | 9.108329 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0302/catalog_0302.hdf5) |
| 307 | 1.322282 | 9.057909 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0307/catalog_0307.hdf5) |
| 312 | 1.305307 | 9.008236 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0312/catalog_0312.hdf5) |
| 319 | 1.288565 | 8.958384 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0319/catalog_0319.hdf5) |
| 324 | 1.271881 | 8.907916 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0324/catalog_0324.hdf5) |
| 332 | 1.255801 | 8.858455 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0332/catalog_0332.hdf5) |
| 341 | 1.239769 | 8.808291 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0341/catalog_0341.hdf5) |
| 349 | 1.223991 | 8.758198 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0349/catalog_0349.hdf5) |
| 358 | 1.208671 | 8.708792 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0358/catalog_0358.hdf5) |
| 366 | 1.193310 | 8.658385 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0366/catalog_0366.hdf5) |
| 374 | 1.178274 | 8.608340 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0374/catalog_0374.hdf5) |
| 382 | 1.163647 | 8.558926 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0382/catalog_0382.hdf5) |
| 390 | 1.148978 | 8.508556 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0390/catalog_0390.hdf5) |
| 398 | 1.134610 | 8.458483 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0398/catalog_0398.hdf5) |
| 406 | 1.120606 | 8.408982 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0406/catalog_0406.hdf5) |
| 414 | 1.106588 | 8.358705 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0414/catalog_0414.hdf5) |
| 422 | 1.092831 | 8.308595 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0422/catalog_0422.hdf5) |
| 429 | 1.079420 | 8.259037 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0429/catalog_0429.hdf5) |
| 437 | 1.066077 | 8.209053 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0437/catalog_0437.hdf5) |
| 445 | 1.052733 | 8.158374 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0445/catalog_0445.hdf5) |
| 452 | 1.039983 | 8.109228 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0452/catalog_0452.hdf5) |
| 460 | 1.027198 | 8.059307 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0460/catalog_0460.hdf5) |
| 468 | 1.014433 | 8.008675 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0468/catalog_0468.hdf5) |
| 475 | 1.002068 | 7.959043 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0475/catalog_0475.hdf5) |
| 482 | 0.989901 | 7.909551 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0482/catalog_0482.hdf5) |
| 490 | 0.977728 | 7.859338 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0490/catalog_0490.hdf5) |
| 497 | 0.965562 | 7.808515 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0497/catalog_0497.hdf5) |
| 506 | 0.953988 | 7.759490 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0506/catalog_0506.hdf5) |
| 513 | 0.942389 | 7.709707 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0513/catalog_0513.hdf5) |
| 520 | 0.930804 | 7.659372 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0520/catalog_0520.hdf5) |
| 527 | 0.919320 | 7.608842 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0527/catalog_0527.hdf5) |
| 535 | 0.908278 | 7.559617 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0535/catalog_0535.hdf5) |
| 543 | 0.897269 | 7.509949 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0543/catalog_0543.hdf5) |
| 552 | 0.886237 | 7.459571 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0552/catalog_0552.hdf5) |
| 560 | 0.875300 | 7.409012 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0560/catalog_0560.hdf5) |
| 568 | 0.864826 | 7.359944 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0568/catalog_0568.hdf5) |
| 577 | 0.854321 | 7.310147 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0577/catalog_0577.hdf5) |
| 585 | 0.843827 | 7.259822 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0585/catalog_0585.hdf5) |
| 594 | 0.833367 | 7.209057 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0594/catalog_0594.hdf5) |
| 603 | 0.823363 | 7.159941 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0603/catalog_0603.hdf5) |
| 611 | 0.813362 | 7.110261 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0611/catalog_0611.hdf5) |
| 618 | 0.803389 | 7.060108 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0618/catalog_0618.hdf5) |
| 622 | 0.793423 | 7.009417 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0622/catalog_0622.hdf5) |
| 628 | 0.783774 | 6.959782 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0628/catalog_0628.hdf5) |
| 633 | 0.774292 | 6.910461 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0633/catalog_0633.hdf5) |
| 637 | 0.764817 | 6.860631 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0637/catalog_0637.hdf5) |
| 642 | 0.755324 | 6.810148 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0642/catalog_0642.hdf5) |
| 647 | 0.745856 | 6.759237 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0647/catalog_0647.hdf5) |
| 652 | 0.736846 | 6.710257 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0652/catalog_0652.hdf5) |
| 658 | 0.727857 | 6.660871 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0658/catalog_0658.hdf5) |
| 662 | 0.718830 | 6.610735 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0662/catalog_0662.hdf5) |
| 667 | 0.709837 | 6.560252 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0667/catalog_0667.hdf5) |
| 672 | 0.700916 | 6.509638 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0672/catalog_0672.hdf5) |
| 677 | 0.692348 | 6.460511 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0677/catalog_0677.hdf5) |
| 681 | 0.683827 | 6.411143 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0681/catalog_0681.hdf5) |
| 686 | 0.675288 | 6.361159 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0686/catalog_0686.hdf5) |
| 691 | 0.666727 | 6.310527 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0691/catalog_0691.hdf5) |
| 697 | 0.658199 | 6.259564 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0697/catalog_0697.hdf5) |
| 701 | 0.650091 | 6.210611 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0701/catalog_0701.hdf5) |
| 705 | 0.642006 | 6.161317 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0705/catalog_0705.hdf5) |
| 710 | 0.633898 | 6.111389 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0710/catalog_0710.hdf5) |
| 714 | 0.625795 | 6.061002 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0714/catalog_0714.hdf5) |
| 719 | 0.617691 | 6.010107 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0719/catalog_0719.hdf5) |
| 723 | 0.609861 | 5.960443 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0723/catalog_0723.hdf5) |
| 727 | 0.602186 | 5.911311 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0727/catalog_0727.hdf5) |
| 732 | 0.594474 | 5.861429 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0732/catalog_0732.hdf5) |
| 736 | 0.586858 | 5.811706 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0736/catalog_0736.hdf5) |
| 741 | 0.579160 | 5.760981 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0741/catalog_0741.hdf5) |
| 746 | 0.571487 | 5.709943 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0746/catalog_0746.hdf5) |
| 750 | 0.564183 | 5.660913 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0750/catalog_0750.hdf5) |
| 754 | 0.556910 | 5.611657 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0754/catalog_0754.hdf5) |
| 758 | 0.549656 | 5.562097 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0758/catalog_0758.hdf5) |
| 762 | 0.542410 | 5.512049 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0762/catalog_0762.hdf5) |
| 765 | 0.535117 | 5.461209 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0765/catalog_0765.hdf5) |
| 770 | 0.527865 | 5.410199 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0770/catalog_0770.hdf5) |
| 774 | 0.520936 | 5.361076 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0774/catalog_0774.hdf5) |
| 778 | 0.514070 | 5.312038 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0778/catalog_0778.hdf5) |
| 782 | 0.507192 | 5.262404 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0782/catalog_0782.hdf5) |
| 786 | 0.500319 | 5.212328 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0786/catalog_0786.hdf5) |
| 789 | 0.493436 | 5.161769 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0789/catalog_0789.hdf5) |
| 793 | 0.486570 | 5.110918 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0793/catalog_0793.hdf5) |
| 798 | 0.479873 | 5.060883 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0798/catalog_0798.hdf5) |
| 801 | 0.473379 | 5.011864 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0801/catalog_0801.hdf5) |
| 805 | 0.466897 | 4.962623 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0805/catalog_0805.hdf5) |
| 808 | 0.460379 | 4.912735 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0808/catalog_0808.hdf5) |
| 811 | 0.453884 | 4.862556 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0811/catalog_0811.hdf5) |
| 815 | 0.447408 | 4.812007 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0815/catalog_0815.hdf5) |
| 820 | 0.440897 | 4.760803 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0820/catalog_0820.hdf5) |
| 823 | 0.434641 | 4.711285 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0823/catalog_0823.hdf5) |
| 827 | 0.428511 | 4.662304 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0827/catalog_0827.hdf5) |
| 831 | 0.422383 | 4.612945 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0831/catalog_0831.hdf5) |
| 835 | 0.416258 | 4.563285 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0835/catalog_0835.hdf5) |
| 837 | 0.410112 | 4.512957 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0837/catalog_0837.hdf5) |
| 841 | 0.403984 | 4.462298 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0841/catalog_0841.hdf5) |
| 844 | 0.397855 | 4.411415 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0844/catalog_0844.hdf5) |
| 848 | 0.391906 | 4.361623 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0848/catalog_0848.hdf5) |
| 852 | 0.386097 | 4.312490 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0852/catalog_0852.hdf5) |
| 856 | 0.380314 | 4.263294 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0856/catalog_0856.hdf5) |
| 859 | 0.374510 | 4.213465 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0859/catalog_0859.hdf5) |
| 863 | 0.368732 | 4.163531 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0863/catalog_0863.hdf5) |
| 867 | 0.362932 | 4.113119 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0867/catalog_0867.hdf5) |
| 871 | 0.357153 | 4.062374 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0871/catalog_0871.hdf5) |
| 875 | 0.351339 | 4.010892 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0875/catalog_0875.hdf5) |
| 878 | 0.345869 | 3.962201 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0878/catalog_0878.hdf5) |
| 881 | 0.340403 | 3.913103 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0881/catalog_0881.hdf5) |
| 885 | 0.334941 | 3.863768 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0885/catalog_0885.hdf5) |
| 889 | 0.329477 | 3.814028 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0889/catalog_0889.hdf5) |
| 892 | 0.324015 | 3.763794 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0892/catalog_0892.hdf5) |
| 896 | 0.318571 | 3.713612 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0896/catalog_0896.hdf5) |
| 900 | 0.313079 | 3.662444 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0900/catalog_0900.hdf5) |
| 904 | 0.307618 | 3.611228 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0904/catalog_0904.hdf5) |
| 907 | 0.302507 | 3.562964 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0907/catalog_0907.hdf5) |
| 912 | 0.297298 | 3.513318 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0912/catalog_0912.hdf5) |
| 915 | 0.292145 | 3.464165 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0915/catalog_0915.hdf5) |
| 918 | 0.287021 | 3.414616 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0918/catalog_0918.hdf5) |
| 921 | 0.281844 | 3.364367 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0921/catalog_0921.hdf5) |
| 925 | 0.276708 | 3.314049 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0925/catalog_0925.hdf5) |
| 928 | 0.271568 | 3.263480 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0928/catalog_0928.hdf5) |
| 932 | 0.266407 | 3.212359 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0932/catalog_0932.hdf5) |
| 936 | 0.261388 | 3.162131 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0936/catalog_0936.hdf5) |
| 940 | 0.256531 | 3.113369 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0940/catalog_0940.hdf5) |
| 944 | 0.251684 | 3.064258 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0944/catalog_0944.hdf5) |
| 948 | 0.246816 | 3.014838 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0948/catalog_0948.hdf5) |
| 953 | 0.241981 | 2.965014 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0953/catalog_0953.hdf5) |
| 958 | 0.237118 | 2.914937 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0958/catalog_0958.hdf5) |
| 962 | 0.232279 | 2.864560 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0962/catalog_0962.hdf5) |
| 967 | 0.227424 | 2.813845 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0967/catalog_0967.hdf5) |
| 972 | 0.222581 | 2.762698 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0972/catalog_0972.hdf5) |
| 977	| 0.217836 | 2.712470 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0977/catalog_0977.hdf5) |
| 980	| 0.213243 | 2.663432 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0980/catalog_0980.hdf5) |
| 984	| 0.208698 | 2.614665 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0984/catalog_0984.hdf5) |
| 988	| 0.204139 | 2.565248 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0988/catalog_0988.hdf5) |
| 992 | 0.199567 | 2.515682 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0992/catalog_0992.hdf5) |
| 997 | 0.195003 | 2.465654 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/0997/catalog_0997.hdf5) |
| 1001 | 0.190438 | 2.415401 | [Download](https://archive.kasi.re.kr/darwin/coconas/Darwin/Darwin1/1001/catalog_1001.hdf5) |

</div>

<!-- jQuery 및 DataTables 라이브러리 및 실행 스크립트 -->
<script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
<script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
<script>
document.addEventListener("DOMContentLoaded", function() {
  var checkAndInit = setInterval(function() {
    if (window.jQuery && $.fn.DataTable) {
      clearInterval(checkAndInit);
      var $table = $('.table-responsive-wrapper table');
      if ($table.length) {
        $table.DataTable({
          "pageLength": 25,
          "autoWidth": false, // 자바스크립트의 자동 폭 계산 끄기
          "lengthMenu": [10,25,50,100],
          "language": {
            "search": "Search: ",
            "lengthMenu": "Show _MENU_ entries",
            "info": "Showing _START_ to _END_ of _TOTAL_ entries",
            "paginate": {
              "previous": "Previous",
              "next": "Next"
            }
          }
        });
      }
    }
  }, 100);
});
</script>

[Go to the Home Page]({{ '/' | absolute_url }})
