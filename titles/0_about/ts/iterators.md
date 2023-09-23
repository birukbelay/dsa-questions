
```ts
// For...in Loop
// For i  in gives an index of the array
const newArr: number[] = new Array(arr.length);
for (const i in arr) {
    newArr[i] = fn(arr[i], Number(i));
}y

```


> iterating in reverse
```Typescript

// Iterating in reverse
for (const func of functions.reverse()) {
    input = func(input);
}


```
Using `reduceRight()` simplifies the code and provides a more functional programming style solution. The key is to understand how the Array.reduceRight() method works and how it can be applied to this problem.
```Typescript

function compose(arr: F[]): F {
    return (x: number) => arr.reduceRight((acc, f) => f(acc), x);
}
```
Array.reduceRight() is a built-in JavaScript array method that can be used to apply a function to each element of an array, starting from the rightmost element and moving towards the left. It takes two arguments: a reducer function and an optional initial value for the accumulator.
