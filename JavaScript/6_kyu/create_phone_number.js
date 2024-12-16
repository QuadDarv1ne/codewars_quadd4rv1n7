/*
[ EN: Create Phone Number ]
[ RU: Создание телефонного номера ]

Напишите функцию, которая принимает массив из 10 целых чисел (в диапазоне от 0 до 9)
и возвращает строку в формате телефонного номера.

Пример:
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) 
// => возвращает "(123) 456-7890"

Возвращённый формат должен быть строго правильным для успешного выполнения задачи.
Не забудьте про пробел после закрывающей скобки.
*/

function createPhoneNumber(numbers) {
  // Формируем строку с использованием массива и шаблонных строк
  return `(${numbers.slice(0, 3).join('')}) ${numbers.slice(3, 6).join('')}-${numbers.slice(6, 10).join('')}`;
}

/*
Альтернативная реализация:
function createPhoneNumber(numbers){
var format = "(xxx) xxx-xxxx";

for(var i = 0; i < numbers.length; i++)
{
  format = format.replace('x', numbers[i]);
}

return format;
}
*/


// Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
// Дата: 30.11.2024
