/**
 * Функция инкрементирует число в конце строки или добавляет 1, если числа нет.
 * 
 * Если строка заканчивается числом, это число увеличивается на 1.
 * Если число имеет ведущие нули, количество цифр сохраняется.
 * Если строка не заканчивается числом, к строке добавляется "1".
 * 
 * Примеры:
 * 
 * incrementString("foo") => "foo1"
 * incrementString("foobar23") => "foobar24"
 * incrementString("foo0042") => "foo0043"
 * incrementString("foo9") => "foo10"
 * incrementString("foo099") => "foo100"
 * 
 * @param {string} strng - строка, которая может содержать число в конце.
 * @returns {string} - строка с инкрементированным числом или строка с добавленным "1".
 */
function incrementString(strng) {
  const match = strng.match(/(\d+)$/);
  
  if (match) {
    const number = match[0];
    const incrementedNumber = (parseInt(number) + 1).toString();
    const paddedNumber = incrementedNumber.padStart(number.length, '0');
    return strng.slice(0, -number.length) + paddedNumber;
  } else {
    return strng + '1';
  }
}
