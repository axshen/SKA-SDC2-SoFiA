from astropy.io.votable import parse_single_table, from_table, writeto
from astropy.table import Table, vstack

print("Loading catalogue 1");
table = parse_single_table("catalogues/sofia_sdc2_001_cat.xml").to_table();

for i in range(2, 81):
	print("Loading catalogue {:d}".format(i));
	table2 = parse_single_table("catalogues/sofia_sdc2_{:03d}_cat.xml".format(i)).to_table();
	table = vstack([table, table2]);

print("Writing merged catalogue");
votable = from_table(table);
writeto(votable, "merged_catalogue.xml");
