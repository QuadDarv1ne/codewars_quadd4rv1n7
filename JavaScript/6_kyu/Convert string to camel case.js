/*
[ EN: Convert string to camel case ]
[ RU: Преобразование строки в camelCase ]

Задача:
Написать функцию, которая преобразует строку, разделённую дефисами или подчёркиваниями, в camelCase.
Первая буква результирующей строки остаётся строчной, если первая буква исходной строки была строчной.
Все остальные слова начинаются с заглавной буквы.

Примеры:
"the-stealth-warrior" -> "theStealthWarrior"
"The_Stealth_Warrior" -> "TheStealthWarrior"
"The_Stealth-Warrior" -> "TheStealthWarrior"
*/

function toCamelCase(str) {
    // Если строка пуста, сразу возвращаем её
    if (!str) return "";

    // Разделяем строку по дефисам или подчёркиваниям
    let words = str.split(/[-_]/);

    // Обрабатываем каждое слово, начиная со второго: делаем первую букву заглавной
    for (let i = 1; i < words.length; i++) {
        words[i] = words[i][0].toUpperCase() + words[i].slice(1);
    }

    // Объединяем слова обратно в строку
    return words.join("");
}

// Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
// Дата: 16.12.2024
