# Generated from grammar/SailingParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,161,493,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,5,0,78,8,0,10,
        0,12,0,81,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,104,8,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,123,8,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,137,8,2,1,3,1,
        3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,155,
        8,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,186,
        8,6,1,6,1,6,1,6,1,6,3,6,192,8,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,200,
        8,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,3,9,210,8,9,1,10,1,10,3,10,214,
        8,10,1,11,1,11,1,11,3,11,219,8,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,3,11,232,8,11,1,12,1,12,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,248,8,13,1,14,
        1,14,1,14,1,14,3,14,254,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,3,15,277,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,295,8,16,1,17,1,17,1,18,
        1,18,1,19,1,19,1,19,1,19,3,19,305,8,19,1,19,1,19,1,19,1,19,3,19,
        311,8,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,3,19,329,8,19,1,20,1,20,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,3,21,340,8,21,1,21,1,21,1,21,3,21,345,8,21,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,371,8,
        22,1,23,1,23,1,23,5,23,376,8,23,10,23,12,23,379,9,23,1,24,1,24,1,
        24,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,3,26,399,8,26,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,
        28,3,28,409,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,4,29,418,8,29,
        11,29,12,29,419,1,29,1,29,1,30,1,30,1,30,1,30,3,30,428,8,30,1,31,
        1,31,1,31,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,3,33,441,8,33,
        1,33,1,33,1,33,1,33,1,33,1,33,4,33,449,8,33,11,33,12,33,450,1,33,
        1,33,1,33,1,33,1,33,1,33,4,33,459,8,33,11,33,12,33,460,1,33,1,33,
        3,33,465,8,33,3,33,467,8,33,1,34,1,34,1,34,1,34,3,34,473,8,34,1,
        34,1,34,1,34,1,34,3,34,479,8,34,1,34,1,34,1,34,1,34,3,34,485,8,34,
        3,34,487,8,34,1,35,1,35,1,36,1,36,1,36,0,0,37,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,0,13,1,0,7,10,1,0,16,19,1,0,28,33,1,0,34,35,
        1,0,48,55,1,0,59,62,1,0,66,70,1,0,75,85,1,0,115,117,1,0,141,142,
        2,0,139,139,146,146,1,0,147,151,3,0,138,138,140,140,143,144,566,
        0,79,1,0,0,0,2,103,1,0,0,0,4,136,1,0,0,0,6,138,1,0,0,0,8,154,1,0,
        0,0,10,156,1,0,0,0,12,199,1,0,0,0,14,201,1,0,0,0,16,203,1,0,0,0,
        18,209,1,0,0,0,20,213,1,0,0,0,22,231,1,0,0,0,24,233,1,0,0,0,26,247,
        1,0,0,0,28,253,1,0,0,0,30,276,1,0,0,0,32,294,1,0,0,0,34,296,1,0,
        0,0,36,298,1,0,0,0,38,328,1,0,0,0,40,330,1,0,0,0,42,344,1,0,0,0,
        44,370,1,0,0,0,46,372,1,0,0,0,48,380,1,0,0,0,50,383,1,0,0,0,52,398,
        1,0,0,0,54,400,1,0,0,0,56,408,1,0,0,0,58,410,1,0,0,0,60,427,1,0,
        0,0,62,429,1,0,0,0,64,432,1,0,0,0,66,466,1,0,0,0,68,486,1,0,0,0,
        70,488,1,0,0,0,72,490,1,0,0,0,74,75,3,2,1,0,75,76,5,152,0,0,76,78,
        1,0,0,0,77,74,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,
        80,82,1,0,0,0,81,79,1,0,0,0,82,83,5,0,0,1,83,1,1,0,0,0,84,104,3,
        4,2,0,85,104,3,8,4,0,86,104,3,12,6,0,87,104,3,18,9,0,88,104,3,20,
        10,0,89,104,3,22,11,0,90,104,3,26,13,0,91,104,3,30,15,0,92,104,3,
        32,16,0,93,104,3,38,19,0,94,104,3,44,22,0,95,104,3,48,24,0,96,104,
        3,52,26,0,97,104,3,42,21,0,98,104,3,54,27,0,99,104,3,56,28,0,100,
        104,3,58,29,0,101,104,3,66,33,0,102,104,3,60,30,0,103,84,1,0,0,0,
        103,85,1,0,0,0,103,86,1,0,0,0,103,87,1,0,0,0,103,88,1,0,0,0,103,
        89,1,0,0,0,103,90,1,0,0,0,103,91,1,0,0,0,103,92,1,0,0,0,103,93,1,
        0,0,0,103,94,1,0,0,0,103,95,1,0,0,0,103,96,1,0,0,0,103,97,1,0,0,
        0,103,98,1,0,0,0,103,99,1,0,0,0,103,100,1,0,0,0,103,101,1,0,0,0,
        103,102,1,0,0,0,104,3,1,0,0,0,105,106,5,1,0,0,106,137,3,6,3,0,107,
        108,5,1,0,0,108,137,5,11,0,0,109,110,5,1,0,0,110,137,5,13,0,0,111,
        112,5,1,0,0,112,137,5,12,0,0,113,114,5,2,0,0,114,137,3,6,3,0,115,
        116,5,2,0,0,116,137,5,11,0,0,117,118,5,3,0,0,118,122,3,6,3,0,119,
        120,5,46,0,0,120,121,5,156,0,0,121,123,5,137,0,0,122,119,1,0,0,0,
        122,123,1,0,0,0,123,137,1,0,0,0,124,125,5,4,0,0,125,126,3,6,3,0,
        126,127,5,45,0,0,127,128,5,156,0,0,128,129,5,136,0,0,129,137,1,0,
        0,0,130,131,5,5,0,0,131,132,5,16,0,0,132,137,3,6,3,0,133,134,5,6,
        0,0,134,135,5,16,0,0,135,137,3,6,3,0,136,105,1,0,0,0,136,107,1,0,
        0,0,136,109,1,0,0,0,136,111,1,0,0,0,136,113,1,0,0,0,136,115,1,0,
        0,0,136,117,1,0,0,0,136,124,1,0,0,0,136,130,1,0,0,0,136,133,1,0,
        0,0,137,5,1,0,0,0,138,139,7,0,0,0,139,7,1,0,0,0,140,141,5,14,0,0,
        141,155,3,10,5,0,142,143,5,6,0,0,143,155,3,10,5,0,144,145,5,15,0,
        0,145,155,3,10,5,0,146,147,5,5,0,0,147,155,3,10,5,0,148,149,5,15,
        0,0,149,150,3,10,5,0,150,151,5,46,0,0,151,152,5,156,0,0,152,153,
        5,137,0,0,153,155,1,0,0,0,154,140,1,0,0,0,154,142,1,0,0,0,154,144,
        1,0,0,0,154,146,1,0,0,0,154,148,1,0,0,0,155,9,1,0,0,0,156,157,7,
        1,0,0,157,11,1,0,0,0,158,159,5,20,0,0,159,160,5,45,0,0,160,200,3,
        14,7,0,161,162,5,20,0,0,162,163,5,45,0,0,163,200,3,16,8,0,164,165,
        5,20,0,0,165,166,5,45,0,0,166,167,3,16,8,0,167,168,5,156,0,0,168,
        169,5,136,0,0,169,200,1,0,0,0,170,171,5,20,0,0,171,200,5,21,0,0,
        172,173,5,22,0,0,173,174,5,23,0,0,174,200,5,24,0,0,175,176,5,22,
        0,0,176,177,5,23,0,0,177,200,5,25,0,0,178,179,5,22,0,0,179,180,5,
        23,0,0,180,200,3,16,8,0,181,185,5,26,0,0,182,183,5,46,0,0,183,184,
        5,156,0,0,184,186,5,136,0,0,185,182,1,0,0,0,185,186,1,0,0,0,186,
        200,1,0,0,0,187,191,5,27,0,0,188,189,5,46,0,0,189,190,5,156,0,0,
        190,192,5,136,0,0,191,188,1,0,0,0,191,192,1,0,0,0,192,200,1,0,0,
        0,193,194,5,41,0,0,194,195,5,45,0,0,195,200,3,14,7,0,196,197,5,41,
        0,0,197,198,5,45,0,0,198,200,3,16,8,0,199,158,1,0,0,0,199,161,1,
        0,0,0,199,164,1,0,0,0,199,170,1,0,0,0,199,172,1,0,0,0,199,175,1,
        0,0,0,199,178,1,0,0,0,199,181,1,0,0,0,199,187,1,0,0,0,199,193,1,
        0,0,0,199,196,1,0,0,0,200,13,1,0,0,0,201,202,7,2,0,0,202,15,1,0,
        0,0,203,204,7,3,0,0,204,17,1,0,0,0,205,206,5,36,0,0,206,210,5,38,
        0,0,207,208,5,37,0,0,208,210,5,38,0,0,209,205,1,0,0,0,209,207,1,
        0,0,0,210,19,1,0,0,0,211,214,5,39,0,0,212,214,5,40,0,0,213,211,1,
        0,0,0,213,212,1,0,0,0,214,21,1,0,0,0,215,216,5,41,0,0,216,218,5,
        156,0,0,217,219,5,136,0,0,218,217,1,0,0,0,218,219,1,0,0,0,219,232,
        1,0,0,0,220,221,5,41,0,0,221,232,3,24,12,0,222,223,5,41,0,0,223,
        224,5,45,0,0,224,225,5,47,0,0,225,232,5,157,0,0,226,227,5,41,0,0,
        227,228,5,45,0,0,228,229,5,42,0,0,229,230,5,156,0,0,230,232,5,136,
        0,0,231,215,1,0,0,0,231,220,1,0,0,0,231,222,1,0,0,0,231,226,1,0,
        0,0,232,23,1,0,0,0,233,234,7,4,0,0,234,25,1,0,0,0,235,236,5,42,0,
        0,236,237,5,45,0,0,237,238,5,47,0,0,238,248,5,157,0,0,239,240,5,
        43,0,0,240,241,5,156,0,0,241,248,5,136,0,0,242,243,5,44,0,0,243,
        244,3,28,14,0,244,245,3,28,14,0,245,248,1,0,0,0,246,248,5,44,0,0,
        247,235,1,0,0,0,247,239,1,0,0,0,247,242,1,0,0,0,247,246,1,0,0,0,
        248,27,1,0,0,0,249,254,5,158,0,0,250,251,5,156,0,0,251,252,5,136,
        0,0,252,254,5,156,0,0,253,249,1,0,0,0,253,250,1,0,0,0,254,29,1,0,
        0,0,255,277,5,90,0,0,256,257,5,90,0,0,257,258,5,91,0,0,258,277,5,
        92,0,0,259,260,5,90,0,0,260,261,5,94,0,0,261,277,5,92,0,0,262,263,
        5,90,0,0,263,277,5,96,0,0,264,265,5,89,0,0,265,266,5,45,0,0,266,
        277,5,97,0,0,267,268,5,37,0,0,268,277,5,89,0,0,269,270,5,91,0,0,
        270,277,5,92,0,0,271,272,5,94,0,0,272,277,5,92,0,0,273,274,5,95,
        0,0,274,277,5,92,0,0,275,277,5,93,0,0,276,255,1,0,0,0,276,256,1,
        0,0,0,276,259,1,0,0,0,276,262,1,0,0,0,276,264,1,0,0,0,276,267,1,
        0,0,0,276,269,1,0,0,0,276,271,1,0,0,0,276,273,1,0,0,0,276,275,1,
        0,0,0,277,31,1,0,0,0,278,279,5,56,0,0,279,295,3,34,17,0,280,281,
        5,56,0,0,281,282,3,34,17,0,282,283,3,36,18,0,283,295,1,0,0,0,284,
        285,5,57,0,0,285,295,3,34,17,0,286,287,5,57,0,0,287,295,5,65,0,0,
        288,289,5,58,0,0,289,295,3,16,8,0,290,291,5,58,0,0,291,295,5,63,
        0,0,292,293,5,58,0,0,293,295,5,64,0,0,294,278,1,0,0,0,294,280,1,
        0,0,0,294,284,1,0,0,0,294,286,1,0,0,0,294,288,1,0,0,0,294,290,1,
        0,0,0,294,292,1,0,0,0,295,33,1,0,0,0,296,297,7,5,0,0,297,35,1,0,
        0,0,298,299,7,6,0,0,299,37,1,0,0,0,300,301,5,71,0,0,301,304,3,40,
        20,0,302,303,5,156,0,0,303,305,5,145,0,0,304,302,1,0,0,0,304,305,
        1,0,0,0,305,329,1,0,0,0,306,307,5,72,0,0,307,310,3,40,20,0,308,309,
        5,156,0,0,309,311,5,145,0,0,310,308,1,0,0,0,310,311,1,0,0,0,311,
        329,1,0,0,0,312,313,5,73,0,0,313,329,3,40,20,0,314,315,5,86,0,0,
        315,316,5,76,0,0,316,317,5,45,0,0,317,318,5,88,0,0,318,329,5,157,
        0,0,319,320,5,87,0,0,320,321,5,76,0,0,321,322,5,45,0,0,322,323,5,
        88,0,0,323,329,5,157,0,0,324,325,5,105,0,0,325,329,5,74,0,0,326,
        327,5,105,0,0,327,329,5,122,0,0,328,300,1,0,0,0,328,306,1,0,0,0,
        328,312,1,0,0,0,328,314,1,0,0,0,328,319,1,0,0,0,328,324,1,0,0,0,
        328,326,1,0,0,0,329,39,1,0,0,0,330,331,7,7,0,0,331,41,1,0,0,0,332,
        333,5,98,0,0,333,334,5,45,0,0,334,345,5,99,0,0,335,336,5,100,0,0,
        336,337,5,101,0,0,337,339,5,102,0,0,338,340,3,16,8,0,339,338,1,0,
        0,0,339,340,1,0,0,0,340,345,1,0,0,0,341,342,5,103,0,0,342,343,5,
        45,0,0,343,345,5,104,0,0,344,332,1,0,0,0,344,335,1,0,0,0,344,341,
        1,0,0,0,345,43,1,0,0,0,346,347,5,37,0,0,347,348,5,106,0,0,348,371,
        5,157,0,0,349,350,5,107,0,0,350,351,5,106,0,0,351,371,5,157,0,0,
        352,353,5,37,0,0,353,371,5,110,0,0,354,355,5,107,0,0,355,371,5,110,
        0,0,356,357,5,37,0,0,357,371,5,109,0,0,358,359,5,107,0,0,359,371,
        5,109,0,0,360,361,5,37,0,0,361,371,5,112,0,0,362,363,5,107,0,0,363,
        371,5,112,0,0,364,365,5,37,0,0,365,371,5,111,0,0,366,367,5,37,0,
        0,367,371,5,113,0,0,368,369,5,108,0,0,369,371,3,46,23,0,370,346,
        1,0,0,0,370,349,1,0,0,0,370,352,1,0,0,0,370,354,1,0,0,0,370,356,
        1,0,0,0,370,358,1,0,0,0,370,360,1,0,0,0,370,362,1,0,0,0,370,364,
        1,0,0,0,370,366,1,0,0,0,370,368,1,0,0,0,371,45,1,0,0,0,372,377,5,
        157,0,0,373,374,5,153,0,0,374,376,5,157,0,0,375,373,1,0,0,0,376,
        379,1,0,0,0,377,375,1,0,0,0,377,378,1,0,0,0,378,47,1,0,0,0,379,377,
        1,0,0,0,380,381,5,114,0,0,381,382,3,50,25,0,382,49,1,0,0,0,383,384,
        7,8,0,0,384,51,1,0,0,0,385,386,5,118,0,0,386,399,5,157,0,0,387,388,
        5,118,0,0,388,399,5,119,0,0,389,390,5,118,0,0,390,399,5,120,0,0,
        391,392,5,118,0,0,392,393,5,121,0,0,393,399,5,157,0,0,394,395,5,
        118,0,0,395,399,5,122,0,0,396,397,5,118,0,0,397,399,5,123,0,0,398,
        385,1,0,0,0,398,387,1,0,0,0,398,389,1,0,0,0,398,391,1,0,0,0,398,
        394,1,0,0,0,398,396,1,0,0,0,399,53,1,0,0,0,400,401,5,125,0,0,401,
        55,1,0,0,0,402,403,5,105,0,0,403,409,5,126,0,0,404,405,5,105,0,0,
        405,409,5,120,0,0,406,407,5,105,0,0,407,409,5,128,0,0,408,402,1,
        0,0,0,408,404,1,0,0,0,408,406,1,0,0,0,409,57,1,0,0,0,410,411,5,129,
        0,0,411,412,5,156,0,0,412,413,5,130,0,0,413,417,5,154,0,0,414,415,
        3,2,1,0,415,416,5,152,0,0,416,418,1,0,0,0,417,414,1,0,0,0,418,419,
        1,0,0,0,419,417,1,0,0,0,419,420,1,0,0,0,420,421,1,0,0,0,421,422,
        5,155,0,0,422,59,1,0,0,0,423,424,5,134,0,0,424,428,3,62,31,0,425,
        426,5,135,0,0,426,428,3,68,34,0,427,423,1,0,0,0,427,425,1,0,0,0,
        428,61,1,0,0,0,429,430,5,156,0,0,430,431,3,64,32,0,431,63,1,0,0,
        0,432,433,7,9,0,0,433,65,1,0,0,0,434,435,5,131,0,0,435,436,3,68,
        34,0,436,437,5,132,0,0,437,440,3,2,1,0,438,439,5,133,0,0,439,441,
        3,2,1,0,440,438,1,0,0,0,440,441,1,0,0,0,441,467,1,0,0,0,442,443,
        5,131,0,0,443,444,3,68,34,0,444,448,5,154,0,0,445,446,3,2,1,0,446,
        447,5,152,0,0,447,449,1,0,0,0,448,445,1,0,0,0,449,450,1,0,0,0,450,
        448,1,0,0,0,450,451,1,0,0,0,451,452,1,0,0,0,452,464,5,155,0,0,453,
        454,5,133,0,0,454,458,5,154,0,0,455,456,3,2,1,0,456,457,5,152,0,
        0,457,459,1,0,0,0,458,455,1,0,0,0,459,460,1,0,0,0,460,458,1,0,0,
        0,460,461,1,0,0,0,461,462,1,0,0,0,462,463,5,155,0,0,463,465,1,0,
        0,0,464,453,1,0,0,0,464,465,1,0,0,0,465,467,1,0,0,0,466,434,1,0,
        0,0,466,442,1,0,0,0,467,67,1,0,0,0,468,469,5,126,0,0,469,470,3,70,
        35,0,470,472,5,156,0,0,471,473,7,10,0,0,472,471,1,0,0,0,472,473,
        1,0,0,0,473,487,1,0,0,0,474,475,5,127,0,0,475,476,3,70,35,0,476,
        478,5,156,0,0,477,479,5,139,0,0,478,477,1,0,0,0,478,479,1,0,0,0,
        479,487,1,0,0,0,480,481,5,128,0,0,481,482,3,70,35,0,482,484,5,156,
        0,0,483,485,5,138,0,0,484,483,1,0,0,0,484,485,1,0,0,0,485,487,1,
        0,0,0,486,468,1,0,0,0,486,474,1,0,0,0,486,480,1,0,0,0,487,69,1,0,
        0,0,488,489,7,11,0,0,489,71,1,0,0,0,490,491,7,12,0,0,491,73,1,0,
        0,0,36,79,103,122,136,154,185,191,199,209,213,218,231,247,253,276,
        294,304,310,328,339,344,370,377,398,408,419,427,440,450,460,464,
        466,472,478,484,486
    ]

