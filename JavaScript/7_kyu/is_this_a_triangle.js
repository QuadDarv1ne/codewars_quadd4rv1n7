/*
Is this a triangle ?

Implement a function that accepts 3 integer values a, b, c.
The function should return true if a triangle can be built with the sides of given length and false in any other case.
(In this case, all triangles must have surface greater than 0 to be accepted).

Examples:
Input -> Output
1,2,2 -> true
4,2,3 -> true
2,2,2 -> true
1,2,3 -> false
-5,1,3 -> false
0,2,3 -> false
1,2,9 -> false
*/


function isTriangle(a, b, c) {
    return a > 0 && b > 0 && c > 0 && a + b > c && b + c > a && c + a > b;
}


// Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
// Дата: 29.11.2024

/*
Хижина программиста Æ 
https://t.me/hut_programmer_07  
@quadd4rv1n7
*/
