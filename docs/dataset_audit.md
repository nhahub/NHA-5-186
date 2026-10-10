# Dataset Acceptance Audit — D22

- Generated at (UTC): 2026-10-10T15:53:48.436424+00:00
- Scope: deduped MegaVul and Big-Vul only.
- This report does not claim acceptance for datasets that were not audited.

## 1. Dataset Summary

| Dataset | Rows | Columns | Unique hashes | Rows in duplicate-hash groups | Empty code rows |
|---|---:|---:|---:|---:|---:|
| MegaVul | 336803 | 8 | 336803 | 0 | 0 |
| Big-Vul | 103345 | 8 | 103345 | 0 | 0 |
| cvefixes_cpp | 2628 | 8 | 2628 | 0 | 0 |
| cvefixes_python | 4486 | 8 | 4486 | 0 | 0 |

## 2. Structural and Data-Quality Checks

### MegaVul

- File: `C:\Users\eyada\OneDrive\Desktop\SHIELD\data\interim\megavul_deduped.parquet`
- Detected code column: `code`
- Detected label column: `label`
- Detected language column: `language`
- Detected CWE column: `cwe`
- Detected hash column: `None`
- Missing required schema columns: `[]`
- Valid binary labels (0/1): `True`
- Invalid or missing labels: `0`

#### Missing values by column

| column     |   missing_count |   missing_pct |
|:-----------|----------------:|--------------:|
| code       |               0 |         0     |
| language   |               0 |         0     |
| label      |               0 |         0     |
| cwe        |               0 |         0     |
| project    |               0 |         0     |
| commit     |               0 |         0     |
| fixed_code |          320179 |        95.064 |
| source     |               0 |         0     |

#### Empty strings by column

| column     |   empty_strings |
|:-----------|----------------:|
| code       |               0 |
| language   |               0 |
| cwe        |               0 |
| project    |               0 |
| commit     |               0 |
| fixed_code |               0 |
| source     |               0 |

#### Label distribution

|   label |   count |
|--------:|--------:|
|       1 |   16624 |
|       0 |  320179 |

### Big-Vul

- File: `C:\Users\eyada\OneDrive\Desktop\SHIELD\data\interim\bigvul_deduped.parquet`
- Detected code column: `code`
- Detected label column: `label`
- Detected language column: `language`
- Detected CWE column: `cwe`
- Detected hash column: `None`
- Missing required schema columns: `[]`
- Valid binary labels (0/1): `True`
- Invalid or missing labels: `0`

#### Missing values by column

| column     |   missing_count |   missing_pct |
|:-----------|----------------:|--------------:|
| code       |               0 |         0     |
| language   |               0 |         0     |
| label      |               0 |         0     |
| cwe        |               0 |         0     |
| project    |               0 |         0     |
| commit     |               0 |         0     |
| fixed_code |           97474 |        94.319 |
| source     |               0 |         0     |

#### Empty strings by column

| column     |   empty_strings |
|:-----------|----------------:|
| code       |               0 |
| language   |               0 |
| cwe        |               0 |
| project    |               0 |
| commit     |               0 |
| fixed_code |               0 |
| source     |               0 |

#### Label distribution

|   label |   count |
|--------:|--------:|
|       0 |   97474 |
|       1 |    5871 |

### cvefixes_cpp

- File: `C:\Users\eyada\OneDrive\Desktop\SHIELD\data\interim\cvefixes_cpp_deduped.parquet`
- Detected code column: `code`
- Detected label column: `label`
- Detected language column: `language`
- Detected CWE column: `cwe`
- Detected hash column: `None`
- Missing required schema columns: `[]`
- Valid binary labels (0/1): `True`
- Invalid or missing labels: `0`

#### Missing values by column

| column     |   missing_count |   missing_pct |
|:-----------|----------------:|--------------:|
| code       |               0 |         0     |
| language   |               0 |         0     |
| label      |               0 |         0     |
| cwe        |               0 |         0     |
| project    |               0 |         0     |
| commit     |               0 |         0     |
| fixed_code |            1749 |        66.553 |
| source     |               0 |         0     |

#### Empty strings by column

| column     |   empty_strings |
|:-----------|----------------:|
| code       |               0 |
| language   |               0 |
| cwe        |               0 |
| project    |               0 |
| commit     |               0 |
| fixed_code |               0 |
| source     |               0 |

#### Label distribution

|   label |   count |
|--------:|--------:|
|       1 |    1074 |
|       0 |    1554 |

### cvefixes_python

- File: `C:\Users\eyada\OneDrive\Desktop\SHIELD\data\interim\cvefixes_python_deduped.parquet`
- Detected code column: `code`
- Detected label column: `label`
- Detected language column: `language`
- Detected CWE column: `cwe`
- Detected hash column: `None`
- Missing required schema columns: `[]`
- Valid binary labels (0/1): `True`
- Invalid or missing labels: `0`

#### Missing values by column

| column     |   missing_count |   missing_pct |
|:-----------|----------------:|--------------:|
| code       |               0 |         0     |
| language   |               0 |         0     |
| label      |               0 |         0     |
| cwe        |               0 |         0     |
| project    |               0 |         0     |
| commit     |               0 |         0     |
| fixed_code |            2539 |        56.598 |
| source     |               0 |         0     |

#### Empty strings by column

| column     |   empty_strings |
|:-----------|----------------:|
| code       |               0 |
| language   |               0 |
| cwe        |               0 |
| project    |               0 |
| commit     |               0 |
| fixed_code |               0 |
| source     |               0 |

#### Label distribution

|   label |   count |
|--------:|--------:|
|       1 |    2542 |
|       0 |    1944 |

## 3. Language × CWE Count Matrix

Counts are calculated from the available language and CWE columns. Vulnerable counts assume label 1 means vulnerable; verify this convention against the project dataset documentation.

