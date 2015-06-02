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
