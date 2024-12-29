function high(x) {
  const words = x.split(' ');
  let highestScore = 0;
  let highestScoringWord = '';

  for (const word of words) {
    let score = 0;
    for (const letter of word) {
      score += letter.charCodeAt(0) - 96;  // 'a' is at charCode 97, so we subtract 96 to get its position
    }
    if (score > highestScore) {
      highestScore = score;
      highestScoringWord = word;
    }
  }

  return highestScoringWord;
}
