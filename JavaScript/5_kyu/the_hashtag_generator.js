/*
[ The Hashtag Generator ]

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:
It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

Examples:
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
*/


function generateHashtag(str) {
    // Trim the input string and split it into words
    const words = str.trim().split(/\s+/);
    
    // If the input is empty after trimming, return false
    if (words.length === 0 || words[0] === "") return false;
    
    // Capitalize the first letter of each word and join them with no spaces
    const hashtag = "#" + words.map(word => word[0].toUpperCase() + word.slice(1).toLowerCase()).join("");
    
    // Return false if the hashtag is longer than 140 characters or is empty
    return hashtag.length > 140 || hashtag === "#" ? false : hashtag;
  }
  

// Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
// Дата: 29.11.2024
