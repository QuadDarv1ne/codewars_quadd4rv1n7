/**
 * Функция решает задачу нахождения значения неизвестного знака (?), который заменяется на цифру от 0 до 9.
 * Входное выражение представляет собой математическое уравнение, в котором одна или несколько цифр заменены на знак вопроса (?).
 * Мы должны найти минимальную возможную цифру для знака вопроса, чтобы уравнение стало истинным.
 * 
 * Алгоритм:
 * 1. Заменяет символ `=` на `==`, чтобы уравнение стало валидным для проверки с помощью функции `eval()`.
 * 2. Обрабатывает случаи с двойным минусом (`--`), заключая их в скобки для корректной работы с `eval()`.
 * 3. Для каждой цифры от 0 до 9 заменяет все знаки вопроса на текущую цифру и проверяет корректность выражения.
 * 4. Для цифры 0 дополнительно проверяет, чтобы не было некорректных чисел с ведущими нулями (например, 012).
 * 5. Если выражение становится истинным, возвращает найденную цифру. Если ни одна цифра не подходит, возвращает -1.
 * 
 * @param {string} exp - Входное строковое математическое выражение с неизвестными знаками (?), которые нужно заменить на цифры.
 * @returns {number} - Минимальная цифра, которая заменяет все знаки вопроса и делает выражение истинным, или -1, если решения нет.
 */
function solveExpression(exp) {
  console.log('------------------new------------------');
  console.log(exp);
  let op = '+-*=';
  let arr = []
  //  making 'exp' to an actual conditional expression
  exp = exp.replace('=','==');
  //  '--' is not acceptable on 'eval', so parenthesize them.
  if((idx = exp.indexOf('--')) !== -1){
    let idx2 = exp.indexOf('==');
    let temp = exp.split``;
    temp.splice(idx+1, 0, '(');
    temp.splice(idx2+1, 0, ')');
    exp = temp.join``;
  }
  
  //  replacing '?' to 0 -> 9
  console.log(exp);
  for(let i = 0; i <= 9; i++){
    let temp = exp.replace(/\?/g, i);
    
    //  when it's 0, there're more things to check
    if(i === 0){
      let flag = false;
      for(let j = 0; j < temp.length; j++){
        console.log('inner',j);
        if(temp[j] == 0 && (j-1 < 0 || op.indexOf(temp[j-1]) !== -1) && !(j+1 >= temp.length || op.indexOf(temp[j+1]) !== -1)){
          flag = true;
          break;
        }
      }
      console.log('flag',flag);
      if(flag) continue;
    }
    
    //  check if the new expression is correct.
    console.log(temp);
    if(exp.indexOf(String(i)) === -1 && eval(temp)){
      console.log('answer', i);
      return i;
    }
  }
  
  //  if all failed, nothing is possible.
  return -1;
}

/*
Хижина программиста Æ 
https://t.me/hut_programmer_07  
@quadd4rv1n7
*/
