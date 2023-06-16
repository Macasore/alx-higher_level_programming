const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c = 'X') {
    const row = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) console.log(row);
  }
}

module.exports = Square;