| dataset         | language   | cwe       |   total_samples |   vulnerable_samples |
|:----------------|:-----------|:----------|----------------:|---------------------:|
| MegaVul         | cpp        | CWE-119   |           26405 |                 1589 |
| MegaVul         | cpp        | CWE-787   |           28120 |                 1509 |
| MegaVul         | cpp        | CWE-125   |           23577 |                 1443 |
| MegaVul         | cpp        | <MISSING> |           31415 |                 1400 |
| MegaVul         | cpp        | CWE-476   |           26965 |                 1286 |
| MegaVul         | cpp        | CWE-20    |           19448 |                 1070 |
| MegaVul         | cpp        | CWE-416   |           24599 |                 1004 |
| MegaVul         | cpp        | CWE-190   |           11781 |                  708 |
| MegaVul         | cpp        | CWE-200   |           11801 |                  560 |
| MegaVul         | cpp        | CWE-362   |           10623 |                  509 |
| MegaVul         | cpp        | CWE-399   |            9985 |                  439 |
| MegaVul         | cpp        | CWE-264   |            9541 |                  426 |
| MegaVul         | cpp        | CWE-120   |            6657 |                  424 |
| MegaVul         | cpp        | CWE-400   |            6223 |                  313 |
| MegaVul         | cpp        | CWE-189   |            6005 |                  295 |
| MegaVul         | cpp        | CWE-401   |           11501 |                  280 |
| MegaVul         | cpp        | CWE-617   |            4039 |                  260 |
| MegaVul         | cpp        | CWE-835   |            5079 |                  251 |
| MegaVul         | cpp        | CWE-415   |            6091 |                  184 |
| MegaVul         | cpp        | CWE-772   |            2974 |                  174 |
| MegaVul         | cpp        | CWE-369   |            2496 |                  169 |
| MegaVul         | cpp        | CWE-22    |            3758 |                  155 |
| MegaVul         | cpp        | CWE-254   |            2872 |                  128 |
| MegaVul         | cpp        | CWE-674   |            1981 |                  120 |
| MegaVul         | cpp        | CWE-122   |            2090 |                  115 |
| MegaVul         | cpp        | CWE-908   |            1816 |                  102 |
| MegaVul         | cpp        | CWE-59    |            1747 |                   95 |
| MegaVul         | cpp        | CWE-287   |            1626 |                   94 |
| MegaVul         | cpp        | CWE-770   |            2019 |                   93 |
| MegaVul         | cpp        | CWE-284   |            1452 |                   93 |
| MegaVul         | cpp        | CWE-834   |            4158 |                   88 |
| MegaVul         | cpp        | CWE-310   |            1301 |                   80 |
| MegaVul         | cpp        | CWE-909   |            1327 |                   78 |
| MegaVul         | cpp        | CWE-74    |            2384 |                   73 |
| MegaVul         | cpp        | CWE-295   |            1944 |                   71 |
| MegaVul         | cpp        | CWE-269   |            1013 |                   70 |
| MegaVul         | cpp        | CWE-667   |            1421 |                   69 |
| MegaVul         | cpp        | CWE-17    |            1002 |                   65 |
| MegaVul         | cpp        | CWE-193   |             889 |                   64 |
| MegaVul         | cpp        | CWE-78    |            1296 |                   60 |
| MegaVul         | cpp        | CWE-459   |             660 |                   60 |
| MegaVul         | cpp        | CWE-404   |            1748 |                   59 |
| MegaVul         | cpp        | CWE-843   |            1093 |                   58 |
| MegaVul         | cpp        | CWE-754   |             930 |                   58 |
| MegaVul         | cpp        | CWE-79    |             914 |                   58 |
| MegaVul         | cpp        | CWE-732   |             829 |                   58 |
| MegaVul         | cpp        | CWE-19    |            1271 |                   55 |
| MegaVul         | cpp        | CWE-681   |             703 |                   51 |
| MegaVul         | cpp        | CWE-863   |            1229 |                   49 |
| MegaVul         | cpp        | CWE-755   |            1048 |                   42 |
| MegaVul         | cpp        | CWE-252   |             526 |                   42 |
| MegaVul         | cpp        | CWE-665   |            1032 |                   40 |
| MegaVul         | cpp        | CWE-89    |            1743 |                   37 |
| MegaVul         | cpp        | CWE-668   |             853 |                   35 |
| MegaVul         | cpp        | CWE-129   |             726 |                   34 |
| MegaVul         | cpp        | CWE-203   |             737 |                   33 |
| MegaVul         | cpp        | CWE-367   |             952 |                   32 |
| MegaVul         | cpp        | CWE-704   |             748 |                   32 |
| MegaVul         | cpp        | CWE-682   |             581 |                   32 |
| MegaVul         | cpp        | CWE-131   |             528 |                   32 |
| MegaVul         | cpp        | CWE-1284  |             368 |                   32 |
| MegaVul         | cpp        | CWE-330   |             504 |                   31 |
| MegaVul         | cpp        | CWE-862   |             459 |                   30 |
| MegaVul         | cpp        | CWE-354   |             445 |                   30 |
| MegaVul         | cpp        | CWE-763   |             439 |                   30 |
| MegaVul         | cpp        | CWE-134   |            1055 |                   28 |
| MegaVul         | cpp        | CWE-191   |             817 |                   27 |
| MegaVul         | cpp        | CWE-824   |             507 |                   25 |
| MegaVul         | cpp        | CWE-327   |             314 |                   25 |
| MegaVul         | cpp        | CWE-276   |             674 |                   24 |
| MegaVul         | cpp        | CWE-121   |             233 |                   23 |
| MegaVul         | cpp        | CWE-502   |             113 |                   22 |
| MegaVul         | cpp        | CWE-212   |             291 |                   21 |
| MegaVul         | cpp        | CWE-697   |             239 |                   21 |
| MegaVul         | cpp        | CWE-345   |             196 |                   20 |
| MegaVul         | cpp        | CWE-436   |             281 |                   19 |
| MegaVul         | cpp        | CWE-77    |             412 |                   18 |
| MegaVul         | cpp        | CWE-94    |             395 |                   18 |
| MegaVul         | cpp        | CWE-611   |             240 |                   18 |
| MegaVul         | cpp        | CWE-444   |             186 |                   18 |
| MegaVul         | cpp        | CWE-326   |             157 |                   18 |
| MegaVul         | cpp        | CWE-662   |             111 |                   18 |
| MegaVul         | cpp        | CWE-776   |              81 |                   18 |
| MegaVul         | cpp        | CWE-434   |             574 |                   16 |
| MegaVul         | cpp        | CWE-116   |             455 |                   15 |
| MegaVul         | cpp        | CWE-601   |             216 |                   15 |
| MegaVul         | cpp        | CWE-672   |              78 |                   13 |
| MegaVul         | cpp        | CWE-347   |             100 |                   12 |
| MegaVul         | cpp        | CWE-440   |             636 |                   11 |
| MegaVul         | cpp        | CWE-426   |             201 |                   10 |
| MegaVul         | cpp        | CWE-613   |              44 |                   10 |
| MegaVul         | cpp        | CWE-197   |              35 |                   10 |
| MegaVul         | cpp        | CWE-552   |             338 |                    9 |
| MegaVul         | cpp        | CWE-384   |             217 |                    9 |
| MegaVul         | cpp        | CWE-319   |             166 |                    9 |
| MegaVul         | cpp        | CWE-306   |             113 |                    9 |
| MegaVul         | cpp        | CWE-1021  |             501 |                    8 |
| MegaVul         | cpp        | CWE-346   |             232 |                    8 |
| MegaVul         | cpp        | CWE-670   |             170 |                    8 |
| MegaVul         | cpp        | CWE-388   |             123 |                    8 |
| MegaVul         | cpp        | CWE-918   |             103 |                    8 |
| MegaVul         | cpp        | CWE-290   |              79 |                    8 |
| MegaVul         | cpp        | CWE-913   |              46 |                    8 |
| MegaVul         | cpp        | CWE-428   |             106 |                    7 |
| MegaVul         | cpp        | CWE-911   |             102 |                    7 |
| MegaVul         | cpp        | CWE-532   |             127 |                    6 |
| MegaVul         | cpp        | CWE-90    |              91 |                    6 |
| MegaVul         | cpp        | CWE-407   |              59 |                    6 |
| MegaVul         | cpp        | CWE-331   |              38 |                    6 |
| MegaVul         | cpp        | CWE-18    |              36 |                    6 |
| MegaVul         | cpp        | CWE-385   |              18 |                    6 |
| MegaVul         | cpp        | CWE-693   |             328 |                    5 |
| MegaVul         | cpp        | CWE-680   |             143 |                    5 |
| MegaVul         | cpp        | CWE-823   |             114 |                    5 |
| MegaVul         | cpp        | CWE-1187  |              78 |                    5 |
| MegaVul         | cpp        | CWE-126   |              26 |                    5 |
| MegaVul         | cpp        | CWE-337   |              21 |                    5 |
| MegaVul         | cpp        | CWE-409   |              17 |                    5 |
| MegaVul         | cpp        | CWE-427   |             360 |                    4 |
| MegaVul         | cpp        | CWE-16    |             309 |                    4 |
| MegaVul         | cpp        | CWE-285   |             191 |                    4 |
| MegaVul         | cpp        | CWE-273   |             161 |                    4 |
| MegaVul         | cpp        | CWE-1077  |             100 |                    4 |
| MegaVul         | cpp        | CWE-522   |              67 |                    4 |
| MegaVul         | cpp        | CWE-626   |              55 |                    4 |
| MegaVul         | cpp        | CWE-88    |              28 |                    4 |
| MegaVul         | cpp        | CWE-338   |              22 |                    4 |
| MegaVul         | cpp        | CWE-241   |              21 |                    4 |
| MegaVul         | cpp        | CWE-1188  |             260 |                    3 |
| MegaVul         | cpp        | CWE-706   |             146 |                    3 |
| MegaVul         | cpp        | CWE-229   |             113 |                    3 |
| MegaVul         | cpp        | CWE-494   |              48 |                    3 |
| MegaVul         | cpp        | CWE-325   |              38 |                    3 |
| MegaVul         | cpp        | CWE-118   |              32 |                    3 |
| MegaVul         | cpp        | CWE-172   |              17 |                    3 |
| MegaVul         | cpp        | CWE-707   |              16 |                    3 |
| MegaVul         | cpp        | CWE-639   |             116 |                    2 |
| MegaVul         | cpp        | CWE-307   |              34 |                    2 |
| MegaVul         | cpp        | CWE-838   |              34 |                    2 |
| MegaVul         | cpp        | CWE-320   |              23 |                    2 |
| MegaVul         | cpp        | CWE-113   |              17 |                    2 |
| MegaVul         | cpp        | CWE-924   |              12 |                    2 |
| MegaVul         | cpp        | CWE-255   |               8 |                    2 |
| MegaVul         | cpp        | CWE-762   |               7 |                    2 |
| MegaVul         | cpp        | CWE-1333  |               3 |                    2 |
| MegaVul         | cpp        | CWE-250   |             587 |                    1 |
| MegaVul         | cpp        | CWE-312   |             187 |                    1 |
| MegaVul         | cpp        | CWE-460   |              89 |                    1 |
| MegaVul         | cpp        | CWE-1050  |              75 |                    1 |
| MegaVul         | cpp        | CWE-358   |              66 |                    1 |
| MegaVul         | cpp        | CWE-248   |              60 |                    1 |
| MegaVul         | cpp        | CWE-349   |              60 |                    1 |
| MegaVul         | cpp        | CWE-300   |              56 |                    1 |
| MegaVul         | cpp        | CWE-943   |              56 |                    1 |
| MegaVul         | cpp        | CWE-93    |              47 |                    1 |
| MegaVul         | cpp        | CWE-282   |              31 |                    1 |
| MegaVul         | cpp        | CWE-23    |              27 |                    1 |
| MegaVul         | cpp        | CWE-26    |              27 |                    1 |
| MegaVul         | cpp        | CWE-361   |              27 |                    1 |
| MegaVul         | cpp        | CWE-335   |              22 |                    1 |
| MegaVul         | cpp        | CWE-590   |              22 |                    1 |
| MegaVul         | cpp        | CWE-475   |              21 |                    1 |
| MegaVul         | cpp        | CWE-352   |              17 |                    1 |
| MegaVul         | cpp        | CWE-628   |              15 |                    1 |
| MegaVul         | cpp        | CWE-323   |              12 |                    1 |
| MegaVul         | cpp        | CWE-73    |              11 |                    1 |
| MegaVul         | cpp        | CWE-117   |               9 |                    1 |
| MegaVul         | cpp        | CWE-185   |               8 |                    1 |
| MegaVul         | cpp        | CWE-1049  |               7 |                    1 |
| MegaVul         | cpp        | CWE-610   |               7 |                    1 |
| MegaVul         | cpp        | CWE-202   |               3 |                    1 |
| MegaVul         | cpp        | CWE-324   |               2 |                    1 |
| MegaVul         | cpp        | CWE-209   |               1 |                    1 |
| MegaVul         | cpp        | CWE-788   |              22 |                    0 |
| MegaVul         | cpp        | CWE-208   |               5 |                    0 |
| Big-Vul         | cpp        | <MISSING> |           24363 |                 1473 |
| Big-Vul         | cpp        | CWE-119   |           13556 |                 1064 |
| Big-Vul         | cpp        | CWE-20    |           12631 |                  617 |
| Big-Vul         | cpp        | CWE-399   |            8627 |                  481 |
| Big-Vul         | cpp        | CWE-125   |            3256 |                  263 |
| Big-Vul         | cpp        | CWE-200   |            3835 |                  233 |
| Big-Vul         | cpp        | CWE-264   |            5460 |                  203 |
| Big-Vul         | cpp        | CWE-416   |            5717 |                  178 |
| Big-Vul         | cpp        | CWE-189   |            3128 |                  168 |
| Big-Vul         | cpp        | CWE-362   |            2593 |                  142 |
| Big-Vul         | cpp        | CWE-190   |            1920 |                  135 |
| Big-Vul         | cpp        | CWE-787   |            1592 |                  101 |
| Big-Vul         | cpp        | CWE-284   |            1279 |                   95 |
| Big-Vul         | cpp        | CWE-254   |            2094 |                   78 |
| Big-Vul         | cpp        | CWE-476   |            1891 |                   57 |
| Big-Vul         | cpp        | CWE-415   |             321 |                   42 |
| Big-Vul         | cpp        | CWE-310   |             602 |                   40 |
| Big-Vul         | cpp        | CWE-732   |            1119 |                   38 |
| Big-Vul         | cpp        | CWE-19    |             363 |                   37 |
| Big-Vul         | cpp        | CWE-404   |             700 |                   34 |
| Big-Vul         | cpp        | CWE-79    |             545 |                   32 |
| Big-Vul         | cpp        | CWE-22    |             479 |                   25 |
| Big-Vul         | cpp        | CWE-59    |             547 |                   22 |
| Big-Vul         | cpp        | CWE-285   |             369 |                   22 |
| Big-Vul         | cpp        | CWE-772   |             177 |                   21 |
| Big-Vul         | cpp        | CWE-835   |             440 |                   19 |
| Big-Vul         | cpp        | CWE-269   |             277 |                   18 |
| Big-Vul         | cpp        | CWE-134   |             547 |                   16 |
| Big-Vul         | cpp        | CWE-17    |             275 |                   16 |
| Big-Vul         | cpp        | CWE-311   |             164 |                   16 |
| Big-Vul         | cpp        | CWE-358   |              48 |                   14 |
| Big-Vul         | cpp        | CWE-704   |             475 |                   13 |
| Big-Vul         | cpp        | CWE-287   |             328 |                   12 |
| Big-Vul         | cpp        | CWE-369   |             275 |                   10 |
| Big-Vul         | cpp        | CWE-400   |             324 |                    9 |
| Big-Vul         | cpp        | CWE-94    |             152 |                    9 |
| Big-Vul         | cpp        | CWE-78    |             199 |                    8 |
| Big-Vul         | cpp        | CWE-617   |             723 |                    7 |
| Big-Vul         | cpp        | CWE-354   |              21 |                    7 |
| Big-Vul         | cpp        | CWE-18    |              20 |                    7 |
| Big-Vul         | cpp        | CWE-754   |             233 |                    6 |
| Big-Vul         | cpp        | CWE-320   |             110 |                    6 |
| Big-Vul         | cpp        | CWE-255   |              62 |                    6 |
| Big-Vul         | cpp        | CWE-281   |              39 |                    6 |
| Big-Vul         | cpp        | CWE-611   |             239 |                    5 |
| Big-Vul         | cpp        | CWE-120   |              45 |                    5 |
| Big-Vul         | cpp        | CWE-674   |              30 |                    5 |
| Big-Vul         | cpp        | CWE-388   |              93 |                    4 |
| Big-Vul         | cpp        | CWE-436   |              72 |                    4 |
| Big-Vul         | cpp        | CWE-770   |              36 |                    4 |
| Big-Vul         | cpp        | CWE-346   |              59 |                    3 |
| Big-Vul         | cpp        | CWE-295   |              57 |                    3 |
| Big-Vul         | cpp        | CWE-347   |              21 |                    3 |
| Big-Vul         | cpp        | CWE-77    |             100 |                    2 |
| Big-Vul         | cpp        | CWE-862   |              41 |                    2 |
| Big-Vul         | cpp        | CWE-601   |              37 |                    2 |
| Big-Vul         | cpp        | CWE-426   |              22 |                    2 |
| Big-Vul         | cpp        | CWE-522   |               6 |                    2 |
| Big-Vul         | cpp        | CWE-327   |               3 |                    2 |
| Big-Vul         | cpp        | CWE-682   |               3 |                    2 |
| Big-Vul         | cpp        | CWE-345   |               2 |                    2 |
| Big-Vul         | cpp        | CWE-532   |              67 |                    1 |
| Big-Vul         | cpp        | CWE-330   |              50 |                    1 |
| Big-Vul         | cpp        | CWE-1021  |              43 |                    1 |
| Big-Vul         | cpp        | CWE-834   |              33 |                    1 |
| Big-Vul         | cpp        | CWE-352   |              29 |                    1 |
| Big-Vul         | cpp        | CWE-502   |              21 |                    1 |
| Big-Vul         | cpp        | CWE-90    |              17 |                    1 |
| Big-Vul         | cpp        | CWE-755   |              14 |                    1 |
| Big-Vul         | cpp        | CWE-664   |              13 |                    1 |
| Big-Vul         | cpp        | CWE-74    |               9 |                    1 |
| Big-Vul         | cpp        | CWE-824   |               6 |                    1 |
| Big-Vul         | cpp        | CWE-209   |               1 |                    1 |
| Big-Vul         | cpp        | CWE-252   |               1 |                    1 |
| Big-Vul         | cpp        | CWE-93    |              91 |                    0 |
| Big-Vul         | cpp        | CWE-290   |              58 |                    0 |
| Big-Vul         | cpp        | CWE-89    |              47 |                    0 |
| Big-Vul         | cpp        | CWE-16    |              23 |                    0 |
| Big-Vul         | cpp        | CWE-668   |              20 |                    0 |
| Big-Vul         | cpp        | CWE-918   |              14 |                    0 |
| Big-Vul         | cpp        | CWE-706   |              12 |                    0 |
| Big-Vul         | cpp        | CWE-693   |              11 |                    0 |
| Big-Vul         | cpp        | CWE-191   |               7 |                    0 |
| Big-Vul         | cpp        | CWE-665   |               3 |                    0 |
| Big-Vul         | cpp        | CWE-769   |               3 |                    0 |
| Big-Vul         | cpp        | CWE-129   |               2 |                    0 |
| Big-Vul         | cpp        | CWE-172   |               2 |                    0 |
| Big-Vul         | cpp        | CWE-361   |               2 |                    0 |
| Big-Vul         | cpp        | CWE-494   |               2 |                    0 |
| Big-Vul         | cpp        | CWE-909   |               2 |                    0 |
| cvefixes_cpp    | cpp        | CWE-787   |             372 |                  372 |
| cvefixes_cpp    | cpp        | CWE-125   |             354 |                  354 |
| cvefixes_cpp    | cpp        | <MISSING> |            1696 |                  142 |
| cvefixes_cpp    | cpp        | CWE-284   |              52 |                   52 |
| cvefixes_cpp    | cpp        | CWE-190   |              40 |                   40 |
| cvefixes_cpp    | cpp        | CWE-20    |              40 |                   40 |
| cvefixes_cpp    | cpp        | CWE-843   |              38 |                   38 |
| cvefixes_cpp    | cpp        | CWE-22    |              32 |                   32 |
| cvefixes_cpp    | cpp        | CWE-476   |              25 |                   25 |
| cvefixes_cpp    | cpp        | CWE-617   |              24 |                   24 |
| cvefixes_cpp    | cpp        | CWE-120   |              23 |                   23 |
| cvefixes_cpp    | cpp        | CWE-416   |              21 |                   21 |
| cvefixes_cpp    | cpp        | CWE-362   |              17 |                   17 |
| cvefixes_cpp    | cpp        | CWE-835   |              17 |                   17 |
| cvefixes_cpp    | cpp        | CWE-200   |              14 |                   14 |
| cvefixes_cpp    | cpp        | CWE-776   |              14 |                   14 |
| cvefixes_cpp    | cpp        | CWE-119   |              13 |                   13 |
| cvefixes_cpp    | cpp        | CWE-400   |              11 |                   11 |
| cvefixes_cpp    | cpp        | CWE-59    |              10 |                   10 |
| cvefixes_cpp    | cpp        | CWE-330   |               8 |                    8 |
| cvefixes_cpp    | cpp        | CWE-415   |               7 |                    7 |
| cvefixes_cpp    | cpp        | CWE-287   |               6 |                    6 |
| cvefixes_cpp    | cpp        | CWE-681   |               6 |                    6 |
| cvefixes_cpp    | cpp        | CWE-347   |               5 |                    5 |
| cvefixes_cpp    | cpp        | CWE-369   |               5 |                    5 |
| cvefixes_cpp    | cpp        | CWE-122   |               3 |                    3 |
| cvefixes_cpp    | cpp        | CWE-290   |               3 |                    3 |
| cvefixes_cpp    | cpp        | CWE-295   |               3 |                    3 |
| cvefixes_cpp    | cpp        | CWE-354   |               3 |                    3 |
| cvefixes_cpp    | cpp        | CWE-401   |               3 |                    3 |
| cvefixes_cpp    | cpp        | CWE-670   |               3 |                    3 |
| cvefixes_cpp    | cpp        | CWE-674   |               3 |                    3 |
| cvefixes_cpp    | cpp        | CWE-754   |               3 |                    3 |
| cvefixes_cpp    | cpp        | CWE-755   |               3 |                    3 |
| cvefixes_cpp    | cpp        | CWE-913   |               3 |                    3 |
| cvefixes_cpp    | cpp        | CWE-131   |               2 |                    2 |
| cvefixes_cpp    | cpp        | CWE-189   |               2 |                    2 |
| cvefixes_cpp    | cpp        | CWE-384   |               2 |                    2 |
| cvefixes_cpp    | cpp        | CWE-502   |               2 |                    2 |
| cvefixes_cpp    | cpp        | CWE-668   |               2 |                    2 |
| cvefixes_cpp    | cpp        | CWE-763   |               2 |                    2 |
| cvefixes_cpp    | cpp        | CWE-77    |               2 |                    2 |
| cvefixes_cpp    | cpp        | CWE-770   |               2 |                    2 |
| cvefixes_cpp    | cpp        | CWE-78    |               2 |                    2 |
| cvefixes_cpp    | cpp        | CWE-79    |               2 |                    2 |
| cvefixes_cpp    | cpp        | CWE-824   |               2 |                    2 |
| cvefixes_cpp    | cpp        | CWE-116   |               1 |                    1 |
| cvefixes_cpp    | cpp        | CWE-134   |               1 |                    1 |
| cvefixes_cpp    | cpp        | CWE-241   |               1 |                    1 |
| cvefixes_cpp    | cpp        | CWE-252   |               1 |                    1 |
| cvefixes_cpp    | cpp        | CWE-269   |               1 |                    1 |
| cvefixes_cpp    | cpp        | CWE-345   |               1 |                    1 |
| cvefixes_cpp    | cpp        | CWE-399   |               1 |                    1 |
| cvefixes_cpp    | cpp        | CWE-404   |               1 |                    1 |
| cvefixes_cpp    | cpp        | CWE-444   |               1 |                    1 |
| cvefixes_cpp    | cpp        | CWE-613   |               1 |                    1 |
| cvefixes_cpp    | cpp        | CWE-672   |               1 |                    1 |
| cvefixes_cpp    | cpp        | CWE-704   |               1 |                    1 |
| cvefixes_cpp    | cpp        | CWE-772   |               1 |                    1 |
| cvefixes_cpp    | cpp        | CWE-823   |               1 |                    1 |
| cvefixes_cpp    | cpp        | CWE-908   |               1 |                    1 |
| cvefixes_python | python     | <MISSING> |            2433 |                  489 |
| cvefixes_python | python     | CWE-79    |             163 |                  163 |
| cvefixes_python | python     | CWE-918   |             161 |                  161 |
| cvefixes_python | python     | CWE-22    |             158 |                  158 |
| cvefixes_python | python     | CWE-601   |             130 |                  130 |
| cvefixes_python | python     | CWE-444   |             118 |                  118 |
| cvefixes_python | python     | CWE-613   |             104 |                  104 |
| cvefixes_python | python     | CWE-94    |              98 |                   98 |
| cvefixes_python | python     | CWE-20    |              79 |                   79 |
| cvefixes_python | python     | CWE-400   |              69 |                   69 |
| cvefixes_python | python     | CWE-200   |              68 |                   68 |
| cvefixes_python | python     | CWE-502   |              59 |                   59 |
| cvefixes_python | python     | CWE-352   |              50 |                   50 |
| cvefixes_python | python     | CWE-89    |              49 |                   49 |
| cvefixes_python | python     | CWE-287   |              45 |                   45 |
| cvefixes_python | python     | CWE-863   |              41 |                   41 |
| cvefixes_python | python     | CWE-78    |              39 |                   39 |
| cvefixes_python | python     | CWE-264   |              36 |                   36 |
| cvefixes_python | python     | CWE-770   |              35 |                   35 |
| cvefixes_python | python     | CWE-693   |              34 |                   34 |
| cvefixes_python | python     | CWE-59    |              32 |                   32 |
| cvefixes_python | python     | CWE-359   |              31 |                   31 |
| cvefixes_python | python     | CWE-269   |              30 |                   30 |
| cvefixes_python | python     | CWE-74    |              30 |                   30 |
| cvefixes_python | python     | CWE-29    |              27 |                   27 |
| cvefixes_python | python     | CWE-521   |              27 |                   27 |
| cvefixes_python | python     | CWE-125   |              23 |                   23 |
| cvefixes_python | python     | CWE-203   |              23 |                   23 |
| cvefixes_python | python     | CWE-312   |              23 |                   23 |
| cvefixes_python | python     | CWE-21    |              19 |                   19 |
| cvefixes_python | python     | CWE-436   |              17 |                   17 |
| cvefixes_python | python     | CWE-532   |              17 |                   17 |
| cvefixes_python | python     | CWE-611   |              16 |                   16 |
| cvefixes_python | python     | CWE-295   |              14 |                   14 |
| cvefixes_python | python     | CWE-755   |              14 |                   14 |
| cvefixes_python | python     | CWE-434   |              13 |                   13 |
| cvefixes_python | python     | CWE-77    |              13 |                   13 |
| cvefixes_python | python     | CWE-843   |              13 |                   13 |
| cvefixes_python | python     | CWE-362   |              12 |                   12 |
| cvefixes_python | python     | CWE-119   |              11 |                   11 |
| cvefixes_python | python     | CWE-190   |              11 |                   11 |
| cvefixes_python | python     | CWE-209   |              11 |                   11 |
| cvefixes_python | python     | CWE-116   |              10 |                   10 |
| cvefixes_python | python     | CWE-326   |              10 |                   10 |
| cvefixes_python | python     | CWE-367   |              10 |                   10 |
| cvefixes_python | python     | CWE-346   |               9 |                    9 |
| cvefixes_python | python     | CWE-617   |               9 |                    9 |
| cvefixes_python | python     | CWE-668   |               9 |                    9 |
| cvefixes_python | python     | CWE-1333  |               8 |                    8 |
| cvefixes_python | python     | CWE-311   |               8 |                    8 |
| cvefixes_python | python     | CWE-697   |               8 |                    8 |
| cvefixes_python | python     | CWE-862   |               8 |                    8 |
| cvefixes_python | python     | CWE-93    |               8 |                    8 |
| cvefixes_python | python     | CWE-290   |               7 |                    7 |
| cvefixes_python | python     | CWE-787   |               7 |                    7 |
| cvefixes_python | python     | CWE-835   |               7 |                    7 |
| cvefixes_python | python     | CWE-366   |               6 |                    6 |
| cvefixes_python | python     | CWE-670   |               6 |                    6 |
| cvefixes_python | python     | CWE-73    |               6 |                    6 |
| cvefixes_python | python     | CWE-921   |               6 |                    6 |
| cvefixes_python | python     | CWE-330   |               5 |                    5 |
| cvefixes_python | python     | CWE-331   |               5 |                    5 |
| cvefixes_python | python     | CWE-674   |               5 |                    5 |
| cvefixes_python | python     | CWE-684   |               5 |                    5 |
| cvefixes_python | python     | CWE-1188  |               4 |                    4 |
| cvefixes_python | python     | CWE-23    |               4 |                    4 |
| cvefixes_python | python     | CWE-254   |               4 |                    4 |
| cvefixes_python | python     | CWE-284   |               4 |                    4 |
| cvefixes_python | python     | CWE-347   |               4 |                    4 |
| cvefixes_python | python     | CWE-36    |               4 |                    4 |
| cvefixes_python | python     | CWE-667   |               4 |                    4 |
| cvefixes_python | python     | CWE-75    |               4 |                    4 |
| cvefixes_python | python     | CWE-776   |               4 |                    4 |
| cvefixes_python | python     | CWE-1021  |               3 |                    3 |
| cvefixes_python | python     | CWE-120   |               3 |                    3 |
| cvefixes_python | python     | CWE-193   |               3 |                    3 |
| cvefixes_python | python     | CWE-252   |               3 |                    3 |
| cvefixes_python | python     | CWE-285   |               3 |                    3 |
| cvefixes_python | python     | CWE-306   |               3 |                    3 |
| cvefixes_python | python     | CWE-310   |               3 |                    3 |
| cvefixes_python | python     | CWE-354   |               3 |                    3 |
| cvefixes_python | python     | CWE-416   |               3 |                    3 |
| cvefixes_python | python     | CWE-427   |               3 |                    3 |
| cvefixes_python | python     | CWE-476   |               3 |                    3 |
| cvefixes_python | python     | CWE-662   |               3 |                    3 |
| cvefixes_python | python     | CWE-682   |               3 |                    3 |
| cvefixes_python | python     | CWE-732   |               3 |                    3 |
| cvefixes_python | python     | CWE-789   |               3 |                    3 |
| cvefixes_python | python     | CWE-1236  |               2 |                    2 |
| cvefixes_python | python     | CWE-172   |               2 |                    2 |
| cvefixes_python | python     | CWE-19    |               2 |                    2 |
| cvefixes_python | python     | CWE-212   |               2 |                    2 |
| cvefixes_python | python     | CWE-255   |               2 |                    2 |
| cvefixes_python | python     | CWE-327   |               2 |                    2 |
| cvefixes_python | python     | CWE-369   |               2 |                    2 |
| cvefixes_python | python     | CWE-415   |               2 |                    2 |
| cvefixes_python | python     | CWE-522   |               2 |                    2 |
| cvefixes_python | python     | CWE-640   |               2 |                    2 |
| cvefixes_python | python     | CWE-88    |               2 |                    2 |
| cvefixes_python | python     | CWE-1336  |               1 |                    1 |
| cvefixes_python | python     | CWE-134   |               1 |                    1 |
| cvefixes_python | python     | CWE-377   |               1 |                    1 |
| cvefixes_python | python     | CWE-404   |               1 |                    1 |
| cvefixes_python | python     | CWE-440   |               1 |                    1 |
| cvefixes_python | python     | CWE-475   |               1 |                    1 |
| cvefixes_python | python     | CWE-534   |               1 |                    1 |
| cvefixes_python | python     | CWE-620   |               1 |                    1 |
| cvefixes_python | python     | CWE-707   |               1 |                    1 |
| cvefixes_python | python     | CWE-754   |               1 |                    1 |
| cvefixes_python | python     | CWE-80    |               1 |                    1 |
| cvefixes_python | python     | CWE-824   |               1 |                    1 |
| cvefixes_python | python     | CWE-98    |               1 |                    1 |