class SailingParser ( Parser ):

    grammarFileName = "SailingParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'postaw'", "<INVALID>", "'refuj'", "'ustaw'", 
                     "'wybierz'", "'luzuj'", "'grot'", "'fok'", "<INVALID>", 
                     "'sztaksel'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'dobij'", "<INVALID>", "'szoty'", "<INVALID>", "'brasy'", 
                     "'talrepy'", "'ster'", "'prosto'", "'zwrot'", "'przez'", 
                     "'sztag'", "<INVALID>", "'odpadaj'", "'ostrzej'", "'baksztag'", 
                     "'bejdewind'", "<INVALID>", "'fordewind'", "<INVALID>", 
                     "'ostry bejdewind'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'cumuj'", "'odcumuj'", "'kurs'", 
                     "'namiar'", "'peleng'", "'pozycja'", "'na'", "'do'", 
                     "'punkt'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'ognia'", "'salwa'", "'armaty'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'burta lewa'", "'burta prawa'", 
                     "<INVALID>", "<INVALID>", "'kartacz'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'skarb'", "<INVALID>", 
                     "'srebro'", "<INVALID>", "'prowiant'", "'rum'", "<INVALID>", 
                     "'proch'", "'beczki'", "'skrzynie'", "'zakop'", "'wykop'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'stop'", "'wolny'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'stanowiska'", "<INVALID>", 
                     "'za'", "<INVALID>", "'wszyscy'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'sygnalizuj'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'napraw'", "<INVALID>", "'maszt'", "'takielunek'", 
                     "'loguj'", "<INVALID>", "<INVALID>", "'zdarzenie'", 
                     "<INVALID>", "'stan jednostki'", "'alarm'", "'alarm bojowy'", 
                     "'wiatr'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'czekaj'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'beaufort'", 
                     "'>='", "'<='", "'>'", "'<'", "<INVALID>", "';'", "','", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "POSTAW", "ZWIN", "REFUJ", "USTAW", "WYBIERZ", 
                      "LUZUJ", "GROT", "FOK", "BEZANMESANA", "SZTAKSEL", 
                      "WSZYSTKIE_ZAGLE", "ZAGLE_SZTORMOWE", "PELNE_ZAGLE", 
                      "DOBIJ", "NAPIN", "SZOTY", "FALY", "BRASY", "TALREPY", 
                      "STER", "PROSTO", "ZWROT", "PRZEZ", "SZTAG", "RUFE", 
                      "ODPADAJ", "OSTRZEJ", "BAKSZTAG", "BEJDEWIND", "POLWIATR", 
                      "FORDEWIND", "POLBAKSZTAG", "OSTRY_BEJDEWIND", "LEWA_BURTA", 
                      "PRAWA_BURTA", "RZUC", "PODNIES", "KOTWICE", "CUMUJ", 
                      "ODCUMUJ", "KURS", "NAMIAR", "PELENG", "POZYCJA", 
                      "NA", "DO", "PUNKT", "POLNOC", "POLUDNIE", "WSCHOD", 
                      "ZACHOD", "POLNOCNY_WSCHOD", "POLNOCNY_ZACHOD", "POLUDNIOWY_WSCHOD", 
                      "POLUDNIOWY_ZACHOD", "LADUJ", "OGNIA", "SALWA", "ARMATY", 
                      "DZIALA", "KOLUBRYNA", "KARRONADA", "BURTA_LEWA", 
                      "BURTA_PRAWA", "WSZYSTKIE_DZIALA", "KULA", "KARTACZ", 
                      "LANCUCH_KULA", "ZAPALAJACA", "BOMBA", "ZALADUJ", 
                      "ROZLADUJ", "PRZELADUJ", "LADOWNIA", "LUPY", "SKARB", 
                      "ZLOTO", "SREBRO", "AMUNICJA", "PROWIANT", "RUM", 
                      "WODA_PITNA", "PROCH", "BECZKI", "SKRZYNIE", "ZAKOP", 
                      "WYKOP", "WYSPA", "WIOSLA", "WESLUJ", "CALA", "NAPRZOD", 
                      "STOP_KW", "WOLNY", "SREDNI", "WSTECZNY", "WODE", 
                      "ZALOGA", "STANOWISKA", "CZLOWIEK", "ZA", "BURTA", 
                      "WSZYSCY", "POKLAD", "RAPORT", "FLAGE", "OPUSC", "SYGNALIZUJ", 
                      "BANDERA", "JOLLY_ROGER", "FLAGA_HANDLOWA", "FALS_FLAGA", 
                      "FLAGA_BIALA", "NAPRAW", "KADLUB", "MASZT", "TAKIELUNEK", 
                      "LOGUJ", "POZYCJE", "POGODE", "ZDARZENIE", "STAN_LADOWNI", 
                      "STAN_JEDNOSTKI", "ALARM", "ALARM_BOJOWY", "WIATR", 
                      "PREDKOSC", "GLEBOKOSC", "POWTORZ", "RAZY", "JEZELI", 
                      "WTEDY", "INACZEJ", "CZEKAJ", "CZEKAJ_AZ", "STOPNI", 
                      "PROCENT", "METROW", "WEZLOW", "MIL_MORSKICH", "SEKUND", 
                      "MINUT", "KABELTOW", "JARDOW", "SZTUK", "BEAUFORT", 
                      "GTE", "LTE", "GT", "LT", "EQ", "SEMICOLON", "COMMA", 
                      "LBRACE", "RBRACE", "NUMBER", "STRING", "COORDINATE", 
                      "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_command = 1
    RULE_sailCommand = 2
    RULE_sail = 3
    RULE_riggingCommand = 4
    RULE_riggingElement = 5
    RULE_rudderCommand = 6
    RULE_windDirection = 7
    RULE_boardSide = 8
    RULE_anchorCommand = 9
    RULE_mooringCommand = 10
    RULE_courseCommand = 11
    RULE_compassPoint = 12
    RULE_navigationCommand = 13
    RULE_coordinate = 14
    RULE_speedCommand = 15
    RULE_combatCommand = 16
    RULE_cannonGroup = 17
    RULE_ammoType = 18
    RULE_cargoCommand = 19
    RULE_cargoType = 20
    RULE_crewCommand = 21
    RULE_flagCommand = 22
    RULE_flagSequence = 23
    RULE_repairCommand = 24
    RULE_repairTarget = 25
    RULE_logCommand = 26
    RULE_emergencyCommand = 27
    RULE_weatherQuery = 28
    RULE_repeatCommand = 29
    RULE_waitCommand = 30
    RULE_duration = 31
    RULE_timeUnit = 32
    RULE_conditionCommand = 33
    RULE_condition = 34
    RULE_compOp = 35
    RULE_unit = 36

    ruleNames =  [ "program", "command", "sailCommand", "sail", "riggingCommand", 
                   "riggingElement", "rudderCommand", "windDirection", "boardSide", 
                   "anchorCommand", "mooringCommand", "courseCommand", "compassPoint", 
                   "navigationCommand", "coordinate", "speedCommand", "combatCommand", 
                   "cannonGroup", "ammoType", "cargoCommand", "cargoType", 
                   "crewCommand", "flagCommand", "flagSequence", "repairCommand", 
                   "repairTarget", "logCommand", "emergencyCommand", "weatherQuery", 
                   "repeatCommand", "waitCommand", "duration", "timeUnit", 
                   "conditionCommand", "condition", "compOp", "unit" ]

    EOF = Token.EOF
    POSTAW=1
    ZWIN=2
    REFUJ=3
    USTAW=4
    WYBIERZ=5
    LUZUJ=6
    GROT=7
    FOK=8
    BEZANMESANA=9
    SZTAKSEL=10
    WSZYSTKIE_ZAGLE=11
    ZAGLE_SZTORMOWE=12
    PELNE_ZAGLE=13
    DOBIJ=14
    NAPIN=15
    SZOTY=16
    FALY=17
    BRASY=18
    TALREPY=19
    STER=20
    PROSTO=21
    ZWROT=22
    PRZEZ=23
    SZTAG=24
    RUFE=25
    ODPADAJ=26
    OSTRZEJ=27
    BAKSZTAG=28
    BEJDEWIND=29
    POLWIATR=30
    FORDEWIND=31
    POLBAKSZTAG=32
    OSTRY_BEJDEWIND=33
    LEWA_BURTA=34
    PRAWA_BURTA=35
    RZUC=36
    PODNIES=37
    KOTWICE=38
    CUMUJ=39
    ODCUMUJ=40
    KURS=41
    NAMIAR=42
    PELENG=43
    POZYCJA=44
    NA=45
    DO=46
    PUNKT=47
    POLNOC=48
    POLUDNIE=49
    WSCHOD=50
    ZACHOD=51
    POLNOCNY_WSCHOD=52
    POLNOCNY_ZACHOD=53
    POLUDNIOWY_WSCHOD=54
    POLUDNIOWY_ZACHOD=55
    LADUJ=56
    OGNIA=57
    SALWA=58
    ARMATY=59
    DZIALA=60
    KOLUBRYNA=61
    KARRONADA=62
    BURTA_LEWA=63
    BURTA_PRAWA=64
    WSZYSTKIE_DZIALA=65
    KULA=66
    KARTACZ=67
    LANCUCH_KULA=68
    ZAPALAJACA=69
    BOMBA=70
    ZALADUJ=71
    ROZLADUJ=72
    PRZELADUJ=73
    LADOWNIA=74
    LUPY=75
    SKARB=76
    ZLOTO=77
    SREBRO=78
    AMUNICJA=79
    PROWIANT=80
    RUM=81
    WODA_PITNA=82
    PROCH=83
    BECZKI=84
    SKRZYNIE=85
    ZAKOP=86
    WYKOP=87
    WYSPA=88
    WIOSLA=89
    WESLUJ=90
    CALA=91
    NAPRZOD=92
    STOP_KW=93
    WOLNY=94
    SREDNI=95
    WSTECZNY=96
    WODE=97
    ZALOGA=98
    STANOWISKA=99
    CZLOWIEK=100
    ZA=101
    BURTA=102
    WSZYSCY=103
    POKLAD=104
    RAPORT=105
    FLAGE=106
    OPUSC=107
    SYGNALIZUJ=108
    BANDERA=109
    JOLLY_ROGER=110
    FLAGA_HANDLOWA=111
    FALS_FLAGA=112
    FLAGA_BIALA=113
    NAPRAW=114
    KADLUB=115
    MASZT=116
    TAKIELUNEK=117
    LOGUJ=118
    POZYCJE=119
    POGODE=120
    ZDARZENIE=121
    STAN_LADOWNI=122
    STAN_JEDNOSTKI=123
    ALARM=124
    ALARM_BOJOWY=125
    WIATR=126
    PREDKOSC=127
    GLEBOKOSC=128
    POWTORZ=129
    RAZY=130
    JEZELI=131
    WTEDY=132
    INACZEJ=133
    CZEKAJ=134
    CZEKAJ_AZ=135
    STOPNI=136
    PROCENT=137
    METROW=138
    WEZLOW=139
    MIL_MORSKICH=140
    SEKUND=141
    MINUT=142
    KABELTOW=143
    JARDOW=144
    SZTUK=145
    BEAUFORT=146
    GTE=147
    LTE=148
    GT=149
    LT=150
    EQ=151
    SEMICOLON=152
    COMMA=153
    LBRACE=154
    RBRACE=155
    NUMBER=156
    STRING=157
    COORDINATE=158
    WS=159
    LINE_COMMENT=160
    BLOCK_COMMENT=161

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SailingParser.EOF, 0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SailingParser.CommandContext)
            else:
                return self.getTypedRuleContext(SailingParser.CommandContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(SailingParser.SEMICOLON)
            else:
                return self.getToken(SailingParser.SEMICOLON, i)

        def getRuleIndex(self):
            return SailingParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SailingParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 504437999246819454) != 0) or ((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & -7764055995669708793) != 0) or _la==135:
                self.state = 74
                self.command()
                self.state = 75
                self.match(SailingParser.SEMICOLON)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self.match(SailingParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sailCommand(self):
            return self.getTypedRuleContext(SailingParser.SailCommandContext,0)


        def riggingCommand(self):
            return self.getTypedRuleContext(SailingParser.RiggingCommandContext,0)


        def rudderCommand(self):
            return self.getTypedRuleContext(SailingParser.RudderCommandContext,0)


        def anchorCommand(self):
            return self.getTypedRuleContext(SailingParser.AnchorCommandContext,0)


        def mooringCommand(self):
            return self.getTypedRuleContext(SailingParser.MooringCommandContext,0)


        def courseCommand(self):
            return self.getTypedRuleContext(SailingParser.CourseCommandContext,0)


        def navigationCommand(self):
            return self.getTypedRuleContext(SailingParser.NavigationCommandContext,0)


        def speedCommand(self):
            return self.getTypedRuleContext(SailingParser.SpeedCommandContext,0)


        def combatCommand(self):
            return self.getTypedRuleContext(SailingParser.CombatCommandContext,0)


        def cargoCommand(self):
            return self.getTypedRuleContext(SailingParser.CargoCommandContext,0)


        def flagCommand(self):
            return self.getTypedRuleContext(SailingParser.FlagCommandContext,0)


        def repairCommand(self):
            return self.getTypedRuleContext(SailingParser.RepairCommandContext,0)


        def logCommand(self):
            return self.getTypedRuleContext(SailingParser.LogCommandContext,0)


        def crewCommand(self):
            return self.getTypedRuleContext(SailingParser.CrewCommandContext,0)


        def emergencyCommand(self):
            return self.getTypedRuleContext(SailingParser.EmergencyCommandContext,0)


        def weatherQuery(self):
            return self.getTypedRuleContext(SailingParser.WeatherQueryContext,0)


        def repeatCommand(self):
            return self.getTypedRuleContext(SailingParser.RepeatCommandContext,0)


        def conditionCommand(self):
            return self.getTypedRuleContext(SailingParser.ConditionCommandContext,0)


        def waitCommand(self):
            return self.getTypedRuleContext(SailingParser.WaitCommandContext,0)


        def getRuleIndex(self):
            return SailingParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = SailingParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.sailCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.riggingCommand()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.rudderCommand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.anchorCommand()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 88
                self.mooringCommand()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 89
                self.courseCommand()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 90
                self.navigationCommand()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 91
                self.speedCommand()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 92
                self.combatCommand()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 93
                self.cargoCommand()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 94
                self.flagCommand()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 95
                self.repairCommand()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 96
                self.logCommand()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 97
                self.crewCommand()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 98
                self.emergencyCommand()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 99
                self.weatherQuery()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 100
                self.repeatCommand()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 101
                self.conditionCommand()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 102
                self.waitCommand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SailCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_sailCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SetFullSailsContext(SailCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SailCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def POSTAW(self):
            return self.getToken(SailingParser.POSTAW, 0)
        def PELNE_ZAGLE(self):
            return self.getToken(SailingParser.PELNE_ZAGLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetFullSails" ):
                listener.enterSetFullSails(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetFullSails" ):
                listener.exitSetFullSails(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetFullSails" ):
                return visitor.visitSetFullSails(self)
            else:
                return visitor.visitChildren(self)


    class FurlSailContext(SailCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SailCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ZWIN(self):
            return self.getToken(SailingParser.ZWIN, 0)
        def sail(self):
            return self.getTypedRuleContext(SailingParser.SailContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFurlSail" ):
                listener.enterFurlSail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFurlSail" ):
                listener.exitFurlSail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFurlSail" ):
                return visitor.visitFurlSail(self)
            else:
                return visitor.visitChildren(self)


    class ReefSailContext(SailCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SailCommandContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def REFUJ(self):
            return self.getToken(SailingParser.REFUJ, 0)
        def sail(self):
            return self.getTypedRuleContext(SailingParser.SailContext,0)

        def DO(self):
            return self.getToken(SailingParser.DO, 0)
        def PROCENT(self):
            return self.getToken(SailingParser.PROCENT, 0)
        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReefSail" ):
                listener.enterReefSail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReefSail" ):
                listener.exitReefSail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReefSail" ):
                return visitor.visitReefSail(self)
            else:
                return visitor.visitChildren(self)


    class SetStormSailsContext(SailCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SailCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def POSTAW(self):
            return self.getToken(SailingParser.POSTAW, 0)
        def ZAGLE_SZTORMOWE(self):
            return self.getToken(SailingParser.ZAGLE_SZTORMOWE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetStormSails" ):
                listener.enterSetStormSails(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetStormSails" ):
                listener.exitSetStormSails(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetStormSails" ):
                return visitor.visitSetStormSails(self)
            else:
                return visitor.visitChildren(self)


    class SetAllSailsContext(SailCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SailCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def POSTAW(self):
            return self.getToken(SailingParser.POSTAW, 0)
        def WSZYSTKIE_ZAGLE(self):
            return self.getToken(SailingParser.WSZYSTKIE_ZAGLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetAllSails" ):
                listener.enterSetAllSails(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetAllSails" ):
                listener.exitSetAllSails(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetAllSails" ):
                return visitor.visitSetAllSails(self)
            else:
                return visitor.visitChildren(self)


    class SetSailContext(SailCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SailCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def POSTAW(self):
            return self.getToken(SailingParser.POSTAW, 0)
        def sail(self):
            return self.getTypedRuleContext(SailingParser.SailContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetSail" ):
                listener.enterSetSail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetSail" ):
                listener.exitSetSail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetSail" ):
                return visitor.visitSetSail(self)
            else:
                return visitor.visitChildren(self)


    class SetSailAngleContext(SailCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SailCommandContext
            super().__init__(parser)
            self.angle = None # Token
            self.copyFrom(ctx)

        def USTAW(self):
            return self.getToken(SailingParser.USTAW, 0)
        def sail(self):
            return self.getTypedRuleContext(SailingParser.SailContext,0)

        def NA(self):
            return self.getToken(SailingParser.NA, 0)
        def STOPNI(self):
            return self.getToken(SailingParser.STOPNI, 0)
        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetSailAngle" ):
                listener.enterSetSailAngle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetSailAngle" ):
                listener.exitSetSailAngle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetSailAngle" ):
                return visitor.visitSetSailAngle(self)
            else:
                return visitor.visitChildren(self)


    class FurlAllSailsContext(SailCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SailCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ZWIN(self):
            return self.getToken(SailingParser.ZWIN, 0)
        def WSZYSTKIE_ZAGLE(self):
            return self.getToken(SailingParser.WSZYSTKIE_ZAGLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFurlAllSails" ):
                listener.enterFurlAllSails(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFurlAllSails" ):
                listener.exitFurlAllSails(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFurlAllSails" ):
                return visitor.visitFurlAllSails(self)
            else:
                return visitor.visitChildren(self)


    class TrimSailContext(SailCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SailCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WYBIERZ(self):
            return self.getToken(SailingParser.WYBIERZ, 0)
        def SZOTY(self):
            return self.getToken(SailingParser.SZOTY, 0)
        def sail(self):
            return self.getTypedRuleContext(SailingParser.SailContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrimSail" ):
                listener.enterTrimSail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrimSail" ):
                listener.exitTrimSail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrimSail" ):
                return visitor.visitTrimSail(self)
            else:
                return visitor.visitChildren(self)


    class EaseSailContext(SailCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SailCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LUZUJ(self):
            return self.getToken(SailingParser.LUZUJ, 0)
        def SZOTY(self):
            return self.getToken(SailingParser.SZOTY, 0)
        def sail(self):
            return self.getTypedRuleContext(SailingParser.SailContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEaseSail" ):
                listener.enterEaseSail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEaseSail" ):
                listener.exitEaseSail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEaseSail" ):
                return visitor.visitEaseSail(self)
            else:
                return visitor.visitChildren(self)



    def sailCommand(self):

        localctx = SailingParser.SailCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sailCommand)
        self._la = 0 # Token type
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = SailingParser.SetSailContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(SailingParser.POSTAW)
                self.state = 106
                self.sail()
                pass

            elif la_ == 2:
                localctx = SailingParser.SetAllSailsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(SailingParser.POSTAW)
                self.state = 108
                self.match(SailingParser.WSZYSTKIE_ZAGLE)
                pass

            elif la_ == 3:
                localctx = SailingParser.SetFullSailsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.match(SailingParser.POSTAW)
                self.state = 110
                self.match(SailingParser.PELNE_ZAGLE)
                pass

            elif la_ == 4:
                localctx = SailingParser.SetStormSailsContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 111
                self.match(SailingParser.POSTAW)
                self.state = 112
                self.match(SailingParser.ZAGLE_SZTORMOWE)
                pass

            elif la_ == 5:
                localctx = SailingParser.FurlSailContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 113
                self.match(SailingParser.ZWIN)
                self.state = 114
                self.sail()
                pass

            elif la_ == 6:
                localctx = SailingParser.FurlAllSailsContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 115
                self.match(SailingParser.ZWIN)
                self.state = 116
                self.match(SailingParser.WSZYSTKIE_ZAGLE)
                pass

            elif la_ == 7:
                localctx = SailingParser.ReefSailContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 117
                self.match(SailingParser.REFUJ)
                self.state = 118
                self.sail()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 119
                    self.match(SailingParser.DO)
                    self.state = 120
                    localctx.value = self.match(SailingParser.NUMBER)
                    self.state = 121
                    self.match(SailingParser.PROCENT)


                pass

            elif la_ == 8:
                localctx = SailingParser.SetSailAngleContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 124
                self.match(SailingParser.USTAW)
                self.state = 125
                self.sail()
                self.state = 126
                self.match(SailingParser.NA)
                self.state = 127
                localctx.angle = self.match(SailingParser.NUMBER)
                self.state = 128
                self.match(SailingParser.STOPNI)
                pass

            elif la_ == 9:
                localctx = SailingParser.TrimSailContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 130
                self.match(SailingParser.WYBIERZ)
                self.state = 131
                self.match(SailingParser.SZOTY)
                self.state = 132
                self.sail()
                pass

            elif la_ == 10:
                localctx = SailingParser.EaseSailContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 133
                self.match(SailingParser.LUZUJ)
                self.state = 134
                self.match(SailingParser.SZOTY)
                self.state = 135
                self.sail()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROT(self):
            return self.getToken(SailingParser.GROT, 0)

        def FOK(self):
            return self.getToken(SailingParser.FOK, 0)

        def BEZANMESANA(self):
            return self.getToken(SailingParser.BEZANMESANA, 0)

        def SZTAKSEL(self):
            return self.getToken(SailingParser.SZTAKSEL, 0)

        def getRuleIndex(self):
            return SailingParser.RULE_sail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSail" ):
                listener.enterSail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSail" ):
                listener.exitSail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSail" ):
                return visitor.visitSail(self)
            else:
                return visitor.visitChildren(self)




    def sail(self):

        localctx = SailingParser.SailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RiggingCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_riggingCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TightenRiggingContext(RiggingCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RiggingCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DOBIJ(self):
            return self.getToken(SailingParser.DOBIJ, 0)
        def riggingElement(self):
            return self.getTypedRuleContext(SailingParser.RiggingElementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTightenRigging" ):
                listener.enterTightenRigging(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTightenRigging" ):
                listener.exitTightenRigging(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTightenRigging" ):
                return visitor.visitTightenRigging(self)
            else:
                return visitor.visitChildren(self)


    class TensionRiggingContext(RiggingCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RiggingCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAPIN(self):
            return self.getToken(SailingParser.NAPIN, 0)
        def riggingElement(self):
            return self.getTypedRuleContext(SailingParser.RiggingElementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTensionRigging" ):
                listener.enterTensionRigging(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTensionRigging" ):
                listener.exitTensionRigging(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTensionRigging" ):
                return visitor.visitTensionRigging(self)
            else:
                return visitor.visitChildren(self)


    class LoosenRiggingContext(RiggingCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RiggingCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LUZUJ(self):
            return self.getToken(SailingParser.LUZUJ, 0)
        def riggingElement(self):
            return self.getTypedRuleContext(SailingParser.RiggingElementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoosenRigging" ):
                listener.enterLoosenRigging(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoosenRigging" ):
                listener.exitLoosenRigging(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoosenRigging" ):
                return visitor.visitLoosenRigging(self)
            else:
                return visitor.visitChildren(self)


    class HaulRiggingContext(RiggingCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RiggingCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WYBIERZ(self):
            return self.getToken(SailingParser.WYBIERZ, 0)
        def riggingElement(self):
            return self.getTypedRuleContext(SailingParser.RiggingElementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHaulRigging" ):
                listener.enterHaulRigging(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHaulRigging" ):
                listener.exitHaulRigging(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHaulRigging" ):
                return visitor.visitHaulRigging(self)
            else:
                return visitor.visitChildren(self)


    class TensionRiggingPercentContext(RiggingCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RiggingCommandContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def NAPIN(self):
            return self.getToken(SailingParser.NAPIN, 0)
        def riggingElement(self):
            return self.getTypedRuleContext(SailingParser.RiggingElementContext,0)

        def DO(self):
            return self.getToken(SailingParser.DO, 0)
        def PROCENT(self):
            return self.getToken(SailingParser.PROCENT, 0)
        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTensionRiggingPercent" ):
                listener.enterTensionRiggingPercent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTensionRiggingPercent" ):
                listener.exitTensionRiggingPercent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTensionRiggingPercent" ):
                return visitor.visitTensionRiggingPercent(self)
            else:
                return visitor.visitChildren(self)



    def riggingCommand(self):

        localctx = SailingParser.RiggingCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_riggingCommand)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = SailingParser.TightenRiggingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(SailingParser.DOBIJ)
                self.state = 141
                self.riggingElement()
                pass

            elif la_ == 2:
                localctx = SailingParser.LoosenRiggingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(SailingParser.LUZUJ)
                self.state = 143
                self.riggingElement()
                pass

            elif la_ == 3:
                localctx = SailingParser.TensionRiggingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.match(SailingParser.NAPIN)
                self.state = 145
                self.riggingElement()
                pass

            elif la_ == 4:
                localctx = SailingParser.HaulRiggingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.match(SailingParser.WYBIERZ)
                self.state = 147
                self.riggingElement()
                pass

            elif la_ == 5:
                localctx = SailingParser.TensionRiggingPercentContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 148
                self.match(SailingParser.NAPIN)
                self.state = 149
                self.riggingElement()
                self.state = 150
                self.match(SailingParser.DO)
                self.state = 151
                localctx.value = self.match(SailingParser.NUMBER)
                self.state = 152
                self.match(SailingParser.PROCENT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RiggingElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FALY(self):
            return self.getToken(SailingParser.FALY, 0)

        def BRASY(self):
            return self.getToken(SailingParser.BRASY, 0)

        def TALREPY(self):
            return self.getToken(SailingParser.TALREPY, 0)

        def SZOTY(self):
            return self.getToken(SailingParser.SZOTY, 0)

        def getRuleIndex(self):
            return SailingParser.RULE_riggingElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRiggingElement" ):
                listener.enterRiggingElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRiggingElement" ):
                listener.exitRiggingElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRiggingElement" ):
                return visitor.visitRiggingElement(self)
            else:
                return visitor.visitChildren(self)




    def riggingElement(self):

        localctx = SailingParser.RiggingElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_riggingElement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RudderCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_rudderCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TackContext(RudderCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RudderCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ZWROT(self):
            return self.getToken(SailingParser.ZWROT, 0)
        def PRZEZ(self):
            return self.getToken(SailingParser.PRZEZ, 0)
        def SZTAG(self):
            return self.getToken(SailingParser.SZTAG, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTack" ):
                listener.enterTack(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTack" ):
                listener.exitTack(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTack" ):
                return visitor.visitTack(self)
            else:
                return visitor.visitChildren(self)


    class HeadUpContext(RudderCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RudderCommandContext
            super().__init__(parser)
            self.angle = None # Token
            self.copyFrom(ctx)

        def OSTRZEJ(self):
            return self.getToken(SailingParser.OSTRZEJ, 0)
        def DO(self):
            return self.getToken(SailingParser.DO, 0)
        def STOPNI(self):
            return self.getToken(SailingParser.STOPNI, 0)
        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeadUp" ):
                listener.enterHeadUp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeadUp" ):
                listener.exitHeadUp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeadUp" ):
                return visitor.visitHeadUp(self)
            else:
                return visitor.visitChildren(self)


    class CourseToWindDirContext(RudderCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RudderCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KURS(self):
            return self.getToken(SailingParser.KURS, 0)
        def NA(self):
            return self.getToken(SailingParser.NA, 0)
        def windDirection(self):
            return self.getTypedRuleContext(SailingParser.WindDirectionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCourseToWindDir" ):
                listener.enterCourseToWindDir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCourseToWindDir" ):
                listener.exitCourseToWindDir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCourseToWindDir" ):
                return visitor.visitCourseToWindDir(self)
            else:
                return visitor.visitChildren(self)


    class SteerWindDirectionContext(RudderCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RudderCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STER(self):
            return self.getToken(SailingParser.STER, 0)
        def NA(self):
            return self.getToken(SailingParser.NA, 0)
        def windDirection(self):
            return self.getTypedRuleContext(SailingParser.WindDirectionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSteerWindDirection" ):
                listener.enterSteerWindDirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSteerWindDirection" ):
                listener.exitSteerWindDirection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSteerWindDirection" ):
                return visitor.visitSteerWindDirection(self)
            else:
                return visitor.visitChildren(self)


    class SteerStraightContext(RudderCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RudderCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STER(self):
            return self.getToken(SailingParser.STER, 0)
        def PROSTO(self):
            return self.getToken(SailingParser.PROSTO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSteerStraight" ):
                listener.enterSteerStraight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSteerStraight" ):
                listener.exitSteerStraight(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSteerStraight" ):
                return visitor.visitSteerStraight(self)
            else:
                return visitor.visitChildren(self)


    class GybeContext(RudderCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RudderCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ZWROT(self):
            return self.getToken(SailingParser.ZWROT, 0)
        def PRZEZ(self):
            return self.getToken(SailingParser.PRZEZ, 0)
        def RUFE(self):
            return self.getToken(SailingParser.RUFE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGybe" ):
                listener.enterGybe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGybe" ):
                listener.exitGybe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGybe" ):
                return visitor.visitGybe(self)
            else:
                return visitor.visitChildren(self)


    class SteerBoardSideContext(RudderCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RudderCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STER(self):
            return self.getToken(SailingParser.STER, 0)
        def NA(self):
            return self.getToken(SailingParser.NA, 0)
        def boardSide(self):
            return self.getTypedRuleContext(SailingParser.BoardSideContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSteerBoardSide" ):
                listener.enterSteerBoardSide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSteerBoardSide" ):
                listener.exitSteerBoardSide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSteerBoardSide" ):
                return visitor.visitSteerBoardSide(self)
            else:
                return visitor.visitChildren(self)


    class SteerAngleContext(RudderCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RudderCommandContext
            super().__init__(parser)
            self.angle = None # Token
            self.copyFrom(ctx)

        def STER(self):
            return self.getToken(SailingParser.STER, 0)
        def NA(self):
            return self.getToken(SailingParser.NA, 0)
        def boardSide(self):
            return self.getTypedRuleContext(SailingParser.BoardSideContext,0)

        def STOPNI(self):
            return self.getToken(SailingParser.STOPNI, 0)
        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSteerAngle" ):
                listener.enterSteerAngle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSteerAngle" ):
                listener.exitSteerAngle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSteerAngle" ):
                return visitor.visitSteerAngle(self)
            else:
                return visitor.visitChildren(self)


    class TurnThroughSideContext(RudderCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RudderCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ZWROT(self):
            return self.getToken(SailingParser.ZWROT, 0)
        def PRZEZ(self):
            return self.getToken(SailingParser.PRZEZ, 0)
        def boardSide(self):
            return self.getTypedRuleContext(SailingParser.BoardSideContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTurnThroughSide" ):
                listener.enterTurnThroughSide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTurnThroughSide" ):
                listener.exitTurnThroughSide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTurnThroughSide" ):
                return visitor.visitTurnThroughSide(self)
            else:
                return visitor.visitChildren(self)


    class BearAwayContext(RudderCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RudderCommandContext
            super().__init__(parser)
            self.angle = None # Token
            self.copyFrom(ctx)

        def ODPADAJ(self):
            return self.getToken(SailingParser.ODPADAJ, 0)
        def DO(self):
            return self.getToken(SailingParser.DO, 0)
        def STOPNI(self):
            return self.getToken(SailingParser.STOPNI, 0)
        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBearAway" ):
                listener.enterBearAway(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBearAway" ):
                listener.exitBearAway(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBearAway" ):
                return visitor.visitBearAway(self)
            else:
                return visitor.visitChildren(self)


    class CourseToBoardSideContext(RudderCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RudderCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KURS(self):
            return self.getToken(SailingParser.KURS, 0)
        def NA(self):
            return self.getToken(SailingParser.NA, 0)
        def boardSide(self):
            return self.getTypedRuleContext(SailingParser.BoardSideContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCourseToBoardSide" ):
                listener.enterCourseToBoardSide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCourseToBoardSide" ):
                listener.exitCourseToBoardSide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCourseToBoardSide" ):
                return visitor.visitCourseToBoardSide(self)
            else:
                return visitor.visitChildren(self)



    def rudderCommand(self):

        localctx = SailingParser.RudderCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rudderCommand)
        self._la = 0 # Token type
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = SailingParser.SteerWindDirectionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(SailingParser.STER)
                self.state = 159
                self.match(SailingParser.NA)
                self.state = 160
                self.windDirection()
                pass

            elif la_ == 2:
                localctx = SailingParser.SteerBoardSideContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(SailingParser.STER)
                self.state = 162
                self.match(SailingParser.NA)
                self.state = 163
                self.boardSide()
                pass

            elif la_ == 3:
                localctx = SailingParser.SteerAngleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.match(SailingParser.STER)
                self.state = 165
                self.match(SailingParser.NA)
                self.state = 166
                self.boardSide()
                self.state = 167
                localctx.angle = self.match(SailingParser.NUMBER)
                self.state = 168
                self.match(SailingParser.STOPNI)
                pass

            elif la_ == 4:
                localctx = SailingParser.SteerStraightContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 170
                self.match(SailingParser.STER)
                self.state = 171
                self.match(SailingParser.PROSTO)
                pass

            elif la_ == 5:
                localctx = SailingParser.TackContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 172
                self.match(SailingParser.ZWROT)
                self.state = 173
                self.match(SailingParser.PRZEZ)
                self.state = 174
                self.match(SailingParser.SZTAG)
                pass

            elif la_ == 6:
                localctx = SailingParser.GybeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 175
                self.match(SailingParser.ZWROT)
                self.state = 176
                self.match(SailingParser.PRZEZ)
                self.state = 177
                self.match(SailingParser.RUFE)
                pass

            elif la_ == 7:
                localctx = SailingParser.TurnThroughSideContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 178
                self.match(SailingParser.ZWROT)
                self.state = 179
                self.match(SailingParser.PRZEZ)
                self.state = 180
                self.boardSide()
                pass

            elif la_ == 8:
                localctx = SailingParser.BearAwayContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 181
                self.match(SailingParser.ODPADAJ)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 182
                    self.match(SailingParser.DO)
                    self.state = 183
                    localctx.angle = self.match(SailingParser.NUMBER)
                    self.state = 184
                    self.match(SailingParser.STOPNI)


                pass

            elif la_ == 9:
                localctx = SailingParser.HeadUpContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 187
                self.match(SailingParser.OSTRZEJ)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 188
                    self.match(SailingParser.DO)
                    self.state = 189
                    localctx.angle = self.match(SailingParser.NUMBER)
                    self.state = 190
                    self.match(SailingParser.STOPNI)


                pass

            elif la_ == 10:
                localctx = SailingParser.CourseToWindDirContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 193
                self.match(SailingParser.KURS)
                self.state = 194
                self.match(SailingParser.NA)
                self.state = 195
                self.windDirection()
                pass

            elif la_ == 11:
                localctx = SailingParser.CourseToBoardSideContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 196
                self.match(SailingParser.KURS)
                self.state = 197
                self.match(SailingParser.NA)
                self.state = 198
                self.boardSide()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WindDirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BAKSZTAG(self):
            return self.getToken(SailingParser.BAKSZTAG, 0)

        def BEJDEWIND(self):
            return self.getToken(SailingParser.BEJDEWIND, 0)

        def OSTRY_BEJDEWIND(self):
            return self.getToken(SailingParser.OSTRY_BEJDEWIND, 0)

        def POLWIATR(self):
            return self.getToken(SailingParser.POLWIATR, 0)

        def FORDEWIND(self):
            return self.getToken(SailingParser.FORDEWIND, 0)

        def POLBAKSZTAG(self):
            return self.getToken(SailingParser.POLBAKSZTAG, 0)

        def getRuleIndex(self):
            return SailingParser.RULE_windDirection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWindDirection" ):
                listener.enterWindDirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWindDirection" ):
                listener.exitWindDirection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWindDirection" ):
                return visitor.visitWindDirection(self)
            else:
                return visitor.visitChildren(self)




    def windDirection(self):

        localctx = SailingParser.WindDirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_windDirection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16911433728) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoardSideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEWA_BURTA(self):
            return self.getToken(SailingParser.LEWA_BURTA, 0)

        def PRAWA_BURTA(self):
            return self.getToken(SailingParser.PRAWA_BURTA, 0)

        def getRuleIndex(self):
            return SailingParser.RULE_boardSide

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoardSide" ):
                listener.enterBoardSide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoardSide" ):
                listener.exitBoardSide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoardSide" ):
                return visitor.visitBoardSide(self)
            else:
                return visitor.visitChildren(self)




    def boardSide(self):

        localctx = SailingParser.BoardSideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_boardSide)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            _la = self._input.LA(1)
            if not(_la==34 or _la==35):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnchorCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_anchorCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DropAnchorContext(AnchorCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.AnchorCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RZUC(self):
            return self.getToken(SailingParser.RZUC, 0)
        def KOTWICE(self):
            return self.getToken(SailingParser.KOTWICE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDropAnchor" ):
                listener.enterDropAnchor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDropAnchor" ):
                listener.exitDropAnchor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDropAnchor" ):
                return visitor.visitDropAnchor(self)
            else:
                return visitor.visitChildren(self)


    class RaiseAnchorContext(AnchorCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.AnchorCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PODNIES(self):
            return self.getToken(SailingParser.PODNIES, 0)
        def KOTWICE(self):
            return self.getToken(SailingParser.KOTWICE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaiseAnchor" ):
                listener.enterRaiseAnchor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaiseAnchor" ):
                listener.exitRaiseAnchor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaiseAnchor" ):
                return visitor.visitRaiseAnchor(self)
            else:
                return visitor.visitChildren(self)



    def anchorCommand(self):

        localctx = SailingParser.AnchorCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_anchorCommand)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                localctx = SailingParser.DropAnchorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(SailingParser.RZUC)
                self.state = 206
                self.match(SailingParser.KOTWICE)
                pass
            elif token in [37]:
                localctx = SailingParser.RaiseAnchorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.match(SailingParser.PODNIES)
                self.state = 208
                self.match(SailingParser.KOTWICE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MooringCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_mooringCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MoorContext(MooringCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.MooringCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CUMUJ(self):
            return self.getToken(SailingParser.CUMUJ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoor" ):
                listener.enterMoor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoor" ):
                listener.exitMoor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoor" ):
                return visitor.visitMoor(self)
            else:
                return visitor.visitChildren(self)


    class CastOffContext(MooringCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.MooringCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ODCUMUJ(self):
            return self.getToken(SailingParser.ODCUMUJ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastOff" ):
                listener.enterCastOff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastOff" ):
                listener.exitCastOff(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastOff" ):
                return visitor.visitCastOff(self)
            else:
                return visitor.visitChildren(self)



    def mooringCommand(self):

        localctx = SailingParser.MooringCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_mooringCommand)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                localctx = SailingParser.MoorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(SailingParser.CUMUJ)
                pass
            elif token in [40]:
                localctx = SailingParser.CastOffContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(SailingParser.ODCUMUJ)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CourseCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_courseCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SetCourseWaypointContext(CourseCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CourseCommandContext
            super().__init__(parser)
            self.point = None # Token
            self.copyFrom(ctx)

        def KURS(self):
            return self.getToken(SailingParser.KURS, 0)
        def NA(self):
            return self.getToken(SailingParser.NA, 0)
        def PUNKT(self):
            return self.getToken(SailingParser.PUNKT, 0)
        def STRING(self):
            return self.getToken(SailingParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetCourseWaypoint" ):
                listener.enterSetCourseWaypoint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetCourseWaypoint" ):
                listener.exitSetCourseWaypoint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetCourseWaypoint" ):
                return visitor.visitSetCourseWaypoint(self)
            else:
                return visitor.visitChildren(self)


    class SetCourseNumericContext(CourseCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CourseCommandContext
            super().__init__(parser)
            self.angle = None # Token
            self.copyFrom(ctx)

        def KURS(self):
            return self.getToken(SailingParser.KURS, 0)
        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)
        def STOPNI(self):
            return self.getToken(SailingParser.STOPNI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetCourseNumeric" ):
                listener.enterSetCourseNumeric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetCourseNumeric" ):
                listener.exitSetCourseNumeric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetCourseNumeric" ):
                return visitor.visitSetCourseNumeric(self)
            else:
                return visitor.visitChildren(self)


    class SetCourseBearingContext(CourseCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CourseCommandContext
            super().__init__(parser)
            self.angle = None # Token
            self.copyFrom(ctx)

        def KURS(self):
            return self.getToken(SailingParser.KURS, 0)
        def NA(self):
            return self.getToken(SailingParser.NA, 0)
        def NAMIAR(self):
            return self.getToken(SailingParser.NAMIAR, 0)
        def STOPNI(self):
            return self.getToken(SailingParser.STOPNI, 0)
        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetCourseBearing" ):
                listener.enterSetCourseBearing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetCourseBearing" ):
                listener.exitSetCourseBearing(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetCourseBearing" ):
                return visitor.visitSetCourseBearing(self)
            else:
                return visitor.visitChildren(self)


    class SetCourseCompassContext(CourseCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CourseCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KURS(self):
            return self.getToken(SailingParser.KURS, 0)
        def compassPoint(self):
            return self.getTypedRuleContext(SailingParser.CompassPointContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetCourseCompass" ):
                listener.enterSetCourseCompass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetCourseCompass" ):
                listener.exitSetCourseCompass(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetCourseCompass" ):
                return visitor.visitSetCourseCompass(self)
            else:
                return visitor.visitChildren(self)



    def courseCommand(self):

        localctx = SailingParser.CourseCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_courseCommand)
        self._la = 0 # Token type
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = SailingParser.SetCourseNumericContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(SailingParser.KURS)
                self.state = 216
                localctx.angle = self.match(SailingParser.NUMBER)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==136:
                    self.state = 217
                    self.match(SailingParser.STOPNI)


                pass

            elif la_ == 2:
                localctx = SailingParser.SetCourseCompassContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(SailingParser.KURS)
                self.state = 221
                self.compassPoint()
                pass

            elif la_ == 3:
                localctx = SailingParser.SetCourseWaypointContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.match(SailingParser.KURS)
                self.state = 223
                self.match(SailingParser.NA)
                self.state = 224
                self.match(SailingParser.PUNKT)
                self.state = 225
                localctx.point = self.match(SailingParser.STRING)
                pass

            elif la_ == 4:
                localctx = SailingParser.SetCourseBearingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 226
                self.match(SailingParser.KURS)
                self.state = 227
                self.match(SailingParser.NA)
                self.state = 228
                self.match(SailingParser.NAMIAR)
                self.state = 229
                localctx.angle = self.match(SailingParser.NUMBER)
                self.state = 230
                self.match(SailingParser.STOPNI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompassPointContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POLNOC(self):
            return self.getToken(SailingParser.POLNOC, 0)

        def POLUDNIE(self):
            return self.getToken(SailingParser.POLUDNIE, 0)

        def WSCHOD(self):
            return self.getToken(SailingParser.WSCHOD, 0)

        def ZACHOD(self):
            return self.getToken(SailingParser.ZACHOD, 0)

        def POLNOCNY_WSCHOD(self):
            return self.getToken(SailingParser.POLNOCNY_WSCHOD, 0)

        def POLNOCNY_ZACHOD(self):
            return self.getToken(SailingParser.POLNOCNY_ZACHOD, 0)

        def POLUDNIOWY_WSCHOD(self):
            return self.getToken(SailingParser.POLUDNIOWY_WSCHOD, 0)

        def POLUDNIOWY_ZACHOD(self):
            return self.getToken(SailingParser.POLUDNIOWY_ZACHOD, 0)

        def getRuleIndex(self):
            return SailingParser.RULE_compassPoint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompassPoint" ):
                listener.enterCompassPoint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompassPoint" ):
                listener.exitCompassPoint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompassPoint" ):
                return visitor.visitCompassPoint(self)
            else:
                return visitor.visitChildren(self)




    def compassPoint(self):

        localctx = SailingParser.CompassPointContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_compassPoint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 71776119061217280) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NavigationCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_navigationCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BearingToPointContext(NavigationCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.NavigationCommandContext
            super().__init__(parser)
            self.point = None # Token
            self.copyFrom(ctx)

        def NAMIAR(self):
            return self.getToken(SailingParser.NAMIAR, 0)
        def NA(self):
            return self.getToken(SailingParser.NA, 0)
        def PUNKT(self):
            return self.getToken(SailingParser.PUNKT, 0)
        def STRING(self):
            return self.getToken(SailingParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBearingToPoint" ):
                listener.enterBearingToPoint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBearingToPoint" ):
                listener.exitBearingToPoint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBearingToPoint" ):
                return visitor.visitBearingToPoint(self)
            else:
                return visitor.visitChildren(self)


    class SetBearingContext(NavigationCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.NavigationCommandContext
            super().__init__(parser)
            self.angle = None # Token
            self.copyFrom(ctx)

        def PELENG(self):
            return self.getToken(SailingParser.PELENG, 0)
        def STOPNI(self):
            return self.getToken(SailingParser.STOPNI, 0)
        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetBearing" ):
                listener.enterSetBearing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetBearing" ):
                listener.exitSetBearing(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetBearing" ):
                return visitor.visitSetBearing(self)
            else:
                return visitor.visitChildren(self)


    class ReportPositionContext(NavigationCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.NavigationCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def POZYCJA(self):
            return self.getToken(SailingParser.POZYCJA, 0)
        def coordinate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SailingParser.CoordinateContext)
            else:
                return self.getTypedRuleContext(SailingParser.CoordinateContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReportPosition" ):
                listener.enterReportPosition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReportPosition" ):
                listener.exitReportPosition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReportPosition" ):
                return visitor.visitReportPosition(self)
            else:
                return visitor.visitChildren(self)


    class RequestPositionContext(NavigationCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.NavigationCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def POZYCJA(self):
            return self.getToken(SailingParser.POZYCJA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequestPosition" ):
                listener.enterRequestPosition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequestPosition" ):
                listener.exitRequestPosition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequestPosition" ):
                return visitor.visitRequestPosition(self)
            else:
                return visitor.visitChildren(self)



    def navigationCommand(self):

        localctx = SailingParser.NavigationCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_navigationCommand)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = SailingParser.BearingToPointContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(SailingParser.NAMIAR)
                self.state = 236
                self.match(SailingParser.NA)
                self.state = 237
                self.match(SailingParser.PUNKT)
                self.state = 238
                localctx.point = self.match(SailingParser.STRING)
                pass

            elif la_ == 2:
                localctx = SailingParser.SetBearingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(SailingParser.PELENG)
                self.state = 240
                localctx.angle = self.match(SailingParser.NUMBER)
                self.state = 241
                self.match(SailingParser.STOPNI)
                pass

            elif la_ == 3:
                localctx = SailingParser.ReportPositionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.match(SailingParser.POZYCJA)
                self.state = 243
                self.coordinate()
                self.state = 244
                self.coordinate()
                pass

            elif la_ == 4:
                localctx = SailingParser.RequestPositionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.match(SailingParser.POZYCJA)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordinateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COORDINATE(self):
            return self.getToken(SailingParser.COORDINATE, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(SailingParser.NUMBER)
            else:
                return self.getToken(SailingParser.NUMBER, i)

        def STOPNI(self):
            return self.getToken(SailingParser.STOPNI, 0)

        def getRuleIndex(self):
            return SailingParser.RULE_coordinate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordinate" ):
                listener.enterCoordinate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordinate" ):
                listener.exitCoordinate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoordinate" ):
                return visitor.visitCoordinate(self)
            else:
                return visitor.visitChildren(self)




    def coordinate(self):

        localctx = SailingParser.CoordinateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_coordinate)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [158]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(SailingParser.COORDINATE)
                pass
            elif token in [156]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(SailingParser.NUMBER)
                self.state = 251
                self.match(SailingParser.STOPNI)
                self.state = 252
                self.match(SailingParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpeedCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_speedCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FullAheadContext(SpeedCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SpeedCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CALA(self):
            return self.getToken(SailingParser.CALA, 0)
        def NAPRZOD(self):
            return self.getToken(SailingParser.NAPRZOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFullAhead" ):
                listener.enterFullAhead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFullAhead" ):
                listener.exitFullAhead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFullAhead" ):
                return visitor.visitFullAhead(self)
            else:
                return visitor.visitChildren(self)


    class OarsInWaterContext(SpeedCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SpeedCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WIOSLA(self):
            return self.getToken(SailingParser.WIOSLA, 0)
        def NA(self):
            return self.getToken(SailingParser.NA, 0)
        def WODE(self):
            return self.getToken(SailingParser.WODE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOarsInWater" ):
                listener.enterOarsInWater(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOarsInWater" ):
                listener.exitOarsInWater(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOarsInWater" ):
                return visitor.visitOarsInWater(self)
            else:
                return visitor.visitChildren(self)


    class MediumAheadContext(SpeedCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SpeedCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SREDNI(self):
            return self.getToken(SailingParser.SREDNI, 0)
        def NAPRZOD(self):
            return self.getToken(SailingParser.NAPRZOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMediumAhead" ):
                listener.enterMediumAhead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMediumAhead" ):
                listener.exitMediumAhead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMediumAhead" ):
                return visitor.visitMediumAhead(self)
            else:
                return visitor.visitChildren(self)


    class OarsUpContext(SpeedCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SpeedCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PODNIES(self):
            return self.getToken(SailingParser.PODNIES, 0)
        def WIOSLA(self):
            return self.getToken(SailingParser.WIOSLA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOarsUp" ):
                listener.enterOarsUp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOarsUp" ):
                listener.exitOarsUp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOarsUp" ):
                return visitor.visitOarsUp(self)
            else:
                return visitor.visitChildren(self)


    class SlowAheadContext(SpeedCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SpeedCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WOLNY(self):
            return self.getToken(SailingParser.WOLNY, 0)
        def NAPRZOD(self):
            return self.getToken(SailingParser.NAPRZOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSlowAhead" ):
                listener.enterSlowAhead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSlowAhead" ):
                listener.exitSlowAhead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSlowAhead" ):
                return visitor.visitSlowAhead(self)
            else:
                return visitor.visitChildren(self)


    class RowSlowAheadContext(SpeedCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SpeedCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WESLUJ(self):
            return self.getToken(SailingParser.WESLUJ, 0)
        def WOLNY(self):
            return self.getToken(SailingParser.WOLNY, 0)
        def NAPRZOD(self):
            return self.getToken(SailingParser.NAPRZOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRowSlowAhead" ):
                listener.enterRowSlowAhead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRowSlowAhead" ):
                listener.exitRowSlowAhead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRowSlowAhead" ):
                return visitor.visitRowSlowAhead(self)
            else:
                return visitor.visitChildren(self)


    class AllStopContext(SpeedCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SpeedCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STOP_KW(self):
            return self.getToken(SailingParser.STOP_KW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllStop" ):
                listener.enterAllStop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllStop" ):
                listener.exitAllStop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllStop" ):
                return visitor.visitAllStop(self)
            else:
                return visitor.visitChildren(self)


    class RowFullAheadContext(SpeedCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SpeedCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WESLUJ(self):
            return self.getToken(SailingParser.WESLUJ, 0)
        def CALA(self):
            return self.getToken(SailingParser.CALA, 0)
        def NAPRZOD(self):
            return self.getToken(SailingParser.NAPRZOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRowFullAhead" ):
                listener.enterRowFullAhead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRowFullAhead" ):
                listener.exitRowFullAhead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRowFullAhead" ):
                return visitor.visitRowFullAhead(self)
            else:
                return visitor.visitChildren(self)


    class RowReverseContext(SpeedCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SpeedCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WESLUJ(self):
            return self.getToken(SailingParser.WESLUJ, 0)
        def WSTECZNY(self):
            return self.getToken(SailingParser.WSTECZNY, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRowReverse" ):
                listener.enterRowReverse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRowReverse" ):
                listener.exitRowReverse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRowReverse" ):
                return visitor.visitRowReverse(self)
            else:
                return visitor.visitChildren(self)


    class StartRowingContext(SpeedCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.SpeedCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WESLUJ(self):
            return self.getToken(SailingParser.WESLUJ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartRowing" ):
                listener.enterStartRowing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartRowing" ):
                listener.exitStartRowing(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStartRowing" ):
                return visitor.visitStartRowing(self)
            else:
                return visitor.visitChildren(self)



    def speedCommand(self):

        localctx = SailingParser.SpeedCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_speedCommand)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = SailingParser.StartRowingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(SailingParser.WESLUJ)
                pass

            elif la_ == 2:
                localctx = SailingParser.RowFullAheadContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(SailingParser.WESLUJ)
                self.state = 257
                self.match(SailingParser.CALA)
                self.state = 258
                self.match(SailingParser.NAPRZOD)
                pass

            elif la_ == 3:
                localctx = SailingParser.RowSlowAheadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 259
                self.match(SailingParser.WESLUJ)
                self.state = 260
                self.match(SailingParser.WOLNY)
                self.state = 261
                self.match(SailingParser.NAPRZOD)
                pass

            elif la_ == 4:
                localctx = SailingParser.RowReverseContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 262
                self.match(SailingParser.WESLUJ)
                self.state = 263
                self.match(SailingParser.WSTECZNY)
                pass

            elif la_ == 5:
                localctx = SailingParser.OarsInWaterContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 264
                self.match(SailingParser.WIOSLA)
                self.state = 265
                self.match(SailingParser.NA)
                self.state = 266
                self.match(SailingParser.WODE)
                pass

            elif la_ == 6:
                localctx = SailingParser.OarsUpContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 267
                self.match(SailingParser.PODNIES)
                self.state = 268
                self.match(SailingParser.WIOSLA)
                pass

            elif la_ == 7:
                localctx = SailingParser.FullAheadContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 269
                self.match(SailingParser.CALA)
                self.state = 270
                self.match(SailingParser.NAPRZOD)
                pass

            elif la_ == 8:
                localctx = SailingParser.SlowAheadContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 271
                self.match(SailingParser.WOLNY)
                self.state = 272
                self.match(SailingParser.NAPRZOD)
                pass

            elif la_ == 9:
                localctx = SailingParser.MediumAheadContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 273
                self.match(SailingParser.SREDNI)
                self.state = 274
                self.match(SailingParser.NAPRZOD)
                pass

            elif la_ == 10:
                localctx = SailingParser.AllStopContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 275
                self.match(SailingParser.STOP_KW)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CombatCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_combatCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FireCannonsContext(CombatCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CombatCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OGNIA(self):
            return self.getToken(SailingParser.OGNIA, 0)
        def cannonGroup(self):
            return self.getTypedRuleContext(SailingParser.CannonGroupContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFireCannons" ):
                listener.enterFireCannons(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFireCannons" ):
                listener.exitFireCannons(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFireCannons" ):
                return visitor.visitFireCannons(self)
            else:
                return visitor.visitChildren(self)


    class LoadCannonsAmmoContext(CombatCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CombatCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LADUJ(self):
            return self.getToken(SailingParser.LADUJ, 0)
        def cannonGroup(self):
            return self.getTypedRuleContext(SailingParser.CannonGroupContext,0)

        def ammoType(self):
            return self.getTypedRuleContext(SailingParser.AmmoTypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadCannonsAmmo" ):
                listener.enterLoadCannonsAmmo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadCannonsAmmo" ):
                listener.exitLoadCannonsAmmo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadCannonsAmmo" ):
                return visitor.visitLoadCannonsAmmo(self)
            else:
                return visitor.visitChildren(self)


    class BroadsideContext(CombatCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CombatCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SALWA(self):
            return self.getToken(SailingParser.SALWA, 0)
        def boardSide(self):
            return self.getTypedRuleContext(SailingParser.BoardSideContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBroadside" ):
                listener.enterBroadside(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBroadside" ):
                listener.exitBroadside(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBroadside" ):
                return visitor.visitBroadside(self)
            else:
                return visitor.visitChildren(self)


    class BroadsideLeftContext(CombatCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CombatCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SALWA(self):
            return self.getToken(SailingParser.SALWA, 0)
        def BURTA_LEWA(self):
            return self.getToken(SailingParser.BURTA_LEWA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBroadsideLeft" ):
                listener.enterBroadsideLeft(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBroadsideLeft" ):
                listener.exitBroadsideLeft(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBroadsideLeft" ):
                return visitor.visitBroadsideLeft(self)
            else:
                return visitor.visitChildren(self)


    class LoadCannonsContext(CombatCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CombatCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LADUJ(self):
            return self.getToken(SailingParser.LADUJ, 0)
        def cannonGroup(self):
            return self.getTypedRuleContext(SailingParser.CannonGroupContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadCannons" ):
                listener.enterLoadCannons(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadCannons" ):
                listener.exitLoadCannons(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadCannons" ):
                return visitor.visitLoadCannons(self)
            else:
                return visitor.visitChildren(self)


    class FireAllContext(CombatCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CombatCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OGNIA(self):
            return self.getToken(SailingParser.OGNIA, 0)
        def WSZYSTKIE_DZIALA(self):
            return self.getToken(SailingParser.WSZYSTKIE_DZIALA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFireAll" ):
                listener.enterFireAll(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFireAll" ):
                listener.exitFireAll(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFireAll" ):
                return visitor.visitFireAll(self)
            else:
                return visitor.visitChildren(self)


    class BroadsideRightContext(CombatCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CombatCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SALWA(self):
            return self.getToken(SailingParser.SALWA, 0)
        def BURTA_PRAWA(self):
            return self.getToken(SailingParser.BURTA_PRAWA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBroadsideRight" ):
                listener.enterBroadsideRight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBroadsideRight" ):
                listener.exitBroadsideRight(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBroadsideRight" ):
                return visitor.visitBroadsideRight(self)
            else:
                return visitor.visitChildren(self)



    def combatCommand(self):

        localctx = SailingParser.CombatCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_combatCommand)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = SailingParser.LoadCannonsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(SailingParser.LADUJ)
                self.state = 279
                self.cannonGroup()
                pass

            elif la_ == 2:
                localctx = SailingParser.LoadCannonsAmmoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(SailingParser.LADUJ)
                self.state = 281
                self.cannonGroup()
                self.state = 282
                self.ammoType()
                pass

            elif la_ == 3:
                localctx = SailingParser.FireCannonsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 284
                self.match(SailingParser.OGNIA)
                self.state = 285
                self.cannonGroup()
                pass

            elif la_ == 4:
                localctx = SailingParser.FireAllContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 286
                self.match(SailingParser.OGNIA)
                self.state = 287
                self.match(SailingParser.WSZYSTKIE_DZIALA)
                pass

            elif la_ == 5:
                localctx = SailingParser.BroadsideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 288
                self.match(SailingParser.SALWA)
                self.state = 289
                self.boardSide()
                pass

            elif la_ == 6:
                localctx = SailingParser.BroadsideLeftContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 290
                self.match(SailingParser.SALWA)
                self.state = 291
                self.match(SailingParser.BURTA_LEWA)
                pass

            elif la_ == 7:
                localctx = SailingParser.BroadsideRightContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 292
                self.match(SailingParser.SALWA)
                self.state = 293
                self.match(SailingParser.BURTA_PRAWA)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CannonGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARMATY(self):
            return self.getToken(SailingParser.ARMATY, 0)

        def DZIALA(self):
            return self.getToken(SailingParser.DZIALA, 0)

        def KOLUBRYNA(self):
            return self.getToken(SailingParser.KOLUBRYNA, 0)

        def KARRONADA(self):
            return self.getToken(SailingParser.KARRONADA, 0)

        def getRuleIndex(self):
            return SailingParser.RULE_cannonGroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCannonGroup" ):
                listener.enterCannonGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCannonGroup" ):
                listener.exitCannonGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCannonGroup" ):
                return visitor.visitCannonGroup(self)
            else:
                return visitor.visitChildren(self)




    def cannonGroup(self):

        localctx = SailingParser.CannonGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_cannonGroup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8646911284551352320) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AmmoTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KULA(self):
            return self.getToken(SailingParser.KULA, 0)

        def KARTACZ(self):
            return self.getToken(SailingParser.KARTACZ, 0)

        def LANCUCH_KULA(self):
            return self.getToken(SailingParser.LANCUCH_KULA, 0)

        def ZAPALAJACA(self):
            return self.getToken(SailingParser.ZAPALAJACA, 0)

        def BOMBA(self):
            return self.getToken(SailingParser.BOMBA, 0)

        def getRuleIndex(self):
            return SailingParser.RULE_ammoType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAmmoType" ):
                listener.enterAmmoType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAmmoType" ):
                listener.exitAmmoType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAmmoType" ):
                return visitor.visitAmmoType(self)
            else:
                return visitor.visitChildren(self)




    def ammoType(self):

        localctx = SailingParser.AmmoTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ammoType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            _la = self._input.LA(1)
            if not(((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 31) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CargoCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_cargoCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TransferCargoContext(CargoCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CargoCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRZELADUJ(self):
            return self.getToken(SailingParser.PRZELADUJ, 0)
        def cargoType(self):
            return self.getTypedRuleContext(SailingParser.CargoTypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransferCargo" ):
                listener.enterTransferCargo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransferCargo" ):
                listener.exitTransferCargo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransferCargo" ):
                return visitor.visitTransferCargo(self)
            else:
                return visitor.visitChildren(self)


    class UnloadCargoContext(CargoCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CargoCommandContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def ROZLADUJ(self):
            return self.getToken(SailingParser.ROZLADUJ, 0)
        def cargoType(self):
            return self.getTypedRuleContext(SailingParser.CargoTypeContext,0)

        def SZTUK(self):
            return self.getToken(SailingParser.SZTUK, 0)
        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnloadCargo" ):
                listener.enterUnloadCargo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnloadCargo" ):
                listener.exitUnloadCargo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnloadCargo" ):
                return visitor.visitUnloadCargo(self)
            else:
                return visitor.visitChildren(self)


    class LoadCargoContext(CargoCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CargoCommandContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def ZALADUJ(self):
            return self.getToken(SailingParser.ZALADUJ, 0)
        def cargoType(self):
            return self.getTypedRuleContext(SailingParser.CargoTypeContext,0)

        def SZTUK(self):
            return self.getToken(SailingParser.SZTUK, 0)
        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadCargo" ):
                listener.enterLoadCargo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadCargo" ):
                listener.exitLoadCargo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadCargo" ):
                return visitor.visitLoadCargo(self)
            else:
                return visitor.visitChildren(self)


    class CargoStateReportContext(CargoCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CargoCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RAPORT(self):
            return self.getToken(SailingParser.RAPORT, 0)
        def STAN_LADOWNI(self):
            return self.getToken(SailingParser.STAN_LADOWNI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCargoStateReport" ):
                listener.enterCargoStateReport(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCargoStateReport" ):
                listener.exitCargoStateReport(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCargoStateReport" ):
                return visitor.visitCargoStateReport(self)
            else:
                return visitor.visitChildren(self)


    class DigTreasureContext(CargoCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CargoCommandContext
            super().__init__(parser)
            self.point = None # Token
            self.copyFrom(ctx)

        def WYKOP(self):
            return self.getToken(SailingParser.WYKOP, 0)
        def SKARB(self):
            return self.getToken(SailingParser.SKARB, 0)
        def NA(self):
            return self.getToken(SailingParser.NA, 0)
        def WYSPA(self):
            return self.getToken(SailingParser.WYSPA, 0)
        def STRING(self):
            return self.getToken(SailingParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigTreasure" ):
                listener.enterDigTreasure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigTreasure" ):
                listener.exitDigTreasure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDigTreasure" ):
                return visitor.visitDigTreasure(self)
            else:
                return visitor.visitChildren(self)


    class CargoReportContext(CargoCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CargoCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RAPORT(self):
            return self.getToken(SailingParser.RAPORT, 0)
        def LADOWNIA(self):
            return self.getToken(SailingParser.LADOWNIA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCargoReport" ):
                listener.enterCargoReport(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCargoReport" ):
                listener.exitCargoReport(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCargoReport" ):
                return visitor.visitCargoReport(self)
            else:
                return visitor.visitChildren(self)


    class BuryTreasureContext(CargoCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CargoCommandContext
            super().__init__(parser)
            self.point = None # Token
            self.copyFrom(ctx)

        def ZAKOP(self):
            return self.getToken(SailingParser.ZAKOP, 0)
        def SKARB(self):
            return self.getToken(SailingParser.SKARB, 0)
        def NA(self):
            return self.getToken(SailingParser.NA, 0)
        def WYSPA(self):
            return self.getToken(SailingParser.WYSPA, 0)
        def STRING(self):
            return self.getToken(SailingParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuryTreasure" ):
                listener.enterBuryTreasure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuryTreasure" ):
                listener.exitBuryTreasure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuryTreasure" ):
                return visitor.visitBuryTreasure(self)
            else:
                return visitor.visitChildren(self)



    def cargoCommand(self):

        localctx = SailingParser.CargoCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_cargoCommand)
        self._la = 0 # Token type
        try:
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = SailingParser.LoadCargoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(SailingParser.ZALADUJ)
                self.state = 301
                self.cargoType()
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==156:
                    self.state = 302
                    localctx.value = self.match(SailingParser.NUMBER)
                    self.state = 303
                    self.match(SailingParser.SZTUK)


                pass

            elif la_ == 2:
                localctx = SailingParser.UnloadCargoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.match(SailingParser.ROZLADUJ)
                self.state = 307
                self.cargoType()
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==156:
                    self.state = 308
                    localctx.value = self.match(SailingParser.NUMBER)
                    self.state = 309
                    self.match(SailingParser.SZTUK)


                pass

            elif la_ == 3:
                localctx = SailingParser.TransferCargoContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                self.match(SailingParser.PRZELADUJ)
                self.state = 313
                self.cargoType()
                pass

            elif la_ == 4:
                localctx = SailingParser.BuryTreasureContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 314
                self.match(SailingParser.ZAKOP)
                self.state = 315
                self.match(SailingParser.SKARB)
                self.state = 316
                self.match(SailingParser.NA)
                self.state = 317
                self.match(SailingParser.WYSPA)
                self.state = 318
                localctx.point = self.match(SailingParser.STRING)
                pass

            elif la_ == 5:
                localctx = SailingParser.DigTreasureContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 319
                self.match(SailingParser.WYKOP)
                self.state = 320
                self.match(SailingParser.SKARB)
                self.state = 321
                self.match(SailingParser.NA)
                self.state = 322
                self.match(SailingParser.WYSPA)
                self.state = 323
                localctx.point = self.match(SailingParser.STRING)
                pass

            elif la_ == 6:
                localctx = SailingParser.CargoReportContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 324
                self.match(SailingParser.RAPORT)
                self.state = 325
                self.match(SailingParser.LADOWNIA)
                pass

            elif la_ == 7:
                localctx = SailingParser.CargoStateReportContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 326
                self.match(SailingParser.RAPORT)
                self.state = 327
                self.match(SailingParser.STAN_LADOWNI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CargoTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LUPY(self):
            return self.getToken(SailingParser.LUPY, 0)

        def SKARB(self):
            return self.getToken(SailingParser.SKARB, 0)

        def ZLOTO(self):
            return self.getToken(SailingParser.ZLOTO, 0)

        def SREBRO(self):
            return self.getToken(SailingParser.SREBRO, 0)

        def AMUNICJA(self):
            return self.getToken(SailingParser.AMUNICJA, 0)

        def PROWIANT(self):
            return self.getToken(SailingParser.PROWIANT, 0)

        def RUM(self):
            return self.getToken(SailingParser.RUM, 0)

        def WODA_PITNA(self):
            return self.getToken(SailingParser.WODA_PITNA, 0)

        def PROCH(self):
            return self.getToken(SailingParser.PROCH, 0)

        def BECZKI(self):
            return self.getToken(SailingParser.BECZKI, 0)

        def SKRZYNIE(self):
            return self.getToken(SailingParser.SKRZYNIE, 0)

        def getRuleIndex(self):
            return SailingParser.RULE_cargoType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCargoType" ):
                listener.enterCargoType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCargoType" ):
                listener.exitCargoType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCargoType" ):
                return visitor.visitCargoType(self)
            else:
                return visitor.visitChildren(self)




    def cargoType(self):

        localctx = SailingParser.CargoTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_cargoType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            _la = self._input.LA(1)
            if not(((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & 2047) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CrewCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_crewCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AllOnDeckContext(CrewCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CrewCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WSZYSCY(self):
            return self.getToken(SailingParser.WSZYSCY, 0)
        def NA(self):
            return self.getToken(SailingParser.NA, 0)
        def POKLAD(self):
            return self.getToken(SailingParser.POKLAD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllOnDeck" ):
                listener.enterAllOnDeck(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllOnDeck" ):
                listener.exitAllOnDeck(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllOnDeck" ):
                return visitor.visitAllOnDeck(self)
            else:
                return visitor.visitChildren(self)


    class CrewToStationsContext(CrewCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CrewCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ZALOGA(self):
            return self.getToken(SailingParser.ZALOGA, 0)
        def NA(self):
            return self.getToken(SailingParser.NA, 0)
        def STANOWISKA(self):
            return self.getToken(SailingParser.STANOWISKA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCrewToStations" ):
                listener.enterCrewToStations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCrewToStations" ):
                listener.exitCrewToStations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCrewToStations" ):
                return visitor.visitCrewToStations(self)
            else:
                return visitor.visitChildren(self)


    class ManOverboardContext(CrewCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.CrewCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CZLOWIEK(self):
            return self.getToken(SailingParser.CZLOWIEK, 0)
        def ZA(self):
            return self.getToken(SailingParser.ZA, 0)
        def BURTA(self):
            return self.getToken(SailingParser.BURTA, 0)
        def boardSide(self):
            return self.getTypedRuleContext(SailingParser.BoardSideContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterManOverboard" ):
                listener.enterManOverboard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitManOverboard" ):
                listener.exitManOverboard(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManOverboard" ):
                return visitor.visitManOverboard(self)
            else:
                return visitor.visitChildren(self)



    def crewCommand(self):

        localctx = SailingParser.CrewCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_crewCommand)
        self._la = 0 # Token type
        try:
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [98]:
                localctx = SailingParser.CrewToStationsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.match(SailingParser.ZALOGA)
                self.state = 333
                self.match(SailingParser.NA)
                self.state = 334
                self.match(SailingParser.STANOWISKA)
                pass
            elif token in [100]:
                localctx = SailingParser.ManOverboardContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.match(SailingParser.CZLOWIEK)
                self.state = 336
                self.match(SailingParser.ZA)
                self.state = 337
                self.match(SailingParser.BURTA)
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==34 or _la==35:
                    self.state = 338
                    self.boardSide()


                pass
            elif token in [103]:
                localctx = SailingParser.AllOnDeckContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 341
                self.match(SailingParser.WSZYSCY)
                self.state = 342
                self.match(SailingParser.NA)
                self.state = 343
                self.match(SailingParser.POKLAD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_flagCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RaiseJollyRogerContext(FlagCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.FlagCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PODNIES(self):
            return self.getToken(SailingParser.PODNIES, 0)
        def JOLLY_ROGER(self):
            return self.getToken(SailingParser.JOLLY_ROGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaiseJollyRoger" ):
                listener.enterRaiseJollyRoger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaiseJollyRoger" ):
                listener.exitRaiseJollyRoger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaiseJollyRoger" ):
                return visitor.visitRaiseJollyRoger(self)
            else:
                return visitor.visitChildren(self)


    class RaiseFlagContext(FlagCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.FlagCommandContext
            super().__init__(parser)
            self.flag = None # Token
            self.copyFrom(ctx)

        def PODNIES(self):
            return self.getToken(SailingParser.PODNIES, 0)
        def FLAGE(self):
            return self.getToken(SailingParser.FLAGE, 0)
        def STRING(self):
            return self.getToken(SailingParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaiseFlag" ):
                listener.enterRaiseFlag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaiseFlag" ):
                listener.exitRaiseFlag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaiseFlag" ):
                return visitor.visitRaiseFlag(self)
            else:
                return visitor.visitChildren(self)


    class RaiseMerchantFlagContext(FlagCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.FlagCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PODNIES(self):
            return self.getToken(SailingParser.PODNIES, 0)
        def FLAGA_HANDLOWA(self):
            return self.getToken(SailingParser.FLAGA_HANDLOWA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaiseMerchantFlag" ):
                listener.enterRaiseMerchantFlag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaiseMerchantFlag" ):
                listener.exitRaiseMerchantFlag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaiseMerchantFlag" ):
                return visitor.visitRaiseMerchantFlag(self)
            else:
                return visitor.visitChildren(self)


    class RaiseBannerContext(FlagCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.FlagCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PODNIES(self):
            return self.getToken(SailingParser.PODNIES, 0)
        def BANDERA(self):
            return self.getToken(SailingParser.BANDERA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaiseBanner" ):
                listener.enterRaiseBanner(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaiseBanner" ):
                listener.exitRaiseBanner(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaiseBanner" ):
                return visitor.visitRaiseBanner(self)
            else:
                return visitor.visitChildren(self)


    class RaiseWhiteFlagContext(FlagCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.FlagCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PODNIES(self):
            return self.getToken(SailingParser.PODNIES, 0)
        def FLAGA_BIALA(self):
            return self.getToken(SailingParser.FLAGA_BIALA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaiseWhiteFlag" ):
                listener.enterRaiseWhiteFlag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaiseWhiteFlag" ):
                listener.exitRaiseWhiteFlag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaiseWhiteFlag" ):
                return visitor.visitRaiseWhiteFlag(self)
            else:
                return visitor.visitChildren(self)


    class LowerFlagContext(FlagCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.FlagCommandContext
            super().__init__(parser)
            self.flag = None # Token
            self.copyFrom(ctx)

        def OPUSC(self):
            return self.getToken(SailingParser.OPUSC, 0)
        def FLAGE(self):
            return self.getToken(SailingParser.FLAGE, 0)
        def STRING(self):
            return self.getToken(SailingParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLowerFlag" ):
                listener.enterLowerFlag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLowerFlag" ):
                listener.exitLowerFlag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLowerFlag" ):
                return visitor.visitLowerFlag(self)
            else:
                return visitor.visitChildren(self)


    class LowerJollyRogerContext(FlagCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.FlagCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPUSC(self):
            return self.getToken(SailingParser.OPUSC, 0)
        def JOLLY_ROGER(self):
            return self.getToken(SailingParser.JOLLY_ROGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLowerJollyRoger" ):
                listener.enterLowerJollyRoger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLowerJollyRoger" ):
                listener.exitLowerJollyRoger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLowerJollyRoger" ):
                return visitor.visitLowerJollyRoger(self)
            else:
                return visitor.visitChildren(self)


    class LowerBannerContext(FlagCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.FlagCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPUSC(self):
            return self.getToken(SailingParser.OPUSC, 0)
        def BANDERA(self):
            return self.getToken(SailingParser.BANDERA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLowerBanner" ):
                listener.enterLowerBanner(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLowerBanner" ):
                listener.exitLowerBanner(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLowerBanner" ):
                return visitor.visitLowerBanner(self)
            else:
                return visitor.visitChildren(self)


    class RaiseFalseFlagContext(FlagCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.FlagCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PODNIES(self):
            return self.getToken(SailingParser.PODNIES, 0)
        def FALS_FLAGA(self):
            return self.getToken(SailingParser.FALS_FLAGA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaiseFalseFlag" ):
                listener.enterRaiseFalseFlag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaiseFalseFlag" ):
                listener.exitRaiseFalseFlag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaiseFalseFlag" ):
                return visitor.visitRaiseFalseFlag(self)
            else:
                return visitor.visitChildren(self)


    class SignalFlagsContext(FlagCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.FlagCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SYGNALIZUJ(self):
            return self.getToken(SailingParser.SYGNALIZUJ, 0)
        def flagSequence(self):
            return self.getTypedRuleContext(SailingParser.FlagSequenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignalFlags" ):
                listener.enterSignalFlags(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignalFlags" ):
                listener.exitSignalFlags(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignalFlags" ):
                return visitor.visitSignalFlags(self)
            else:
                return visitor.visitChildren(self)


    class LowerFalseFlagContext(FlagCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.FlagCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPUSC(self):
            return self.getToken(SailingParser.OPUSC, 0)
        def FALS_FLAGA(self):
            return self.getToken(SailingParser.FALS_FLAGA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLowerFalseFlag" ):
                listener.enterLowerFalseFlag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLowerFalseFlag" ):
                listener.exitLowerFalseFlag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLowerFalseFlag" ):
                return visitor.visitLowerFalseFlag(self)
            else:
                return visitor.visitChildren(self)



    def flagCommand(self):

        localctx = SailingParser.FlagCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_flagCommand)
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = SailingParser.RaiseFlagContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(SailingParser.PODNIES)
                self.state = 347
                self.match(SailingParser.FLAGE)
                self.state = 348
                localctx.flag = self.match(SailingParser.STRING)
                pass

            elif la_ == 2:
                localctx = SailingParser.LowerFlagContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.match(SailingParser.OPUSC)
                self.state = 350
                self.match(SailingParser.FLAGE)
                self.state = 351
                localctx.flag = self.match(SailingParser.STRING)
                pass

            elif la_ == 3:
                localctx = SailingParser.RaiseJollyRogerContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                self.match(SailingParser.PODNIES)
                self.state = 353
                self.match(SailingParser.JOLLY_ROGER)
                pass

            elif la_ == 4:
                localctx = SailingParser.LowerJollyRogerContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 354
                self.match(SailingParser.OPUSC)
                self.state = 355
                self.match(SailingParser.JOLLY_ROGER)
                pass

            elif la_ == 5:
                localctx = SailingParser.RaiseBannerContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 356
                self.match(SailingParser.PODNIES)
                self.state = 357
                self.match(SailingParser.BANDERA)
                pass

            elif la_ == 6:
                localctx = SailingParser.LowerBannerContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 358
                self.match(SailingParser.OPUSC)
                self.state = 359
                self.match(SailingParser.BANDERA)
                pass

            elif la_ == 7:
                localctx = SailingParser.RaiseFalseFlagContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 360
                self.match(SailingParser.PODNIES)
                self.state = 361
                self.match(SailingParser.FALS_FLAGA)
                pass

            elif la_ == 8:
                localctx = SailingParser.LowerFalseFlagContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 362
                self.match(SailingParser.OPUSC)
                self.state = 363
                self.match(SailingParser.FALS_FLAGA)
                pass

            elif la_ == 9:
                localctx = SailingParser.RaiseMerchantFlagContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 364
                self.match(SailingParser.PODNIES)
                self.state = 365
                self.match(SailingParser.FLAGA_HANDLOWA)
                pass

            elif la_ == 10:
                localctx = SailingParser.RaiseWhiteFlagContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 366
                self.match(SailingParser.PODNIES)
                self.state = 367
                self.match(SailingParser.FLAGA_BIALA)
                pass

            elif la_ == 11:
                localctx = SailingParser.SignalFlagsContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 368
                self.match(SailingParser.SYGNALIZUJ)
                self.state = 369
                self.flagSequence()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagSequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SailingParser.STRING)
            else:
                return self.getToken(SailingParser.STRING, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SailingParser.COMMA)
            else:
                return self.getToken(SailingParser.COMMA, i)

        def getRuleIndex(self):
            return SailingParser.RULE_flagSequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlagSequence" ):
                listener.enterFlagSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlagSequence" ):
                listener.exitFlagSequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlagSequence" ):
                return visitor.visitFlagSequence(self)
            else:
                return visitor.visitChildren(self)




    def flagSequence(self):

        localctx = SailingParser.FlagSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_flagSequence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(SailingParser.STRING)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==153:
                self.state = 373
                self.match(SailingParser.COMMA)
                self.state = 374
                self.match(SailingParser.STRING)
                self.state = 379
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepairCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_repairCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RepairContext(RepairCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RepairCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAPRAW(self):
            return self.getToken(SailingParser.NAPRAW, 0)
        def repairTarget(self):
            return self.getTypedRuleContext(SailingParser.RepairTargetContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepair" ):
                listener.enterRepair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepair" ):
                listener.exitRepair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepair" ):
                return visitor.visitRepair(self)
            else:
                return visitor.visitChildren(self)



    def repairCommand(self):

        localctx = SailingParser.RepairCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_repairCommand)
        try:
            localctx = SailingParser.RepairContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(SailingParser.NAPRAW)
            self.state = 381
            self.repairTarget()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepairTargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KADLUB(self):
            return self.getToken(SailingParser.KADLUB, 0)

        def MASZT(self):
            return self.getToken(SailingParser.MASZT, 0)

        def TAKIELUNEK(self):
            return self.getToken(SailingParser.TAKIELUNEK, 0)

        def getRuleIndex(self):
            return SailingParser.RULE_repairTarget

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepairTarget" ):
                listener.enterRepairTarget(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepairTarget" ):
                listener.exitRepairTarget(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepairTarget" ):
                return visitor.visitRepairTarget(self)
            else:
                return visitor.visitChildren(self)




    def repairTarget(self):

        localctx = SailingParser.RepairTargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_repairTarget)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            _la = self._input.LA(1)
            if not(((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & 7) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_logCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LogShipStateContext(LogCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.LogCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOGUJ(self):
            return self.getToken(SailingParser.LOGUJ, 0)
        def STAN_JEDNOSTKI(self):
            return self.getToken(SailingParser.STAN_JEDNOSTKI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogShipState" ):
                listener.enterLogShipState(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogShipState" ):
                listener.exitLogShipState(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogShipState" ):
                return visitor.visitLogShipState(self)
            else:
                return visitor.visitChildren(self)


    class LogMessageContext(LogCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.LogCommandContext
            super().__init__(parser)
            self.message = None # Token
            self.copyFrom(ctx)

        def LOGUJ(self):
            return self.getToken(SailingParser.LOGUJ, 0)
        def STRING(self):
            return self.getToken(SailingParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogMessage" ):
                listener.enterLogMessage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogMessage" ):
                listener.exitLogMessage(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogMessage" ):
                return visitor.visitLogMessage(self)
            else:
                return visitor.visitChildren(self)


    class LogEventContext(LogCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.LogCommandContext
            super().__init__(parser)
            self.message = None # Token
            self.copyFrom(ctx)

        def LOGUJ(self):
            return self.getToken(SailingParser.LOGUJ, 0)
        def ZDARZENIE(self):
            return self.getToken(SailingParser.ZDARZENIE, 0)
        def STRING(self):
            return self.getToken(SailingParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogEvent" ):
                listener.enterLogEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogEvent" ):
                listener.exitLogEvent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogEvent" ):
                return visitor.visitLogEvent(self)
            else:
                return visitor.visitChildren(self)


    class LogWeatherContext(LogCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.LogCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOGUJ(self):
            return self.getToken(SailingParser.LOGUJ, 0)
        def POGODE(self):
            return self.getToken(SailingParser.POGODE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogWeather" ):
                listener.enterLogWeather(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogWeather" ):
                listener.exitLogWeather(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogWeather" ):
                return visitor.visitLogWeather(self)
            else:
                return visitor.visitChildren(self)


    class LogCargoStateContext(LogCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.LogCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOGUJ(self):
            return self.getToken(SailingParser.LOGUJ, 0)
        def STAN_LADOWNI(self):
            return self.getToken(SailingParser.STAN_LADOWNI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogCargoState" ):
                listener.enterLogCargoState(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogCargoState" ):
                listener.exitLogCargoState(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogCargoState" ):
                return visitor.visitLogCargoState(self)
            else:
                return visitor.visitChildren(self)


    class LogPositionContext(LogCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.LogCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOGUJ(self):
            return self.getToken(SailingParser.LOGUJ, 0)
        def POZYCJE(self):
            return self.getToken(SailingParser.POZYCJE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogPosition" ):
                listener.enterLogPosition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogPosition" ):
                listener.exitLogPosition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogPosition" ):
                return visitor.visitLogPosition(self)
            else:
                return visitor.visitChildren(self)



    def logCommand(self):

        localctx = SailingParser.LogCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_logCommand)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = SailingParser.LogMessageContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.match(SailingParser.LOGUJ)
                self.state = 386
                localctx.message = self.match(SailingParser.STRING)
                pass

            elif la_ == 2:
                localctx = SailingParser.LogPositionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.match(SailingParser.LOGUJ)
                self.state = 388
                self.match(SailingParser.POZYCJE)
                pass

            elif la_ == 3:
                localctx = SailingParser.LogWeatherContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 389
                self.match(SailingParser.LOGUJ)
                self.state = 390
                self.match(SailingParser.POGODE)
                pass

            elif la_ == 4:
                localctx = SailingParser.LogEventContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 391
                self.match(SailingParser.LOGUJ)
                self.state = 392
                self.match(SailingParser.ZDARZENIE)
                self.state = 393
                localctx.message = self.match(SailingParser.STRING)
                pass

            elif la_ == 5:
                localctx = SailingParser.LogCargoStateContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 394
                self.match(SailingParser.LOGUJ)
                self.state = 395
                self.match(SailingParser.STAN_LADOWNI)
                pass

            elif la_ == 6:
                localctx = SailingParser.LogShipStateContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 396
                self.match(SailingParser.LOGUJ)
                self.state = 397
                self.match(SailingParser.STAN_JEDNOSTKI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmergencyCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_emergencyCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BattleAlarmContext(EmergencyCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.EmergencyCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ALARM_BOJOWY(self):
            return self.getToken(SailingParser.ALARM_BOJOWY, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBattleAlarm" ):
                listener.enterBattleAlarm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBattleAlarm" ):
                listener.exitBattleAlarm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBattleAlarm" ):
                return visitor.visitBattleAlarm(self)
            else:
                return visitor.visitChildren(self)



    def emergencyCommand(self):

        localctx = SailingParser.EmergencyCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_emergencyCommand)
        try:
            localctx = SailingParser.BattleAlarmContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(SailingParser.ALARM_BOJOWY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WeatherQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_weatherQuery

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReportWeatherContext(WeatherQueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.WeatherQueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RAPORT(self):
            return self.getToken(SailingParser.RAPORT, 0)
        def POGODE(self):
            return self.getToken(SailingParser.POGODE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReportWeather" ):
                listener.enterReportWeather(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReportWeather" ):
                listener.exitReportWeather(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReportWeather" ):
                return visitor.visitReportWeather(self)
            else:
                return visitor.visitChildren(self)


    class ReportDepthContext(WeatherQueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.WeatherQueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RAPORT(self):
            return self.getToken(SailingParser.RAPORT, 0)
        def GLEBOKOSC(self):
            return self.getToken(SailingParser.GLEBOKOSC, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReportDepth" ):
                listener.enterReportDepth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReportDepth" ):
                listener.exitReportDepth(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReportDepth" ):
                return visitor.visitReportDepth(self)
            else:
                return visitor.visitChildren(self)


    class ReportWindContext(WeatherQueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.WeatherQueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RAPORT(self):
            return self.getToken(SailingParser.RAPORT, 0)
        def WIATR(self):
            return self.getToken(SailingParser.WIATR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReportWind" ):
                listener.enterReportWind(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReportWind" ):
                listener.exitReportWind(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReportWind" ):
                return visitor.visitReportWind(self)
            else:
                return visitor.visitChildren(self)



    def weatherQuery(self):

        localctx = SailingParser.WeatherQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_weatherQuery)
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                localctx = SailingParser.ReportWindContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.match(SailingParser.RAPORT)
                self.state = 403
                self.match(SailingParser.WIATR)
                pass

            elif la_ == 2:
                localctx = SailingParser.ReportWeatherContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.match(SailingParser.RAPORT)
                self.state = 405
                self.match(SailingParser.POGODE)
                pass

            elif la_ == 3:
                localctx = SailingParser.ReportDepthContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 406
                self.match(SailingParser.RAPORT)
                self.state = 407
                self.match(SailingParser.GLEBOKOSC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_repeatCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RepeatContext(RepeatCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.RepeatCommandContext
            super().__init__(parser)
            self.times = None # Token
            self.copyFrom(ctx)

        def POWTORZ(self):
            return self.getToken(SailingParser.POWTORZ, 0)
        def RAZY(self):
            return self.getToken(SailingParser.RAZY, 0)
        def LBRACE(self):
            return self.getToken(SailingParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(SailingParser.RBRACE, 0)
        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)
        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SailingParser.CommandContext)
            else:
                return self.getTypedRuleContext(SailingParser.CommandContext,i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(SailingParser.SEMICOLON)
            else:
                return self.getToken(SailingParser.SEMICOLON, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeat" ):
                listener.enterRepeat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeat" ):
                listener.exitRepeat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeat" ):
                return visitor.visitRepeat(self)
            else:
                return visitor.visitChildren(self)



    def repeatCommand(self):

        localctx = SailingParser.RepeatCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_repeatCommand)
        self._la = 0 # Token type
        try:
            localctx = SailingParser.RepeatContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(SailingParser.POWTORZ)
            self.state = 411
            localctx.times = self.match(SailingParser.NUMBER)
            self.state = 412
            self.match(SailingParser.RAZY)
            self.state = 413
            self.match(SailingParser.LBRACE)
            self.state = 417 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 414
                self.command()
                self.state = 415
                self.match(SailingParser.SEMICOLON)
                self.state = 419 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 504437999246819454) != 0) or ((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & -7764055995669708793) != 0) or _la==135):
                    break

            self.state = 421
            self.match(SailingParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaitCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_waitCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WaitUntilContext(WaitCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.WaitCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CZEKAJ_AZ(self):
            return self.getToken(SailingParser.CZEKAJ_AZ, 0)
        def condition(self):
            return self.getTypedRuleContext(SailingParser.ConditionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWaitUntil" ):
                listener.enterWaitUntil(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWaitUntil" ):
                listener.exitWaitUntil(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWaitUntil" ):
                return visitor.visitWaitUntil(self)
            else:
                return visitor.visitChildren(self)


    class WaitDurationContext(WaitCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.WaitCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CZEKAJ(self):
            return self.getToken(SailingParser.CZEKAJ, 0)
        def duration(self):
            return self.getTypedRuleContext(SailingParser.DurationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWaitDuration" ):
                listener.enterWaitDuration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWaitDuration" ):
                listener.exitWaitDuration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWaitDuration" ):
                return visitor.visitWaitDuration(self)
            else:
                return visitor.visitChildren(self)



    def waitCommand(self):

        localctx = SailingParser.WaitCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_waitCommand)
        try:
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [134]:
                localctx = SailingParser.WaitDurationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.match(SailingParser.CZEKAJ)
                self.state = 424
                self.duration()
                pass
            elif token in [135]:
                localctx = SailingParser.WaitUntilContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.match(SailingParser.CZEKAJ_AZ)
                self.state = 426
                self.condition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DurationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None # Token

        def timeUnit(self):
            return self.getTypedRuleContext(SailingParser.TimeUnitContext,0)


        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)

        def getRuleIndex(self):
            return SailingParser.RULE_duration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDuration" ):
                listener.enterDuration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDuration" ):
                listener.exitDuration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDuration" ):
                return visitor.visitDuration(self)
            else:
                return visitor.visitChildren(self)




    def duration(self):

        localctx = SailingParser.DurationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_duration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            localctx.value = self.match(SailingParser.NUMBER)
            self.state = 430
            self.timeUnit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEKUND(self):
            return self.getToken(SailingParser.SEKUND, 0)

        def MINUT(self):
            return self.getToken(SailingParser.MINUT, 0)

        def getRuleIndex(self):
            return SailingParser.RULE_timeUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeUnit" ):
                listener.enterTimeUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeUnit" ):
                listener.exitTimeUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimeUnit" ):
                return visitor.visitTimeUnit(self)
            else:
                return visitor.visitChildren(self)




    def timeUnit(self):

        localctx = SailingParser.TimeUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_timeUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            _la = self._input.LA(1)
            if not(_la==141 or _la==142):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_conditionCommand

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfConditionBlockContext(ConditionCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.ConditionCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def JEZELI(self):
            return self.getToken(SailingParser.JEZELI, 0)
        def condition(self):
            return self.getTypedRuleContext(SailingParser.ConditionContext,0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(SailingParser.LBRACE)
            else:
                return self.getToken(SailingParser.LBRACE, i)
        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(SailingParser.RBRACE)
            else:
                return self.getToken(SailingParser.RBRACE, i)
        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SailingParser.CommandContext)
            else:
                return self.getTypedRuleContext(SailingParser.CommandContext,i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(SailingParser.SEMICOLON)
            else:
                return self.getToken(SailingParser.SEMICOLON, i)
        def INACZEJ(self):
            return self.getToken(SailingParser.INACZEJ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfConditionBlock" ):
                listener.enterIfConditionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfConditionBlock" ):
                listener.exitIfConditionBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfConditionBlock" ):
                return visitor.visitIfConditionBlock(self)
            else:
                return visitor.visitChildren(self)


    class IfConditionContext(ConditionCommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.ConditionCommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def JEZELI(self):
            return self.getToken(SailingParser.JEZELI, 0)
        def condition(self):
            return self.getTypedRuleContext(SailingParser.ConditionContext,0)

        def WTEDY(self):
            return self.getToken(SailingParser.WTEDY, 0)
        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SailingParser.CommandContext)
            else:
                return self.getTypedRuleContext(SailingParser.CommandContext,i)

        def INACZEJ(self):
            return self.getToken(SailingParser.INACZEJ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfCondition" ):
                listener.enterIfCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfCondition" ):
                listener.exitIfCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfCondition" ):
                return visitor.visitIfCondition(self)
            else:
                return visitor.visitChildren(self)



    def conditionCommand(self):

        localctx = SailingParser.ConditionCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_conditionCommand)
        self._la = 0 # Token type
        try:
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                localctx = SailingParser.IfConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.match(SailingParser.JEZELI)
                self.state = 435
                self.condition()
                self.state = 436
                self.match(SailingParser.WTEDY)
                self.state = 437
                self.command()
                self.state = 440
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 438
                    self.match(SailingParser.INACZEJ)
                    self.state = 439
                    self.command()


                pass

            elif la_ == 2:
                localctx = SailingParser.IfConditionBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.match(SailingParser.JEZELI)
                self.state = 443
                self.condition()
                self.state = 444
                self.match(SailingParser.LBRACE)
                self.state = 448 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 445
                    self.command()
                    self.state = 446
                    self.match(SailingParser.SEMICOLON)
                    self.state = 450 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 504437999246819454) != 0) or ((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & -7764055995669708793) != 0) or _la==135):
                        break

                self.state = 452
                self.match(SailingParser.RBRACE)
                self.state = 464
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 453
                    self.match(SailingParser.INACZEJ)
                    self.state = 454
                    self.match(SailingParser.LBRACE)
                    self.state = 458 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 455
                        self.command()
                        self.state = 456
                        self.match(SailingParser.SEMICOLON)
                        self.state = 460 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 504437999246819454) != 0) or ((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & -7764055995669708793) != 0) or _la==135):
                            break

                    self.state = 462
                    self.match(SailingParser.RBRACE)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SailingParser.RULE_condition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SpeedConditionContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.ConditionContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def PREDKOSC(self):
            return self.getToken(SailingParser.PREDKOSC, 0)
        def compOp(self):
            return self.getTypedRuleContext(SailingParser.CompOpContext,0)

        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)
        def WEZLOW(self):
            return self.getToken(SailingParser.WEZLOW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpeedCondition" ):
                listener.enterSpeedCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpeedCondition" ):
                listener.exitSpeedCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpeedCondition" ):
                return visitor.visitSpeedCondition(self)
            else:
                return visitor.visitChildren(self)


    class WindConditionContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.ConditionContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def WIATR(self):
            return self.getToken(SailingParser.WIATR, 0)
        def compOp(self):
            return self.getTypedRuleContext(SailingParser.CompOpContext,0)

        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)
        def WEZLOW(self):
            return self.getToken(SailingParser.WEZLOW, 0)
        def BEAUFORT(self):
            return self.getToken(SailingParser.BEAUFORT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWindCondition" ):
                listener.enterWindCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWindCondition" ):
                listener.exitWindCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWindCondition" ):
                return visitor.visitWindCondition(self)
            else:
                return visitor.visitChildren(self)


    class DepthConditionContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SailingParser.ConditionContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def GLEBOKOSC(self):
            return self.getToken(SailingParser.GLEBOKOSC, 0)
        def compOp(self):
            return self.getTypedRuleContext(SailingParser.CompOpContext,0)

        def NUMBER(self):
            return self.getToken(SailingParser.NUMBER, 0)
        def METROW(self):
            return self.getToken(SailingParser.METROW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDepthCondition" ):
                listener.enterDepthCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDepthCondition" ):
                listener.exitDepthCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDepthCondition" ):
                return visitor.visitDepthCondition(self)
            else:
                return visitor.visitChildren(self)



    def condition(self):

        localctx = SailingParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [126]:
                localctx = SailingParser.WindConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                self.match(SailingParser.WIATR)
                self.state = 469
                self.compOp()
                self.state = 470
                localctx.value = self.match(SailingParser.NUMBER)
                self.state = 472
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==139 or _la==146:
                    self.state = 471
                    _la = self._input.LA(1)
                    if not(_la==139 or _la==146):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                pass
            elif token in [127]:
                localctx = SailingParser.SpeedConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.match(SailingParser.PREDKOSC)
                self.state = 475
                self.compOp()
                self.state = 476
                localctx.value = self.match(SailingParser.NUMBER)
                self.state = 478
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==139:
                    self.state = 477
                    self.match(SailingParser.WEZLOW)


                pass
            elif token in [128]:
                localctx = SailingParser.DepthConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 480
                self.match(SailingParser.GLEBOKOSC)
                self.state = 481
                self.compOp()
                self.state = 482
                localctx.value = self.match(SailingParser.NUMBER)
                self.state = 484
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==138:
                    self.state = 483
                    self.match(SailingParser.METROW)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(SailingParser.GT, 0)

        def LT(self):
            return self.getToken(SailingParser.LT, 0)

        def EQ(self):
            return self.getToken(SailingParser.EQ, 0)

        def GTE(self):
            return self.getToken(SailingParser.GTE, 0)

        def LTE(self):
            return self.getToken(SailingParser.LTE, 0)

        def getRuleIndex(self):
            return SailingParser.RULE_compOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompOp" ):
                listener.enterCompOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompOp" ):
                listener.exitCompOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompOp" ):
                return visitor.visitCompOp(self)
            else:
                return visitor.visitChildren(self)




    def compOp(self):

        localctx = SailingParser.CompOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_compOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            _la = self._input.LA(1)
            if not(((((_la - 147)) & ~0x3f) == 0 and ((1 << (_la - 147)) & 31) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def METROW(self):
            return self.getToken(SailingParser.METROW, 0)

        def KABELTOW(self):
            return self.getToken(SailingParser.KABELTOW, 0)

        def MIL_MORSKICH(self):
            return self.getToken(SailingParser.MIL_MORSKICH, 0)

        def JARDOW(self):
            return self.getToken(SailingParser.JARDOW, 0)

        def getRuleIndex(self):
            return SailingParser.RULE_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnit" ):
                listener.enterUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnit" ):
                listener.exitUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnit" ):
                return visitor.visitUnit(self)
            else:
                return visitor.visitChildren(self)




    def unit(self):

        localctx = SailingParser.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            _la = self._input.LA(1)
            if not(((((_la - 138)) & ~0x3f) == 0 and ((1 << (_la - 138)) & 101) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





