c2csv.py
=====

AUTHOR:
Yash Chandra

LICENSE:
LGPLv1.0?

DESCRIPTION:
Python Utility to convert any data format into csv. The formats supported are:

1) XML
2) QFX
3) QBX

USAGE:
Usage: c2csv.py <input_filename> <output_filename> <error_filename>

PARAMETERS
-----------
input filename. <mandatory>
takes the format. possible values XML, QFX, QBX <mandatory>
delimiter. default is COMMA. possible values COMMA, SEMICOLON,COLON,PIPE <optional>
Output filename. default will be "c2csv_XML.csv", "c2csv_QFX.csv" etc.  <optional>
Error filename if any errors in utility execution. Default will be "c2csv_error_XML.csv" etc. <optional>

