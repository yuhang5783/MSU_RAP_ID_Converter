## MSU_RAP_ID_Converter
#### A simple script for rice biologists, which used to convert IDs between rice MSU7 and RAP reference genome.
#### The script is written in python3, please make sure python3 is correctly installed on you operating system.

### File description:

**RAP-MSU_2018-03-29.txt**: This file describe the ID corresponding relationship between rice MSU7 and RAP reference genome (Downloaded from the RAP-DB website https://rapdb.dna.affrc.go.jp/download/irgsp1.html)

**your-id-list-one-gene-per-line.txt**: Input your gene ID to this file.

**result.xls**: This file shows the results.

**msu2rap-converter.py**: Script used to convert gene ID from MSU7 to RAP.
```python3 msu2rap-converter.py your-id-list-one-gene-per-line.txt > result.xls```

**rap2msu-converter.py**: Script used to convert gene ID from RAP to MSU7.

```python3 rap2msu-converter.py your-id-list-one-gene-per-line.txt > result.xls```
