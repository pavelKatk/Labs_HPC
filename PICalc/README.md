<h1> Calculate PI using the Monte Carlo method </h1>
<b> Results </b>

<html>
<head>
<meta charset="utf-8">
</head>
<body>
<table border="1">
<tr>
<th>Points count</th>
<th>time CPU (sec.)</th>
<th>time GPU (sec.)</th>
<th>time_CPU / time_GPU</th>
<th> Value Pi </th>
</tr>
<tr><td>65536</td><td>0.04732</td><td>0.00066</td><td>71.49</td><td>3.15942</td></tr>
<tr><td>65536*2</td><td>0.0992</td><td>0.00111</td><td>89.54</td><td>3.13763</td></tr>
<tr><td>65536*4</td><td>0.1885</td><td>0.00128</td><td>147.052</td><td>3.14277</td></tr>
<tr><td>65536*8</td><td>0.39116</td><td>0.002</td><td>195.06</td><td>3.13762</td></tr>
<tr><td>65536*16</td><td>0.7513</td><td>0.003</td><td>252.90</td><td>3.1416</td></tr>
</table>
</body>
</html>
