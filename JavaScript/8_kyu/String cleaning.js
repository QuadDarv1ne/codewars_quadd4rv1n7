/**
 * Функция удаляет все цифры из строки, оставляя все остальные символы (буквы, пробелы, спецсимволы).
 * 
 * Например:
 * stringClean('! !') => '! !'
 * stringClean('123456789') => ''
 * stringClean('This looks5 grea8t!') => 'This looks great!'
 * 
 * @param {string} s - строка, из которой необходимо удалить все цифры.
 * @returns {string} - строка без цифр, остальные символы остаются на месте.
 */
function stringClean(s) {
  return s.replace(/[0-9]/g, '');
}
