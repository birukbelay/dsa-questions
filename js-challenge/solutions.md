# day 5
[2634. Filter Elements from Array](https://leetcode.com/problems/filter-elements-from-array/)

```typescript

function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
    let newArr= []
    for (let i=0; i < arr.length; i++){
        if(fn(arr[i], i)){
            newArr.push(arr[i])
        }
    }
    return newArr
};

```

# day 6

Map reduce
```typescript
const groceries = [
  { id: 173, name: "Soup" }, 
  { id: 964, name: "Apple" },
  { id: 535, name: "Cheese" }
];

/** With filter and map */
var names = groceries
  .filter(item => item.id > 500)
  .map(item => item.name)

/** With reduce */
var names = groceries.reduce((accumulator, val) => {
  if (val.id > 500) {
    accumulator.push(val.name);
  }
  return accumulator;
}, []);

console.log(names); // ["Apple", "Cheese"]

```
[2626. Array Reduce Transformation](https://leetcode.com/problems/array-reduce-transformation)
```typescript
type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    let ans = init
    for (let i=0; i<nums.length;i++){
        // console.log(ans)
        ans = fn(ans, nums[i])
    }
    return ans
};
//  other solutions

var reduce = function(arr, fn, initialVal) {
  let accumulator = initialVal;
  for (const index in arr) {
    accumulator = fn(accumulator, arr[index]);
  } 
    // or
  for (const element of arr) {
      accumulator = fn(accumulator, element);
  }
  return accumulator;
};



```

# day 7
[2629. Function Composition](https://leetcode.com/problems/function-composition/submissions/)
```Typescript

type F = (x: number) => number;

function compose(functions: F[]): F {
	return function(x) {
        for (let i = functions.length - 1; i >= 0; i--) {
          const func = functions[i];
          x=func(x)
        }
        return x
    }
};


```

# day 8

[2666. Allow One Function Call](https://leetcode.com/problems/allow-one-function-call/)

```Typescript
  

```