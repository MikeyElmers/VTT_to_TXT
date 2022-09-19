![orcid](https://img.shields.io/badge/ORCID-0000--0002--3929--788X-green?style=plastic&logo=orcid&url=https://orcid.org/0000-0002-3929-788X)

# VTT_to_TXT 
This script converts all `.vtt` files in the same directory into `.vtt.txt` files. These `.vtt.txt` files can be converted into a [Praat](https://github.com/praat) [1] TextGrid using Francesco Cangemi's TXT to TextGrid `.praat` Script. 

## Motivation
This script was designed to convert the WEBVTT format into a "hh:mm:ss.mmm word" format that can be used to generate a Praat TextGrid (example below).

`.vtt` input 
```
WEBVTT
Kind: captions
Language: en

00:00:02.159 --> 00:00:03.189 align:start position:0%
 
hello

00:00:03.189 --> 00:00:03.199 align:start position:0%
hello
 

00:00:03.199 --> 00:00:05.190 align:start position:0%
hello
we're<00:00:03.439><c> going</c><00:00:03.520><c> to</c><00:00:03.600><c> have</c><00:00:03.760><c> a</c><00:00:03.840><c> quick</c><00:00:04.080><c> look</c><00:00:04.560><c> at</c><00:00:04.799><c> how</c>
```
`.vtt.txt` output
```
00:00:02.159 hello
00:00:03.189
00:00:03.199 we're 
00:00:03.439 going
00:00:03.520 to
00:00:03.600 have
00:00:03.760 a
00:00:03.840 quick
00:00:04.080 look
00:00:04.560 at
00:00:04.799 how
```

## Installation
```
git clone https://github.com/MikeyElmers/VTT_to_TXT
cd VTT_to_TXT
# Put your .vtt files in the VTT_to_TXT directory
python3 VTT_to_TXT.py
```


## Issues/Comments/Suggestions
Please use the [issue tracker](https://github.com/MikeyElmers/VTT_to_TXT/issues).

## References
```[1] Boersma, P. (2002). Praat, a system for doing phonetics by computer.```

## License 
This code is licensed under the terms of the MIT license. See the [LICENSE](https://github.com/MikeyElmers/VTT_to_TXT/blob/main/LICENSE) file for details.
