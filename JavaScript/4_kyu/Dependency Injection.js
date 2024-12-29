/**
 * Конструктор DependencyInjector
 * @param {Object} dependency - объект с зависимостями
 */
var DI = function (dependency) {
  this.dependency = dependency;
};

/**
 * Метод для инъекции зависимостей в функцию.
 * Этот метод принимает функцию, которая имеет зависимости в качестве параметров.
 * Зависимости разрешаются автоматически из объекта, переданного в конструктор DI.
 * 
 * Функция, переданная в метод, будет возвращена с разрешенными зависимостями,
 * которые автоматически подставляются в соответствующие параметры функции.
 * Если функция имеет вложенные функции, они не обрабатываются.
 * 
 * @param {Function} func - Функция, в которую нужно инжектировать зависимости.
 * 
 * @returns {Function} - Новая функция с инжектированными зависимостями.
 */
DI.prototype.inject = function (func) {
  var self = this;

  // Проверяем, что func действительно является функцией
  if (typeof func !== 'function') {
    throw new Error('Argument must be a function');
  }

  // Возвращаем новую функцию, которая будет вызывать оригинальную функцию
  return function () {
    // Получаем имена параметров функции
    var paramNames = func.toString()
      .match(/function\s.*\(([^)]*)\)/);

    if (!paramNames || !paramNames[1]) {
      return func(); // Если параметры не найдены, вызываем функцию без аргументов
    }

    paramNames = paramNames[1]
      .split(',')
      .map(function (param) { return param.trim(); });

    // Создаем массив зависимостей в правильном порядке
    var dependencies = paramNames.map(function (param) {
      return self.dependency[param] || undefined; // Возвращаем undefined, если зависимость не найдена
    });

    // Вызываем оригинальную функцию с разрешенными зависимостями
    return func.apply(null, dependencies);
  };
};
