
''' Create data frames from csv files.
	This code didn't work for v0.7 of pandas, but it did for v1.1
	Specifically, the DataFrame.loc method was missing in 0.7

	Also, this script was written specifically for the workshop. 
	Consider writing something more general.
 '''

import pandas as pd

# Need to mention encoding, doesn't work otherwise:
dat = pd.read_csv('data/cellphoneper100.csv', encoding='utf-8')

# The indices ('row names') are by default 0-indexed. If you
# would rather index by country name, do:
# Note that I changed the name of the first column header to
# 'Country'
dat = dat.set_index('Country')

# Now, you can do:
print dat.loc['Algeria']

# You can also pick out countries like this:
print dat.loc[['Algeria', 'India', 'United States']]

# The above print statements probably didn't yield anything useful,
# as it's too much information to print out.

# So, suppose you wanted to see how many people (per 100) had cellphones
# in the above countries, in say, 2010

print dat.loc[['Algeria', 'India', 'United States'],'2010']



