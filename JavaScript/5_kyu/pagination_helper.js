/*
[ PaginationHelper ]

For this exercise you will be strengthening your page-fu mastery.
You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.

The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page.
The types of values contained within the collection/array are not relevant.

    The following are some examples of how this class is used:
    var helper = new PaginationHelper(['a','b','c','d','e','f'], 4);
    helper.pageCount(); // should == 2
    helper.itemCount(); // should == 6
    helper.pageItemCount(0); // should == 4
    helper.pageItemCount(1); // last page - should == 2
    helper.pageItemCount(2); // should == -1 since the page is invalid

    // pageIndex takes an item index and returns the page that it belongs on
    helper.pageIndex(5); // should == 1 (zero based index)
    helper.pageIndex(2); // should == 0
    helper.pageIndex(20); // should == -1
    helper.pageIndex(-10); // should == -1
*/


class PaginationHelper {
    /**
     * Конструктор принимает массив элементов и число, указывающее, сколько элементов помещается на одной странице
     * @param {Array} collection - Массив элементов
     * @param {number} itemsPerPage - Количество элементов на странице
     */
    constructor(collection, itemsPerPage) {
      this.collection = collection;
      this.itemsPerPage = itemsPerPage;
    }
  
    /**
     * Возвращает общее количество элементов в коллекции
     * @returns {number}
     */
    itemCount() {
      return this.collection.length;
    }
  
    /**
     * Возвращает общее количество страниц
     * @returns {number}
     */
    pageCount() {
      return Math.ceil(this.collection.length / this.itemsPerPage);
    }
  
    /**
     * Возвращает количество элементов на указанной странице.
     * Индекс страницы начинается с нуля.
     * @param {number} pageIndex - Индекс страницы
     * @returns {number} - Количество элементов на странице или -1, если индекс страницы недействителен
     */
    pageItemCount(pageIndex) {
      if (pageIndex < 0 || pageIndex >= this.pageCount()) {
        return -1;
      }
      if (pageIndex === this.pageCount() - 1) {
        return this.collection.length % this.itemsPerPage || this.itemsPerPage;
      }
      return this.itemsPerPage;
    }
  
    /**
     * Определяет, на какой странице находится элемент. Индекс начинается с нуля.
     * @param {number} itemIndex - Индекс элемента в коллекции
     * @returns {number} - Индекс страницы или -1, если индекс элемента недействителен
     */
    pageIndex(itemIndex) {
      if (itemIndex < 0 || itemIndex >= this.collection.length) {
        return -1;
      }
      return Math.floor(itemIndex / this.itemsPerPage);
    }
  }  


// Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
// Дата: 16.12.2024
