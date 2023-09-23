/**
 * 
Given an integer array arr and a mapping function fn, return a new array with a transformation applied to each element.

The returned array should be created such that returnedArray[i] = fn(arr[i], i).

Please solve it without the built-in Array.map method.
 */
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/submissions/
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    return arr.map((k,i)=>fn(k,i))
};

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var mapp = function(arr, fn) {
    const newArr = new Array(arr.length);
    for (i=0; i< arr.length; i++){
        newArr[i]= fn(arr[i],i)
    }
    return newArr
};

function maps(arr: number[], fn: (n: number, i: number) => number): number[] {
    const newArr= new Array(arr.length)
    for (let i=0; i< arr.length; i++){
        newArr[i]= fn(arr[i],i)
    }
    return newArr
};