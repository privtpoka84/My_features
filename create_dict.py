#values is keyes for future dict
#table place were is keyes and values for keyes
#column1 keyes from table
#column2 values for keyes from table


def create_dict(values, table, column1, column2):
	dictionary = {}
	for i in values:
		for j in range(len(table)):
			if i == table.loc[j, column1]:
				dictionary[i] = table.loc[j, column2]
	return dictionary
