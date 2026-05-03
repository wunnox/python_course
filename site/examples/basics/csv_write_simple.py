data=['"Title";"SWX";"Price";"Dividend";"Volume";"Monthly income"\n',
'"Nestle";"NESN";"79";"3.12";"200";"0.66"\n',
'"UBS";"UBSG";"34";"0.84";"300";"0.62"\n',
'"SwissRE";"SREN";"125";"6.28";"400";"1.67"\n'
]

# Write data into a file
with open("example_shares.csv", 'w') as d:
   for line in data:
       d.write(line)
