poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

print(len(poem))  # Ask how many letters here

print(poem[0:13])  # Получаем символы от 0 до 13

print(poem.startswith('All'))  # Проверяем начинается ли стихотворение с слов All ?

print(poem.endswith("That's all folks!"))  # Проверяем, правда ли что стих заканчивается выбранными словами

word = "the"
print(poem.find(word))  # Находим первое упоминание слова

print(poem.rfind(word))  # Находим последнее упоминание слова

print(poem.count(word))  # Считаем общее количество слов
