<h2>Compressions algorithms</h2>
<h3>Run-length encoding (RLE)</h3>
Very simple lossless compression algorithm.
https://en.wikipedia.org/wiki/Run-length_encoding


<h3>Lempel–Ziv–Welch (LZW)</h3>
Simple dictionary lossless compression algorithm.
https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch

<h2>Transformations algorithms</h2>

<h3>Burrows–Wheeler transform (BWT)</h3>
Encoding and decoding strings or lists with own alphabets. Been programmed to avoid wasting too much memory - is not using the rotation string, but use the rotation vectors.
https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform

<h3>Move to front (MTF)</h3>
Encoding string or list of chars to list of integers.
Decoding list of integers to string.
This transformation algorithm uses full ASCII stack.
https://en.wikipedia.org/wiki/Move-to-front_transform

<h3>Discrete Cosine transform (DCT)</h3>
Encoding and decoding list of numbers. - only 1D
https://en.wikipedia.org/wiki/Discrete_cosine_transform

<h2>Binary codes and functions</h2>

<h3>Helper functions</h3>

<h2>strBinToInt</h2>
Binary number representation by string convert to integer. For example: '101' to 5

<h2>strOctToInt<h2>
Octet number representation by string convert to integer.

<h2>strHexToInt<h2>
Hexadecimal number representation by string convert to integer.

<h2>intToBinStr<h2>
Integer number convert to binary number representation by string.

<h2>intToOctStr<h2>
Integer number convert to octet number representation by string.

<h2>intToHexStr<h2>
Integer number convert to hexadecimal number representation by string

<h2>length<h2>
Length of binary integer number

<h2>getFirstBits<h2>
<h2>getLastBits<h2>
<h2>getValueInPosition<h2>
<h2>cutFirst<h2>
<h2>cutLast<h2>
<h2>resplitBinaryCodes<h2>

<h3>Binary codes</h3>
<h2>Fibonacci<h2>
<h2>BCD<h2>
