/**
 * Функция для разложения числа на простые множители.
 * 
 * Эта функция принимает положительное число n и возвращает строку, представляющую разложение числа на простые множители в формате:
 * "(p1**n1)(p2**n2)...(pk**nk)", где p(i) - простое число, а n(i) - его степень (если степень больше 1). 
 * Пример: для числа 86240 результат будет "(2**5)(5)(7**2)(11)".
 * 
 * Шаги работы функции:
 * 1. Сначала проверяется количество раз, которое число n делится на 2.
 * 2. Далее функция проверяет возможные простые множители, начиная с 3, и продолжает до квадратного корня из n.
 * 3. Если после проверки всех возможных делителей n остается больше 1, то это простое число, и оно добавляется в результат.
 * 4. Результат возвращается в виде строки, где каждый простое число и его степень представлены в нужном формате.
 * 
 * @param {number} n - Положительное число, которое нужно разложить на простые множители (n > 1).
 * @returns {string} Строка, представляющая разложение числа n на простые множители.
 * 
 * @example
 * primeFactors(86240);  // Возвращает "(2**5)(5)(7**2)(11)"
 * primeFactors(56);     // Возвращает "(2**3)(7)"
 * primeFactors(97);     // Возвращает "(97)"
 * primeFactors(100);    // Возвращает "(2**2)(5**2)"
 */
function primeFactors(n) {
    // Массив для хранения простых множителей и их степеней.
    let factors = [];
    
    // Проверяем, сколько раз число n делится на 2.
    let count = 0;
    while (n % 2 === 0) {
        n /= 2;  // Делим n на 2, пока оно делится.
        count++; // Увеличиваем счетчик степеней.
    }
    // Если на 2 делится хотя бы один раз, добавляем 2 в результат.
    if (count > 0) {
        factors.push(count === 1 ? "(2)" : `(2**${count})`);
    }

    // Проверяем возможные простые множители начиная с 3.
    for (let i = 3; i <= Math.sqrt(n); i += 2) {
        count = 0;
        // Пока n делится на i, делим его и увеличиваем счетчик степеней.
        while (n % i === 0) {
            n /= i;
            count++;
        }
        // Если на i делится хотя бы один раз, добавляем его в результат.
        if (count > 0) {
            factors.push(count === 1 ? `(${i})` : `(${i}**${count})`);
        }
    }

    // Если после всех проверок n все еще больше 1, значит, это простое число.
    if (n > 1) {
        factors.push(`(${n})`);
    }

    // Возвращаем строку, состоящую из множителей и их степеней.
    return factors.join('');
}

/*
Хижина программиста Æ 
https://t.me/hut_programmer_07  
@quadd4rv1n7
*/
