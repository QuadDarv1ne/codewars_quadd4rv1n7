/*
[ EN: Split Strings ]

Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
*/


function solution(str){
    // Если длина строки нечетная, добавляем '_'
    if (str.length % 2 !== 0) {
        str += '_';
    }
    // Разбиваем строку на пары по 2 символа
    let result = [];
    for (let i = 0; i < str.length; i += 2) {
        result.push(str.slice(i, i + 2));
    }
    return result;
}


// Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
// Дата: 30.11.2024
