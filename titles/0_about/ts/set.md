# set

A typescript Set allows us to store distinct values in a List.
```typescript
    // empty set
    let directions = new Set<string>();
    // Set with initial values
    let directions = new Set<string>(['east', 'west']);
```

`set.add(v)` – adds values into the Set.
`set.has(v)` – checks the existence of a value in the Set.
`set.delete(v)` – deletes a value from the Set.
`set.clear()` – clear all values from the Set.
`set.size` – ‘size‘ property will return size of Set.


> iterating over set

```typescript

let diceEntries = new Set<number>();
 
//Added 6 entries into the set
diceEntries.add(1).add(2).add(3).add(4).add(5).add(6);
 
//Iterate over set entries
for (let currentNumber of diceEntries) {
    console.log(currentNumber);     //Prints 1 2 3 4 5 6
}
 
// Iterate set entries with forEach
diceEntries.forEach(function(value) {
  console.log(value);               //Prints 1 2 3 4 5 6
});

```