'''
[ Extract the domain name from a URL ]

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
'''


def domain_name(url):
    # Удаляем протоколы http://, https:// или другие
    url = url.replace("http://", "").replace("https://", "").replace("www.", "")
    # Разделяем строку по символу '/' и берем первый элемент
    domain = url.split('/')[0]
    # Разделяем строку по символу '.' и возвращаем первый элемент
    return domain.split('.')[0]


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 29.11.2024
