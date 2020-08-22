#out exception list 
out = ['посёлок', 'деревня', 'село', 'городской', 'городского', 'товарищество']

def change_name(row):
    new_lst = []
    lst = row.split()
    for element in lst:
        if element not in out:
            new_lst.append(element)
    if len(new_lst) >= 2:
        new_name = ' '.join(str(e) for e in new_lst)
    else:
        new_name = ''.join(new_lst)
    return new_name

df['locality_name'] = df['locality_name'].apply(change_name)
