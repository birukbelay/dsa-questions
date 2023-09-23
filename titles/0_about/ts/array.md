

var length = numbers.push(10); -> returns the modified array

var length = numbers.pop(); -> returns the poped value

> for .. of
for (let value of iterable) {
  value += 1;
  console.log(value);
}

for(let i = 0; i < myArray.length; i++){ 
console.log(myArray[i]);
}

```typescript
for (const [index, name] of names.entries()) { 
  console.log(`Hello ${name}, your index is ${index}!`);
}
```

> forEach

```typescript
// We also could use the Array.prototype.forEach method to perform the iteration over the values and indexes.
names.forEach((name, index) => {
  console.log(`Hello ${name}, your index is ${index}!`);
});

// There are scenarios where forEach adds value. For instance, when you want to create a new variable within the loop, forEach creates a new instance, where the for loop will assign a new value.


```
But using this way you cannot break the iteration.

> for ...in
```typescript
// Another form of the for loop is for...in. This can be used with an array, list, or tuple. The for...in loop iterates through a list or collection and returns an index on each iteration.
let arr = [10, 20, 30, 40];

for (var index in arr) {
  console.log(index); // prints indexes: 0, 1, 2, 3

  console.log(arr[index]); // prints elements: 10, 20, 30, 40
}


Do not use for in over an Array if the index order is important.
It is better to use a for loop, a for of loop, or Array.forEach() when the order is important.
// The index order is implementation-dependent, and array values may not be accessed in the order you expect.
```