## 4. Label Noise Findings

Conflicting groups are groups where the same selected hash has more than one distinct label. They require manual review; a conflict alone does not prove that a label is wrong.

| Dataset | Conflict groups | Random groups exported | Review CSV |
|---|---:|---:|---|
| MegaVul | 0 | 0 | `None` |
| Big-Vul | 0 | 0 | `None` |
| cvefixes_cpp | 0 | 0 | `None` |
| cvefixes_python | 0 | 0 | `None` |

**Manual review status:** NOT COMPLETED BY THIS SCRIPT.

Open each review CSV, inspect the code, label, CWE, and source context, then record the manually confirmed findings here. Do not treat the number of conflicting groups as the number of confirmed label errors.

## 5. Cross-Dataset Overlap

| dataset_a    | dataset_b       |   unique_hashes_a |   unique_hashes_b |   shared_hashes |   overlap_pct_a |   overlap_pct_b |
|:-------------|:----------------|------------------:|------------------:|----------------:|----------------:|----------------:|
| MegaVul      | Big-Vul         |            336803 |            103345 |               0 |               0 |               0 |
| MegaVul      | cvefixes_cpp    |            336803 |              2628 |               0 |               0 |               0 |
| MegaVul      | cvefixes_python |            336803 |              4486 |               0 |               0 |               0 |
| Big-Vul      | cvefixes_cpp    |            103345 |              2628 |               0 |               0 |               0 |
| Big-Vul      | cvefixes_python |            103345 |              4486 |               0 |               0 |               0 |
| cvefixes_cpp | cvefixes_python |              2628 |              4486 |               0 |               0 |               0 |

