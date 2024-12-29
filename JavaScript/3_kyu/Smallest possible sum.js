const { expect } = require('chai');

/**
 * Функция для нахождения минимальной суммы массива после последовательных преобразований.
 * 
 * В этой задаче выполняется операция, при которой элементы массива X преобразуются по следующему правилу:
 * если X[i] > X[j], то X[i] = X[i] - X[j]. Операция выполняется до тех пор, пока не будет достигнут
 * такой результат, когда элементы массива станут одинаковыми.
 * 
 * После того как все элементы массива станут одинаковыми, результатом будет их сумма.
 * Суть задачи сводится к вычислению наибольшего общего делителя (НОД) для всех элементов массива.
 * Все элементы массива после преобразований будут равны этому НОД, и сумма будет равна НОД, умноженному
 * на количество элементов в массиве.
 * 
 * @param {number[]} numbers Массив положительных целых чисел.
 * @returns {number} Сумма массива после преобразований, когда все элементы становятся равными.
 */
function solution(numbers) {
  // Начинаем с первого элемента массива и вычисляем НОД для всех элементов
  let currentGcd = numbers[0];
  
  // Проходим по массиву и вычисляем НОД всех чисел
  for (let i = 1; i < numbers.length; i++) {
    currentGcd = gcd(currentGcd, numbers[i]);
  }
  
  // Возвращаем сумму массива, где все элементы равны НОД, умноженному на количество элементов
  return currentGcd * numbers.length;
}

/**
 * Вспомогательная функция для вычисления НОД двух чисел с использованием алгоритма Евклида.
 * 
 * @param {number} a Первое число.
 * @param {number} b Второе число.
 * @returns {number} НОД чисел a и b.
 */
function gcd(a, b) {
  while (b !== 0) {
    const temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}
