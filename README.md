c2csv.py
=====
/*
AUTHOR:
Yash Chandra

LICENSE:
LGPL

DESCRIPTION:
Python Utility to convert any data format into csv. The formats supported are:

1) XML
2) QFX
3) QBX

USAGE:
Usage: c2csv.py -I <input_filename> -F XML -D COMMA -O <output_filename> -E <error_filename>

PARAMETERS
-I : input filename. <mandatory>
-F : takes the format. possible values XML, QFX, QBX <mandatory>
-D: delimiter. default is COMMA. possible values COMMA, SEMICOLON,COLON,PIPE <optional>
-O: Output filename. default will be "c2csv_XML.csv", "c2csv_QFX.csv" etc.  <optional>
-E: Error filename if any errors in utility execution. Default will be "c2csv_error_XML.csv" etc. <optional>
*/