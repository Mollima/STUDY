marxes = ['uno', 'duos', 'tres']
separator = ' * '
marxes.append("four")
joined = separator.join(marxes)
print(joined * 28)
separeted = joined.split(separator)
print(separeted)

# Даай разбиратся по срокам, первая строка это наименование, вторая показывает знак,
# который должен разделить их, и для этого, мы к знаку разделения приписываем первую строку,
# нашу масив, и благодаря этому, добавляется разделитель, в другом случае, будет ,бред. Разобрался.