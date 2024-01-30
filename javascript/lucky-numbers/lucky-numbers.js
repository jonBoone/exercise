// @ts-check


/**
 * Calculates the sum of the two input arrays.
 *
 * @param {number[]} array1
 * @param {number[]} array2
 * @returns {number} sum of the two arrays
 */
export function twoSum(array1, array2) {
    let number1 = 0, number2 = 0;
    for (let i = 0; i < array1.length; i++) {
        number1 = number1 * 10;
        number1 += Number(array1[i]);
    }
    for (let j = 0; j < array2.length; j++) {
        number2 = number2 * 10;
        number2 += Number(array2[j]);
    }
    return number1 + number2;
}

/**
 * Checks whether a number is a palindrome.
 *
 * @param {number} value
 * @returns {boolean} whether the number is a palindrome or not
 */
export function luckyNumber(value) {
    const valueString = String(value);
    const odd = valueString.length % 2;
    const midpoint = Math.floor(valueString.length / 2);
    let palindrome = true;

    for (let i = 0, j = valueString.length - 1; i < midpoint; i++, j--) {
        if (valueString[i] != valueString[j]) {
            palindrome = false;
        };
    };

    return palindrome;
}

/**
 * Determines the error message that should be shown to the user
 * for the given input value.
 *
 * @param {string|null|undefined} input
 * @returns {string} error message
 */
export function errorMessage(input) {
    let value = Number(input);
    switch(input) {
    case undefined:
    case null:
    case '':
        return 'Required field';
    default:
        if (!value) {
            return 'Must be a number besides 0';
        } else {
            return '';
        }
    }
}
