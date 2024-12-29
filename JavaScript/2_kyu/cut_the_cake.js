/** 
 * Преобразует двумерный массив в строку, где каждый элемент массива соединяется в строку, 
 * а строки разделяются символом новой строки.
 * @param {Array} cake - Двумерный массив, представляющий торт.
 * @returns {string} Строка, представляющая торт.
 */
function stringify(cake) {
	return cake.map((e) => e.join("")).join("\n");
}

/** 
 * Проверяет, является ли предложенный срез (кусок торта) допустимым.
 * Кусок считается недопустимым, если он выходит за границы торта или содержит больше одного "O" (что значит, что кусок уже был вырезан).
 * @param {Array} cake - Двумерный массив, представляющий торт.
 * @param {number} x - Координата x верхнего левого угла среза.
 * @param {number} y - Координата y верхнего левого угла среза.
 * @param {number} width - Ширина среза.
 * @param {number} height - Высота среза.
 * @returns {string|boolean} Строковое представление среза, если он допустим, или false, если срез недопустим.
 */
function isAValidSlice(cake, x, y, width, height) {
	// Проверка на выход за границы
	if (x + width > cake[0].length) return false;
	if (y + height > cake.length) return false;

	// Реальный срез
	const slice = cake.slice(y, y + height).map((e) => e.slice(x, x + width));
	const slice_str = stringify(slice);

	// Если срез содержит "x", это значит, что кусок уже был вырезан
	if (slice_str.match(/x/)) {
		return false;
	}

	// Если срез содержит ровно один "O", это допустимый срез
	const numberOfO = (slice_str.match(/o/g) || []).length;
	if (numberOfO != 1) {
		return false;
	}

	// Возвращаем срез
	return slice_str;
}

/** 
 * Выполняет разрез торта, помечая вырезанный кусок символами "x".
 * @param {Array} cake - Двумерный массив, представляющий торт.
 * @param {number} x - Координата x верхнего левого угла среза.
 * @param {number} y - Координата y верхнего левого угла среза.
 * @param {number} width - Ширина среза.
 * @param {number} height - Высота среза.
 * @returns {Array} Новый массив торта с выполненным разрезом.
 */
function doCut(cake, x, y, width, height) {
	for (let i = y; i < y + height; i++) {
		for (let j = x; j < x + width; j++) {
			cake[i][j] = "x";
		}
	}
	return cake;
}

/** 
 * Находит верхний левый угол первого непорезанного куска торта.
 * @param {Array} cake - Двумерный массив, представляющий торт.
 * @returns {Array|null} Координаты верхнего левого угла первого непорезанного куска (в формате [y, x]) или null, если весь торт порезан.
 */
function findFirstTopLeftCorner(cake) {
	for (let i = 0; i < cake.length; i++) {
		for (let j = 0; j < cake[i].length; j++) {
			if (cake[i][j] !== "x") {
				return [i, j];
			}
		}
	}
}

/** 
 * Основная функция для поиска всех возможных срезов торта.
 * Алгоритм рекурсивно пробует все возможные размеры срезов от максимального к минимальному.
 * @param {Array} cake - Двумерный массив, представляющий торт.
 * @param {number} size - Размер каждого среза (ширина * высота).
 * @param {Array} slices - Массив, в котором хранятся все успешные срезы.
 * @returns {Array} Массив строковых представлений срезов, если все срезы выполнены корректно, или пустой массив, если это невозможно.
 */
function run(cake, size, slices) {
	// Поиск верхнего левого угла первого непорезанного куска
	const corner = findFirstTopLeftCorner(cake);
	if (null == corner) return slices;

	let x = corner[1];
	let y = corner[0];

	// Перебор всех возможных размеров срезов
	for (let width = size; width >= 1; width--) {
		for (let height = 1; height <= size; height++) {
			if (height * width !== size) continue;

			// Проверка на допустимость среза
			const slice = isAValidSlice(cake, x, y, width, height);
			if (!slice) continue;

			// Добавление среза в список и выполнение разреза
			const newSlices = Object.assign([], slices);
			newSlices.push(slice);

			// Создание нового торта с выполненным разрезом
			let newCake = doCut(
				JSON.parse(JSON.stringify(cake)),
				x,
				y,
				width,
				height
			);

			// Рекурсивный вызов
			let r = run(newCake, size, newSlices);

			// Если срезы найдены, вернуть их
			if (r.length) {
				return r;
			}
		}
	}

	// Если срезов не найдено, вернуть пустой массив
	return [];
}

/** 
 * Функция для поиска всех возможных срезов торта.
 * @param {string} cake - Строковое представление торта, где "o" — съедобный участок, "x" — вырезанный.
 * @returns {Array} Массив строковых представлений срезов.
 */
function cut(cake) {
	// Количество "O" в строке торта
	const num = cake.match(/o/g).length;
	// Преобразование строки в двумерный массив
	const cake_array = cake.split("\n").map((e) => e.split(""));

	// Определение размера среза
	const rows = cake_array.length;
	const cols = cake_array[0].length;
	const size = (rows * cols) / num;

	// Запуск алгоритма
	return run(cake_array, size, []);
}