Overlap is based on the selected hash column when present; otherwise, it is based on SHA-256 using the language-specific normalizers from the deduplication pipeline. For the final deduped files, zero shared hashes is expected because cross-dataset duplicates were removed during deduplication.

## 6. Recommended CWE List per Language

The table below ranks CWE groups by vulnerable sample count. It is a candidate list, not an automatic acceptance decision. Apply the project's official D22 threshold and verify the label convention before selecting CWE groups for downstream experiments.

| dataset         | language   | cwe      |   total_samples |   vulnerable_samples |   rank_within_dataset_language |
|:----------------|:-----------|:---------|----------------:|---------------------:|-------------------------------:|
| MegaVul         | cpp        | CWE-119  |           26405 |                 1589 |                              1 |
| MegaVul         | cpp        | CWE-787  |           28120 |                 1509 |                              2 |
| MegaVul         | cpp        | CWE-125  |           23577 |                 1443 |                              3 |
| MegaVul         | cpp        | CWE-476  |           26965 |                 1286 |                              4 |
| MegaVul         | cpp        | CWE-20   |           19448 |                 1070 |                              5 |
| Big-Vul         | cpp        | CWE-119  |           13556 |                 1064 |                              6 |
| MegaVul         | cpp        | CWE-416  |           24599 |                 1004 |                              7 |
| MegaVul         | cpp        | CWE-190  |           11781 |                  708 |                              8 |
| Big-Vul         | cpp        | CWE-20   |           12631 |                  617 |                              9 |
| MegaVul         | cpp        | CWE-200  |           11801 |                  560 |                             10 |
| MegaVul         | cpp        | CWE-362  |           10623 |                  509 |                             11 |
| Big-Vul         | cpp        | CWE-399  |            8627 |                  481 |                             12 |
| MegaVul         | cpp        | CWE-399  |            9985 |                  439 |                             13 |
| MegaVul         | cpp        | CWE-264  |            9541 |                  426 |                             14 |
| MegaVul         | cpp        | CWE-120  |            6657 |                  424 |                             15 |
| cvefixes_cpp    | cpp        | CWE-787  |             372 |                  372 |                             16 |
| cvefixes_cpp    | cpp        | CWE-125  |             354 |                  354 |                             17 |
| MegaVul         | cpp        | CWE-400  |            6223 |                  313 |                             18 |
| MegaVul         | cpp        | CWE-189  |            6005 |                  295 |                             19 |
| MegaVul         | cpp        | CWE-401  |           11501 |                  280 |                             20 |
| Big-Vul         | cpp        | CWE-125  |            3256 |                  263 |                             21 |
| MegaVul         | cpp        | CWE-617  |            4039 |                  260 |                             22 |
| MegaVul         | cpp        | CWE-835  |            5079 |                  251 |                             23 |
| Big-Vul         | cpp        | CWE-200  |            3835 |                  233 |                             24 |
| Big-Vul         | cpp        | CWE-264  |            5460 |                  203 |                             25 |
| MegaVul         | cpp        | CWE-415  |            6091 |                  184 |                             26 |
| Big-Vul         | cpp        | CWE-416  |            5717 |                  178 |                             27 |
| MegaVul         | cpp        | CWE-772  |            2974 |                  174 |                             28 |
| MegaVul         | cpp        | CWE-369  |            2496 |                  169 |                             29 |
| Big-Vul         | cpp        | CWE-189  |            3128 |                  168 |                             30 |
| MegaVul         | cpp        | CWE-22   |            3758 |                  155 |                             31 |
| Big-Vul         | cpp        | CWE-362  |            2593 |                  142 |                             32 |
| Big-Vul         | cpp        | CWE-190  |            1920 |                  135 |                             33 |
| MegaVul         | cpp        | CWE-254  |            2872 |                  128 |                             34 |
| MegaVul         | cpp        | CWE-674  |            1981 |                  120 |                             35 |
| MegaVul         | cpp        | CWE-122  |            2090 |                  115 |                             36 |
| MegaVul         | cpp        | CWE-908  |            1816 |                  102 |                             37 |
| Big-Vul         | cpp        | CWE-787  |            1592 |                  101 |                             38 |
| MegaVul         | cpp        | CWE-59   |            1747 |                   95 |                             39 |
| Big-Vul         | cpp        | CWE-284  |            1279 |                   95 |                             40 |
| MegaVul         | cpp        | CWE-287  |            1626 |                   94 |                             41 |
| MegaVul         | cpp        | CWE-770  |            2019 |                   93 |                             42 |
| MegaVul         | cpp        | CWE-284  |            1452 |                   93 |                             43 |
| MegaVul         | cpp        | CWE-834  |            4158 |                   88 |                             44 |
| MegaVul         | cpp        | CWE-310  |            1301 |                   80 |                             45 |
| MegaVul         | cpp        | CWE-909  |            1327 |                   78 |                             46 |
| Big-Vul         | cpp        | CWE-254  |            2094 |                   78 |                             47 |
| MegaVul         | cpp        | CWE-74   |            2384 |                   73 |                             48 |
| MegaVul         | cpp        | CWE-295  |            1944 |                   71 |                             49 |
| MegaVul         | cpp        | CWE-269  |            1013 |                   70 |                             50 |
| MegaVul         | cpp        | CWE-667  |            1421 |                   69 |                             51 |
| MegaVul         | cpp        | CWE-17   |            1002 |                   65 |                             52 |
| MegaVul         | cpp        | CWE-193  |             889 |                   64 |                             53 |
| MegaVul         | cpp        | CWE-78   |            1296 |                   60 |                             54 |
| MegaVul         | cpp        | CWE-459  |             660 |                   60 |                             55 |
| MegaVul         | cpp        | CWE-404  |            1748 |                   59 |                             56 |
| MegaVul         | cpp        | CWE-843  |            1093 |                   58 |                             57 |
| MegaVul         | cpp        | CWE-754  |             930 |                   58 |                             58 |
| MegaVul         | cpp        | CWE-79   |             914 |                   58 |                             59 |
| MegaVul         | cpp        | CWE-732  |             829 |                   58 |                             60 |
| Big-Vul         | cpp        | CWE-476  |            1891 |                   57 |                             61 |
| MegaVul         | cpp        | CWE-19   |            1271 |                   55 |                             62 |
| cvefixes_cpp    | cpp        | CWE-284  |              52 |                   52 |                             63 |
| MegaVul         | cpp        | CWE-681  |             703 |                   51 |                             64 |
| MegaVul         | cpp        | CWE-863  |            1229 |                   49 |                             65 |
| MegaVul         | cpp        | CWE-755  |            1048 |                   42 |                             66 |
| MegaVul         | cpp        | CWE-252  |             526 |                   42 |                             67 |
| Big-Vul         | cpp        | CWE-415  |             321 |                   42 |                             68 |
| MegaVul         | cpp        | CWE-665  |            1032 |                   40 |                             69 |
| Big-Vul         | cpp        | CWE-310  |             602 |                   40 |                             70 |
| cvefixes_cpp    | cpp        | CWE-190  |              40 |                   40 |                             71 |
| cvefixes_cpp    | cpp        | CWE-20   |              40 |                   40 |                             72 |
| Big-Vul         | cpp        | CWE-732  |            1119 |                   38 |                             73 |
| cvefixes_cpp    | cpp        | CWE-843  |              38 |                   38 |                             74 |
| MegaVul         | cpp        | CWE-89   |            1743 |                   37 |                             75 |
| Big-Vul         | cpp        | CWE-19   |             363 |                   37 |                             76 |
| MegaVul         | cpp        | CWE-668  |             853 |                   35 |                             77 |
| MegaVul         | cpp        | CWE-129  |             726 |                   34 |                             78 |
| Big-Vul         | cpp        | CWE-404  |             700 |                   34 |                             79 |
| MegaVul         | cpp        | CWE-203  |             737 |                   33 |                             80 |
| MegaVul         | cpp        | CWE-367  |             952 |                   32 |                             81 |
| MegaVul         | cpp        | CWE-704  |             748 |                   32 |                             82 |
| MegaVul         | cpp        | CWE-682  |             581 |                   32 |                             83 |
| MegaVul         | cpp        | CWE-131  |             528 |                   32 |                             84 |
| MegaVul         | cpp        | CWE-1284 |             368 |                   32 |                             85 |
| Big-Vul         | cpp        | CWE-79   |             545 |                   32 |                             86 |
| cvefixes_cpp    | cpp        | CWE-22   |              32 |                   32 |                             87 |
| MegaVul         | cpp        | CWE-330  |             504 |                   31 |                             88 |
| MegaVul         | cpp        | CWE-862  |             459 |                   30 |                             89 |
| MegaVul         | cpp        | CWE-354  |             445 |                   30 |                             90 |
| MegaVul         | cpp        | CWE-763  |             439 |                   30 |                             91 |
| MegaVul         | cpp        | CWE-134  |            1055 |                   28 |                             92 |
| MegaVul         | cpp        | CWE-191  |             817 |                   27 |                             93 |
| MegaVul         | cpp        | CWE-824  |             507 |                   25 |                             94 |
| MegaVul         | cpp        | CWE-327  |             314 |                   25 |                             95 |
| Big-Vul         | cpp        | CWE-22   |             479 |                   25 |                             96 |
| cvefixes_cpp    | cpp        | CWE-476  |              25 |                   25 |                             97 |
| MegaVul         | cpp        | CWE-276  |             674 |                   24 |                             98 |
| cvefixes_cpp    | cpp        | CWE-617  |              24 |                   24 |                             99 |
| MegaVul         | cpp        | CWE-121  |             233 |                   23 |                            100 |
| cvefixes_cpp    | cpp        | CWE-120  |              23 |                   23 |                            101 |
| MegaVul         | cpp        | CWE-502  |             113 |                   22 |                            102 |
| Big-Vul         | cpp        | CWE-59   |             547 |                   22 |                            103 |
| Big-Vul         | cpp        | CWE-285  |             369 |                   22 |                            104 |
| MegaVul         | cpp        | CWE-212  |             291 |                   21 |                            105 |
| MegaVul         | cpp        | CWE-697  |             239 |                   21 |                            106 |
| Big-Vul         | cpp        | CWE-772  |             177 |                   21 |                            107 |
| cvefixes_cpp    | cpp        | CWE-416  |              21 |                   21 |                            108 |
| MegaVul         | cpp        | CWE-345  |             196 |                   20 |                            109 |
| MegaVul         | cpp        | CWE-436  |             281 |                   19 |                            110 |
| Big-Vul         | cpp        | CWE-835  |             440 |                   19 |                            111 |
| MegaVul         | cpp        | CWE-77   |             412 |                   18 |                            112 |
| MegaVul         | cpp        | CWE-94   |             395 |                   18 |                            113 |
| MegaVul         | cpp        | CWE-611  |             240 |                   18 |                            114 |
| MegaVul         | cpp        | CWE-444  |             186 |                   18 |                            115 |
| MegaVul         | cpp        | CWE-326  |             157 |                   18 |                            116 |
| MegaVul         | cpp        | CWE-662  |             111 |                   18 |                            117 |
| MegaVul         | cpp        | CWE-776  |              81 |                   18 |                            118 |
| Big-Vul         | cpp        | CWE-269  |             277 |                   18 |                            119 |
| cvefixes_cpp    | cpp        | CWE-362  |              17 |                   17 |                            120 |
| cvefixes_cpp    | cpp        | CWE-835  |              17 |                   17 |                            121 |
| MegaVul         | cpp        | CWE-434  |             574 |                   16 |                            122 |
| Big-Vul         | cpp        | CWE-134  |             547 |                   16 |                            123 |
| Big-Vul         | cpp        | CWE-17   |             275 |                   16 |                            124 |
| Big-Vul         | cpp        | CWE-311  |             164 |                   16 |                            125 |
| MegaVul         | cpp        | CWE-116  |             455 |                   15 |                            126 |
| MegaVul         | cpp        | CWE-601  |             216 |                   15 |                            127 |
| Big-Vul         | cpp        | CWE-358  |              48 |                   14 |                            128 |
| cvefixes_cpp    | cpp        | CWE-200  |              14 |                   14 |                            129 |
| cvefixes_cpp    | cpp        | CWE-776  |              14 |                   14 |                            130 |
| MegaVul         | cpp        | CWE-672  |              78 |                   13 |                            131 |
| Big-Vul         | cpp        | CWE-704  |             475 |                   13 |                            132 |
| cvefixes_cpp    | cpp        | CWE-119  |              13 |                   13 |                            133 |
| MegaVul         | cpp        | CWE-347  |             100 |                   12 |                            134 |
| Big-Vul         | cpp        | CWE-287  |             328 |                   12 |                            135 |
| MegaVul         | cpp        | CWE-440  |             636 |                   11 |                            136 |
| cvefixes_cpp    | cpp        | CWE-400  |              11 |                   11 |                            137 |
| MegaVul         | cpp        | CWE-426  |             201 |                   10 |                            138 |
| MegaVul         | cpp        | CWE-613  |              44 |                   10 |                            139 |
| MegaVul         | cpp        | CWE-197  |              35 |                   10 |                            140 |
| Big-Vul         | cpp        | CWE-369  |             275 |                   10 |                            141 |
| cvefixes_cpp    | cpp        | CWE-59   |              10 |                   10 |                            142 |
| MegaVul         | cpp        | CWE-552  |             338 |                    9 |                            143 |
| MegaVul         | cpp        | CWE-384  |             217 |                    9 |                            144 |
| MegaVul         | cpp        | CWE-319  |             166 |                    9 |                            145 |
| MegaVul         | cpp        | CWE-306  |             113 |                    9 |                            146 |
| Big-Vul         | cpp        | CWE-400  |             324 |                    9 |                            147 |
| Big-Vul         | cpp        | CWE-94   |             152 |                    9 |                            148 |
| MegaVul         | cpp        | CWE-1021 |             501 |                    8 |                            149 |
| MegaVul         | cpp        | CWE-346  |             232 |                    8 |                            150 |
| MegaVul         | cpp        | CWE-670  |             170 |                    8 |                            151 |
| MegaVul         | cpp        | CWE-388  |             123 |                    8 |                            152 |
| MegaVul         | cpp        | CWE-918  |             103 |                    8 |                            153 |
| MegaVul         | cpp        | CWE-290  |              79 |                    8 |                            154 |
| MegaVul         | cpp        | CWE-913  |              46 |                    8 |                            155 |
| Big-Vul         | cpp        | CWE-78   |             199 |                    8 |                            156 |
| cvefixes_cpp    | cpp        | CWE-330  |               8 |                    8 |                            157 |
| MegaVul         | cpp        | CWE-428  |             106 |                    7 |                            158 |
| MegaVul         | cpp        | CWE-911  |             102 |                    7 |                            159 |
| Big-Vul         | cpp        | CWE-617  |             723 |                    7 |                            160 |
| Big-Vul         | cpp        | CWE-354  |              21 |                    7 |                            161 |
| Big-Vul         | cpp        | CWE-18   |              20 |                    7 |                            162 |
| cvefixes_cpp    | cpp        | CWE-415  |               7 |                    7 |                            163 |
| MegaVul         | cpp        | CWE-532  |             127 |                    6 |                            164 |
| MegaVul         | cpp        | CWE-90   |              91 |                    6 |                            165 |
| MegaVul         | cpp        | CWE-407  |              59 |                    6 |                            166 |
| MegaVul         | cpp        | CWE-331  |              38 |                    6 |                            167 |
| MegaVul         | cpp        | CWE-18   |              36 |                    6 |                            168 |
| MegaVul         | cpp        | CWE-385  |              18 |                    6 |                            169 |
| Big-Vul         | cpp        | CWE-754  |             233 |                    6 |                            170 |
| Big-Vul         | cpp        | CWE-320  |             110 |                    6 |                            171 |
| Big-Vul         | cpp        | CWE-255  |              62 |                    6 |                            172 |
| Big-Vul         | cpp        | CWE-281  |              39 |                    6 |                            173 |
| cvefixes_cpp    | cpp        | CWE-287  |               6 |                    6 |                            174 |
| cvefixes_cpp    | cpp        | CWE-681  |               6 |                    6 |                            175 |
| MegaVul         | cpp        | CWE-693  |             328 |                    5 |                            176 |
| MegaVul         | cpp        | CWE-680  |             143 |                    5 |                            177 |
| MegaVul         | cpp        | CWE-823  |             114 |                    5 |                            178 |
| MegaVul         | cpp        | CWE-1187 |              78 |                    5 |                            179 |
| MegaVul         | cpp        | CWE-126  |              26 |                    5 |                            180 |
| MegaVul         | cpp        | CWE-337  |              21 |                    5 |                            181 |
| MegaVul         | cpp        | CWE-409  |              17 |                    5 |                            182 |
| Big-Vul         | cpp        | CWE-611  |             239 |                    5 |                            183 |
| Big-Vul         | cpp        | CWE-120  |              45 |                    5 |                            184 |
| Big-Vul         | cpp        | CWE-674  |              30 |                    5 |                            185 |
| cvefixes_cpp    | cpp        | CWE-347  |               5 |                    5 |                            186 |
| cvefixes_cpp    | cpp        | CWE-369  |               5 |                    5 |                            187 |
| MegaVul         | cpp        | CWE-427  |             360 |                    4 |                            188 |
| MegaVul         | cpp        | CWE-16   |             309 |                    4 |                            189 |
| MegaVul         | cpp        | CWE-285  |             191 |                    4 |                            190 |
| MegaVul         | cpp        | CWE-273  |             161 |                    4 |                            191 |
| MegaVul         | cpp        | CWE-1077 |             100 |                    4 |                            192 |
| MegaVul         | cpp        | CWE-522  |              67 |                    4 |                            193 |
| MegaVul         | cpp        | CWE-626  |              55 |                    4 |                            194 |
| MegaVul         | cpp        | CWE-88   |              28 |                    4 |                            195 |
| MegaVul         | cpp        | CWE-338  |              22 |                    4 |                            196 |
| MegaVul         | cpp        | CWE-241  |              21 |                    4 |                            197 |
| Big-Vul         | cpp        | CWE-388  |              93 |                    4 |                            198 |
| Big-Vul         | cpp        | CWE-436  |              72 |                    4 |                            199 |
| Big-Vul         | cpp        | CWE-770  |              36 |                    4 |                            200 |
| MegaVul         | cpp        | CWE-1188 |             260 |                    3 |                            201 |
| MegaVul         | cpp        | CWE-706  |             146 |                    3 |                            202 |
| MegaVul         | cpp        | CWE-229  |             113 |                    3 |                            203 |
| MegaVul         | cpp        | CWE-494  |              48 |                    3 |                            204 |
| MegaVul         | cpp        | CWE-325  |              38 |                    3 |                            205 |
| MegaVul         | cpp        | CWE-118  |              32 |                    3 |                            206 |
| MegaVul         | cpp        | CWE-172  |              17 |                    3 |                            207 |
| MegaVul         | cpp        | CWE-707  |              16 |                    3 |                            208 |
| Big-Vul         | cpp        | CWE-346  |              59 |                    3 |                            209 |
| Big-Vul         | cpp        | CWE-295  |              57 |                    3 |                            210 |
| Big-Vul         | cpp        | CWE-347  |              21 |                    3 |                            211 |
| cvefixes_cpp    | cpp        | CWE-122  |               3 |                    3 |                            212 |
| cvefixes_cpp    | cpp        | CWE-290  |               3 |                    3 |                            213 |
| cvefixes_cpp    | cpp        | CWE-295  |               3 |                    3 |                            214 |
| cvefixes_cpp    | cpp        | CWE-354  |               3 |                    3 |                            215 |
| cvefixes_cpp    | cpp        | CWE-401  |               3 |                    3 |                            216 |
| cvefixes_cpp    | cpp        | CWE-670  |               3 |                    3 |                            217 |
| cvefixes_cpp    | cpp        | CWE-674  |               3 |                    3 |                            218 |
| cvefixes_cpp    | cpp        | CWE-754  |               3 |                    3 |                            219 |
| cvefixes_cpp    | cpp        | CWE-755  |               3 |                    3 |                            220 |
| cvefixes_cpp    | cpp        | CWE-913  |               3 |                    3 |                            221 |
| MegaVul         | cpp        | CWE-639  |             116 |                    2 |                            222 |
| MegaVul         | cpp        | CWE-307  |              34 |                    2 |                            223 |
| MegaVul         | cpp        | CWE-838  |              34 |                    2 |                            224 |
| MegaVul         | cpp        | CWE-320  |              23 |                    2 |                            225 |
| MegaVul         | cpp        | CWE-113  |              17 |                    2 |                            226 |
| MegaVul         | cpp        | CWE-924  |              12 |                    2 |                            227 |
| MegaVul         | cpp        | CWE-255  |               8 |                    2 |                            228 |
| MegaVul         | cpp        | CWE-762  |               7 |                    2 |                            229 |
| MegaVul         | cpp        | CWE-1333 |               3 |                    2 |                            230 |
| Big-Vul         | cpp        | CWE-77   |             100 |                    2 |                            231 |
| Big-Vul         | cpp        | CWE-862  |              41 |                    2 |                            232 |
| Big-Vul         | cpp        | CWE-601  |              37 |                    2 |                            233 |
| Big-Vul         | cpp        | CWE-426  |              22 |                    2 |                            234 |
| Big-Vul         | cpp        | CWE-522  |               6 |                    2 |                            235 |
| Big-Vul         | cpp        | CWE-327  |               3 |                    2 |                            236 |
| Big-Vul         | cpp        | CWE-682  |               3 |                    2 |                            237 |
| Big-Vul         | cpp        | CWE-345  |               2 |                    2 |                            238 |
| cvefixes_cpp    | cpp        | CWE-131  |               2 |                    2 |                            239 |
| cvefixes_cpp    | cpp        | CWE-189  |               2 |                    2 |                            240 |
| cvefixes_cpp    | cpp        | CWE-384  |               2 |                    2 |                            241 |
| cvefixes_cpp    | cpp        | CWE-502  |               2 |                    2 |                            242 |
| cvefixes_cpp    | cpp        | CWE-668  |               2 |                    2 |                            243 |
| cvefixes_cpp    | cpp        | CWE-763  |               2 |                    2 |                            244 |
| cvefixes_cpp    | cpp        | CWE-77   |               2 |                    2 |                            245 |
| cvefixes_cpp    | cpp        | CWE-770  |               2 |                    2 |                            246 |
| cvefixes_cpp    | cpp        | CWE-78   |               2 |                    2 |                            247 |
| cvefixes_cpp    | cpp        | CWE-79   |               2 |                    2 |                            248 |
| cvefixes_cpp    | cpp        | CWE-824  |               2 |                    2 |                            249 |
| MegaVul         | cpp        | CWE-250  |             587 |                    1 |                            250 |
| MegaVul         | cpp        | CWE-312  |             187 |                    1 |                            251 |
| MegaVul         | cpp        | CWE-460  |              89 |                    1 |                            252 |
| MegaVul         | cpp        | CWE-1050 |              75 |                    1 |                            253 |
| MegaVul         | cpp        | CWE-358  |              66 |                    1 |                            254 |
| MegaVul         | cpp        | CWE-248  |              60 |                    1 |                            255 |
| MegaVul         | cpp        | CWE-349  |              60 |                    1 |                            256 |
| MegaVul         | cpp        | CWE-300  |              56 |                    1 |                            257 |
| MegaVul         | cpp        | CWE-943  |              56 |                    1 |                            258 |
| MegaVul         | cpp        | CWE-93   |              47 |                    1 |                            259 |
| MegaVul         | cpp        | CWE-282  |              31 |                    1 |                            260 |
| MegaVul         | cpp        | CWE-23   |              27 |                    1 |                            261 |
| MegaVul         | cpp        | CWE-26   |              27 |                    1 |                            262 |
| MegaVul         | cpp        | CWE-361  |              27 |                    1 |                            263 |
| MegaVul         | cpp        | CWE-335  |              22 |                    1 |                            264 |
| MegaVul         | cpp        | CWE-590  |              22 |                    1 |                            265 |
| MegaVul         | cpp        | CWE-475  |              21 |                    1 |                            266 |
| MegaVul         | cpp        | CWE-352  |              17 |                    1 |                            267 |
| MegaVul         | cpp        | CWE-628  |              15 |                    1 |                            268 |
| MegaVul         | cpp        | CWE-323  |              12 |                    1 |                            269 |
| MegaVul         | cpp        | CWE-73   |              11 |                    1 |                            270 |
| MegaVul         | cpp        | CWE-117  |               9 |                    1 |                            271 |
| MegaVul         | cpp        | CWE-185  |               8 |                    1 |                            272 |
| MegaVul         | cpp        | CWE-1049 |               7 |                    1 |                            273 |
| MegaVul         | cpp        | CWE-610  |               7 |                    1 |                            274 |
| MegaVul         | cpp        | CWE-202  |               3 |                    1 |                            275 |
| MegaVul         | cpp        | CWE-324  |               2 |                    1 |                            276 |
| MegaVul         | cpp        | CWE-209  |               1 |                    1 |                            277 |
| Big-Vul         | cpp        | CWE-532  |              67 |                    1 |                            278 |
| Big-Vul         | cpp        | CWE-330  |              50 |                    1 |                            279 |
| Big-Vul         | cpp        | CWE-1021 |              43 |                    1 |                            280 |
| Big-Vul         | cpp        | CWE-834  |              33 |                    1 |                            281 |
| Big-Vul         | cpp        | CWE-352  |              29 |                    1 |                            282 |
| Big-Vul         | cpp        | CWE-502  |              21 |                    1 |                            283 |
| Big-Vul         | cpp        | CWE-90   |              17 |                    1 |                            284 |
| Big-Vul         | cpp        | CWE-755  |              14 |                    1 |                            285 |
| Big-Vul         | cpp        | CWE-664  |              13 |                    1 |                            286 |
| Big-Vul         | cpp        | CWE-74   |               9 |                    1 |                            287 |
| Big-Vul         | cpp        | CWE-824  |               6 |                    1 |                            288 |
| Big-Vul         | cpp        | CWE-209  |               1 |                    1 |                            289 |
| Big-Vul         | cpp        | CWE-252  |               1 |                    1 |                            290 |
| cvefixes_cpp    | cpp        | CWE-116  |               1 |                    1 |                            291 |
| cvefixes_cpp    | cpp        | CWE-134  |               1 |                    1 |                            292 |
| cvefixes_cpp    | cpp        | CWE-241  |               1 |                    1 |                            293 |
| cvefixes_cpp    | cpp        | CWE-252  |               1 |                    1 |                            294 |
| cvefixes_cpp    | cpp        | CWE-269  |               1 |                    1 |                            295 |
| cvefixes_cpp    | cpp        | CWE-345  |               1 |                    1 |                            296 |
| cvefixes_cpp    | cpp        | CWE-399  |               1 |                    1 |                            297 |
| cvefixes_cpp    | cpp        | CWE-404  |               1 |                    1 |                            298 |
| cvefixes_cpp    | cpp        | CWE-444  |               1 |                    1 |                            299 |
| cvefixes_cpp    | cpp        | CWE-613  |               1 |                    1 |                            300 |
| cvefixes_cpp    | cpp        | CWE-672  |               1 |                    1 |                            301 |
| cvefixes_cpp    | cpp        | CWE-704  |               1 |                    1 |                            302 |
| cvefixes_cpp    | cpp        | CWE-772  |               1 |                    1 |                            303 |
| cvefixes_cpp    | cpp        | CWE-823  |               1 |                    1 |                            304 |
| cvefixes_cpp    | cpp        | CWE-908  |               1 |                    1 |                            305 |
| MegaVul         | cpp        | CWE-788  |              22 |                    0 |                            306 |
| MegaVul         | cpp        | CWE-208  |               5 |                    0 |                            307 |
| Big-Vul         | cpp        | CWE-93   |              91 |                    0 |                            308 |
| Big-Vul         | cpp        | CWE-290  |              58 |                    0 |                            309 |
| Big-Vul         | cpp        | CWE-89   |              47 |                    0 |                            310 |
| Big-Vul         | cpp        | CWE-16   |              23 |                    0 |                            311 |
| Big-Vul         | cpp        | CWE-668  |              20 |                    0 |                            312 |
| Big-Vul         | cpp        | CWE-918  |              14 |                    0 |                            313 |
| Big-Vul         | cpp        | CWE-706  |              12 |                    0 |                            314 |
| Big-Vul         | cpp        | CWE-693  |              11 |                    0 |                            315 |
| Big-Vul         | cpp        | CWE-191  |               7 |                    0 |                            316 |
| Big-Vul         | cpp        | CWE-665  |               3 |                    0 |                            317 |
| Big-Vul         | cpp        | CWE-769  |               3 |                    0 |                            318 |
| Big-Vul         | cpp        | CWE-129  |               2 |                    0 |                            319 |
| Big-Vul         | cpp        | CWE-172  |               2 |                    0 |                            320 |
| Big-Vul         | cpp        | CWE-361  |               2 |                    0 |                            321 |
| Big-Vul         | cpp        | CWE-494  |               2 |                    0 |                            322 |
| Big-Vul         | cpp        | CWE-909  |               2 |                    0 |                            323 |
| cvefixes_python | python     | CWE-79   |             163 |                  163 |                              1 |
| cvefixes_python | python     | CWE-918  |             161 |                  161 |                              2 |
| cvefixes_python | python     | CWE-22   |             158 |                  158 |                              3 |
| cvefixes_python | python     | CWE-601  |             130 |                  130 |                              4 |
| cvefixes_python | python     | CWE-444  |             118 |                  118 |                              5 |
| cvefixes_python | python     | CWE-613  |             104 |                  104 |                              6 |
| cvefixes_python | python     | CWE-94   |              98 |                   98 |                              7 |
| cvefixes_python | python     | CWE-20   |              79 |                   79 |                              8 |
| cvefixes_python | python     | CWE-400  |              69 |                   69 |                              9 |
| cvefixes_python | python     | CWE-200  |              68 |                   68 |                             10 |
| cvefixes_python | python     | CWE-502  |              59 |                   59 |                             11 |
| cvefixes_python | python     | CWE-352  |              50 |                   50 |                             12 |
| cvefixes_python | python     | CWE-89   |              49 |                   49 |                             13 |
| cvefixes_python | python     | CWE-287  |              45 |                   45 |                             14 |
| cvefixes_python | python     | CWE-863  |              41 |                   41 |                             15 |
| cvefixes_python | python     | CWE-78   |              39 |                   39 |                             16 |
| cvefixes_python | python     | CWE-264  |              36 |                   36 |                             17 |
| cvefixes_python | python     | CWE-770  |              35 |                   35 |                             18 |
| cvefixes_python | python     | CWE-693  |              34 |                   34 |                             19 |
| cvefixes_python | python     | CWE-59   |              32 |                   32 |                             20 |
| cvefixes_python | python     | CWE-359  |              31 |                   31 |                             21 |
| cvefixes_python | python     | CWE-269  |              30 |                   30 |                             22 |
| cvefixes_python | python     | CWE-74   |              30 |                   30 |                             23 |
| cvefixes_python | python     | CWE-29   |              27 |                   27 |                             24 |
| cvefixes_python | python     | CWE-521  |              27 |                   27 |                             25 |
| cvefixes_python | python     | CWE-125  |              23 |                   23 |                             26 |
| cvefixes_python | python     | CWE-203  |              23 |                   23 |                             27 |
| cvefixes_python | python     | CWE-312  |              23 |                   23 |                             28 |
| cvefixes_python | python     | CWE-21   |              19 |                   19 |                             29 |
| cvefixes_python | python     | CWE-436  |              17 |                   17 |                             30 |
| cvefixes_python | python     | CWE-532  |              17 |                   17 |                             31 |
| cvefixes_python | python     | CWE-611  |              16 |                   16 |                             32 |
| cvefixes_python | python     | CWE-295  |              14 |                   14 |                             33 |
| cvefixes_python | python     | CWE-755  |              14 |                   14 |                             34 |
| cvefixes_python | python     | CWE-434  |              13 |                   13 |                             35 |
| cvefixes_python | python     | CWE-77   |              13 |                   13 |                             36 |
| cvefixes_python | python     | CWE-843  |              13 |                   13 |                             37 |
| cvefixes_python | python     | CWE-362  |              12 |                   12 |                             38 |
| cvefixes_python | python     | CWE-119  |              11 |                   11 |                             39 |
| cvefixes_python | python     | CWE-190  |              11 |                   11 |                             40 |
| cvefixes_python | python     | CWE-209  |              11 |                   11 |                             41 |
| cvefixes_python | python     | CWE-116  |              10 |                   10 |                             42 |
| cvefixes_python | python     | CWE-326  |              10 |                   10 |                             43 |
| cvefixes_python | python     | CWE-367  |              10 |                   10 |                             44 |
| cvefixes_python | python     | CWE-346  |               9 |                    9 |                             45 |
| cvefixes_python | python     | CWE-617  |               9 |                    9 |                             46 |
| cvefixes_python | python     | CWE-668  |               9 |                    9 |                             47 |
| cvefixes_python | python     | CWE-1333 |               8 |                    8 |                             48 |
| cvefixes_python | python     | CWE-311  |               8 |                    8 |                             49 |
| cvefixes_python | python     | CWE-697  |               8 |                    8 |                             50 |
| cvefixes_python | python     | CWE-862  |               8 |                    8 |                             51 |
| cvefixes_python | python     | CWE-93   |               8 |                    8 |                             52 |
| cvefixes_python | python     | CWE-290  |               7 |                    7 |                             53 |
| cvefixes_python | python     | CWE-787  |               7 |                    7 |                             54 |
| cvefixes_python | python     | CWE-835  |               7 |                    7 |                             55 |
| cvefixes_python | python     | CWE-366  |               6 |                    6 |                             56 |
| cvefixes_python | python     | CWE-670  |               6 |                    6 |                             57 |
| cvefixes_python | python     | CWE-73   |               6 |                    6 |                             58 |
| cvefixes_python | python     | CWE-921  |               6 |                    6 |                             59 |
| cvefixes_python | python     | CWE-330  |               5 |                    5 |                             60 |
| cvefixes_python | python     | CWE-331  |               5 |                    5 |                             61 |
| cvefixes_python | python     | CWE-674  |               5 |                    5 |                             62 |
| cvefixes_python | python     | CWE-684  |               5 |                    5 |                             63 |
| cvefixes_python | python     | CWE-1188 |               4 |                    4 |                             64 |
| cvefixes_python | python     | CWE-23   |               4 |                    4 |                             65 |
| cvefixes_python | python     | CWE-254  |               4 |                    4 |                             66 |
| cvefixes_python | python     | CWE-284  |               4 |                    4 |                             67 |
| cvefixes_python | python     | CWE-347  |               4 |                    4 |                             68 |
| cvefixes_python | python     | CWE-36   |               4 |                    4 |                             69 |
| cvefixes_python | python     | CWE-667  |               4 |                    4 |                             70 |
| cvefixes_python | python     | CWE-75   |               4 |                    4 |                             71 |
| cvefixes_python | python     | CWE-776  |               4 |                    4 |                             72 |
| cvefixes_python | python     | CWE-1021 |               3 |                    3 |                             73 |
| cvefixes_python | python     | CWE-120  |               3 |                    3 |                             74 |
| cvefixes_python | python     | CWE-193  |               3 |                    3 |                             75 |
| cvefixes_python | python     | CWE-252  |               3 |                    3 |                             76 |
| cvefixes_python | python     | CWE-285  |               3 |                    3 |                             77 |
| cvefixes_python | python     | CWE-306  |               3 |                    3 |                             78 |
| cvefixes_python | python     | CWE-310  |               3 |                    3 |                             79 |
| cvefixes_python | python     | CWE-354  |               3 |                    3 |                             80 |
| cvefixes_python | python     | CWE-416  |               3 |                    3 |                             81 |
| cvefixes_python | python     | CWE-427  |               3 |                    3 |                             82 |
| cvefixes_python | python     | CWE-476  |               3 |                    3 |                             83 |
| cvefixes_python | python     | CWE-662  |               3 |                    3 |                             84 |
| cvefixes_python | python     | CWE-682  |               3 |                    3 |                             85 |
| cvefixes_python | python     | CWE-732  |               3 |                    3 |                             86 |
| cvefixes_python | python     | CWE-789  |               3 |                    3 |                             87 |
| cvefixes_python | python     | CWE-1236 |               2 |                    2 |                             88 |
| cvefixes_python | python     | CWE-172  |               2 |                    2 |                             89 |
| cvefixes_python | python     | CWE-19   |               2 |                    2 |                             90 |
| cvefixes_python | python     | CWE-212  |               2 |                    2 |                             91 |
| cvefixes_python | python     | CWE-255  |               2 |                    2 |                             92 |
| cvefixes_python | python     | CWE-327  |               2 |                    2 |                             93 |
| cvefixes_python | python     | CWE-369  |               2 |                    2 |                             94 |
| cvefixes_python | python     | CWE-415  |               2 |                    2 |                             95 |
| cvefixes_python | python     | CWE-522  |               2 |                    2 |                             96 |
| cvefixes_python | python     | CWE-640  |               2 |                    2 |                             97 |
| cvefixes_python | python     | CWE-88   |               2 |                    2 |                             98 |
| cvefixes_python | python     | CWE-1336 |               1 |                    1 |                             99 |
| cvefixes_python | python     | CWE-134  |               1 |                    1 |                            100 |
| cvefixes_python | python     | CWE-377  |               1 |                    1 |                            101 |
| cvefixes_python | python     | CWE-404  |               1 |                    1 |                            102 |
| cvefixes_python | python     | CWE-440  |               1 |                    1 |                            103 |
| cvefixes_python | python     | CWE-475  |               1 |                    1 |                            104 |
| cvefixes_python | python     | CWE-534  |               1 |                    1 |                            105 |
| cvefixes_python | python     | CWE-620  |               1 |                    1 |                            106 |
| cvefixes_python | python     | CWE-707  |               1 |                    1 |                            107 |
| cvefixes_python | python     | CWE-754  |               1 |                    1 |                            108 |
| cvefixes_python | python     | CWE-80   |               1 |                    1 |                            109 |
| cvefixes_python | python     | CWE-824  |               1 |                    1 |                            110 |
| cvefixes_python | python     | CWE-98   |               1 |                    1 |                            111 |

## 7. Acceptance Verdict

| Dataset | Verdict | Reason |
|---|---|---|
| MegaVul | PRELIMINARY PASS | basic automated checks passed; official D22 thresholds and manual label-noise review still need confirmation |
| Big-Vul | PRELIMINARY PASS | basic automated checks passed; official D22 thresholds and manual label-noise review still need confirmation |
| cvefixes_cpp | PRELIMINARY PASS | basic automated checks passed; official D22 thresholds and manual label-noise review still need confirmation |
| cvefixes_python | PRELIMINARY PASS | basic automated checks passed; official D22 thresholds and manual label-noise review still need confirmation |

### Scope and Limitations

- Only MegaVul and Big-Vul were audited.
- This report does not provide a verdict for the other project datasets(python).
- Manual label-noise review is still required.
- Official D22 acceptance thresholds must be checked against project docs.
