/**
 * Функция рассчитывает время, которое потребуется черепахе B, чтобы догнать черепаху A.
 * 
 * @param {number} v1 - Скорость черепахи A (в футах в час).
 * @param {number} v2 - Скорость черепахи B (в футах в час).
 * @param {number} g - Преимущество черепахи A в футах (расстояние, на которое A опережает B в начале).
 * 
 * @returns {Array} Массив, содержащий время в формате [часы, минуты, секунды], которое потребуется черепахе B, чтобы догнать черепаху A.
 * Если черепаха B не может догнать черепаху A (когда ее скорость меньше или равна скорости A), возвращается [-1, -1, -1].
 * 
 * Пример:
 * 
 * race(720, 850, 70) => [0, 32, 18]
 * race(80, 91, 37)   => [3, 21, 49]
 * 
 * Описание работы функции:
 * 1. Если скорость черепахи B меньше или равна скорости черепахи A, возвращается [-1, -1, -1], так как B не может догнать A.
 * 2. Рассчитывается время, которое потребуется B, чтобы догнать A, используя разницу в их скоростях и начальное преимущество.
 * 3. Результат времени в часах переводится в формат [часы, минуты, секунды].
 * 
 * @example
 * race(720, 850, 70)  // Возвращает [0, 32, 18]
 * race(80, 91, 37)    // Возвращает [3, 21, 49]
 */


function race(v1, v2, g) {
    // If A is as fast as B or faster, B will never catch A
    if (v1 >= v2) {
        return [-1, -1, -1];
    }

    // Calculate the time it takes for B to catch A
    let timeInHours = g / (v2 - v1);

    // Convert hours to minutes and seconds
    let hours = Math.floor(timeInHours);
    let minutes = Math.floor((timeInHours - hours) * 60);
    let seconds = Math.floor(((timeInHours - hours) * 60 - minutes) * 60);

    // Return the result as an array of [hours, minutes, seconds]
    return [hours, minutes, seconds];
}

/*
Хижина программиста Æ 
https://t.me/hut_programmer_07  
@quadd4rv1n7
*/
