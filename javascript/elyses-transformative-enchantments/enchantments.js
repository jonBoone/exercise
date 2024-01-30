// @ts-check

/**
 * Double every card in the deck.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with every card doubled
 */
export function seeingDouble(deck) {
    return deck.map((card) => card * 2);
}

/**
 *  Creates triplicates of every 3 found in the deck.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with triplicate 3s
 */
export function threeOfEachThree(deck) {
    // gather the indices of the existing 3's in deck
    let indices = [];

    for (let i = 0; i < deck.length; i++) {
        if (deck[i] == 3) {
            indices.push(i);
        }
    }

    // splice the two extra 3's into deck
    // note: all original deck indices > 0 must be offset by 2
    for (let j = 0; j < indices.length; j++) {
            deck.splice(indices[j] == 0 ? 0 : indices[j] + 2,0,3,3);
    }

    return deck;
}

/**
 * Extracts the middle two cards from a deck.
 * Assumes a deck is always 10 cards.
 *
 * @param {number[]} deck of 10 cards
 *
 * @returns {number[]} deck with only two middle cards
 */
export function middleTwo(deck) {
    // zero-based indexing means midpoint is 1 past the actual midpoint
    let midpoint = (deck.length / 2);

    return [deck[midpoint - 1], deck[midpoint]];
}

/**
 * Moves the outside two cards to the middle.
 *
 * @param {number[]} deck with even number of cards
 *
 * @returns {number[]} transformed deck
 */

export function sandwichTrick(deck) {
    let midpoint = (deck.length / 2) - 1;
    let firstCard = deck.shift();
    let lastCard = deck.pop();
    deck.splice(midpoint, 0, lastCard, firstCard);
    return deck;
}

/**
 * Removes every card from the deck except 2s.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with only 2s
 */
export function twoIsSpecial(deck) {
    let numCards = deck.length;
    let twos = deck.filter((value) => value == 2);
    deck.splice(0,numCards);
    for (let i = 0; i < twos.length; i++) {
        deck.splice(i,0,twos[i]);
    }
    return deck;
}

/**
 * Returns a perfectly order deck from lowest to highest.
 *
 * @param {number[]} deck shuffled deck
 *
 * @returns {number[]} ordered deck
 */
export function perfectlyOrdered(deck) {
    return deck.sort((item1, item2) => {
        if (Number(item1) < Number(item2)) {
            return -1;
        } else if (Number(item1) > Number(item2)){
            return 1;
        }
        // ensure stable sort
        return 0;
    });
}

/**
 * Reorders the deck so that the top card ends up at the bottom.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} reordered deck
 */
export function reorder(deck) {
    return deck.reverse();
}
