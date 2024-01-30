/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

export function cookingStatus(timer) {
    switch (timer) {
    case 0:
        return 'Lasagna is done.'
    case undefined:
        return 'You forgot to set the timer.'
    default:
        return 'Not done, please wait.'
    };
};

export function preparationTime(layers, avgLayerPrepTime = 2) {
    let estimate = 0;
    for (let i = 0; i < layers.length; i++) {
        estimate += avgLayerPrepTime;
    };
    return estimate;
};

export function quantities(layers) {
    let sauce = 0;
    let noodles = 0;
    for (let i = 0; i < layers.length; i++) {
        switch (layers[i]) {
        case 'sauce':
            sauce += 0.2;
            break
        case 'noodles':
            noodles += 50;
        default:
            break
        };
    };
    return {'noodles': noodles, 'sauce': sauce};
};

export function addSecretIngredient(friendsList, myList) {
    myList.push(friendsList[friendsList.length - 1]);
};

export function scaleRecipe(recipe, portions) {
    let scaleFactor = portions / 2;
    let newRecipe = {};
    for (let key in recipe) {
        newRecipe[key] = recipe[key] * scaleFactor;
    };
    return newRecipe;
};
