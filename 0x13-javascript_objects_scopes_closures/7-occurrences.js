#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let occurence = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occurence += 1;
    }
  }
  return (occurence);
}

module.exports = {
  nbOccurences
};
