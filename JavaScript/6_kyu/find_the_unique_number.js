/*
[ Find the unique number ]

There is an array with some numbers.
All numbers are equal except for one.
Try to find it.

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55

It’s guaranteed that array contains at least 3 numbers.
The tests contain some very huge arrays, so think about performance.
*/


function findUniq(arr) {
    // We assume there are at least 3 elements in the array.
    
    // Check the first three numbers to identify the two different values.
    const first = arr[0];
    const second = arr[1];
    
    // If the first two numbers are different, one of them is the unique number
    if (first !== second) {
        // Check which one is unique by comparing the third element
        return arr[2] === first ? second : first;
    }
    
    // If the first two numbers are the same, the unique number must be different
    return arr.find(num => num !== first);
}


// Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
// Дата: 30.11.2024
