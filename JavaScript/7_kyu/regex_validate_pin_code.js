/*
[ Regex validate PIN code ]

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
*/


function validatePIN (pin) {
    return /^(\d{4}|\d{6})$/.test(pin);
 }


// Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
// Дата: 29.11.2024

/*
Хижина программиста Æ 
https://t.me/hut_programmer_07  
@quadd4rv1n7
*/
