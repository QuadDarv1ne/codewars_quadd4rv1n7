/*
[ Pick peaks ]
[ Найти вершины ]

В этой задаче вам нужно написать функцию, которая возвращает позиции и значения "вершин" (или локальных максимумов) числового массива.

Например, в массиве arr = [0, 1, 2, 5, 1, 0] есть вершина на позиции 3 со значением 5 (так как arr[3] равно 5).

Результат должен быть представлен в виде объекта с двумя свойствами: pos и peaks. Оба свойства должны быть массивами.
Если в массиве нет вершин, результатом должен быть объект {pos: [], peaks: []}.

Пример: вызов pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) должен вернуть {pos: [3, 7], peaks: [6, 3]} (или эквивалентный результат в других языках).
Все входные массивы будут корректными массивами целых чисел (включая пустые массивы), так что проверять входные данные не нужно.
Первый и последний элементы массива не рассматриваются как вершины (в контексте математической функции мы не знаем, что идёт до первого и после последнего элемента, поэтому они не могут быть вершинами).

Также обратите внимание на плато: массив [1, 2, 2, 2, 1] имеет вершину, тогда как [1, 2, 2, 2, 3] и [1, 2, 2, 2, 2] не имеют.
В случае плато-вершин возвращайте только позицию и значение начала плато.
Например: вызов pickPeaks([1, 2, 2, 2, 1]) должен вернуть {pos: [1], peaks: [2]} (или эквивалентный результат в других языках).

Удачи.
*/


function pickPeaks(arr) {
    let result = { pos: [], peaks: [] }; // Инициализация результата
    let potentialPeakPos = null; // Переменная для хранения позиции начала плато

    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > arr[i - 1]) {
            // Запоминаем начало потенциального пика
            potentialPeakPos = i;
        } else if (arr[i] < arr[i - 1] && potentialPeakPos !== null) {
            // Если есть спад, фиксируем пик
            result.pos.push(potentialPeakPos);
            result.peaks.push(arr[potentialPeakPos]);
            potentialPeakPos = null; // Сбрасываем потенциальный пик
        }
    }

    return result;
}


// Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
// Дата: 16.12.2024