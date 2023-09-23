## maps

A Map allows storing `key-value` pairs (i.e. entries)


> creating empty map

```typescript
    let myMap = new Map<string, number>();
```

The common operations available in a Map are:

`map.set(key, value)` – adds a new entry in the Map.
`map.get(key)` – retrieves the value for a given key from the Map.
`map.has(key)` – checks if a key is present in the Map. Returns true or false.
`map.size` – returns the count of entries in the Map.
`map.delete(key)` – deletes a key-value pair using its key. If key is found and deleted, it returns true, else returns false.
`map.clear()` – deletes all entries from the Map.

### 3. Iterating over Map
Use `for...of` loop to iterate over map keys, values, or entries.

`map.keys()` – to iterate over map keys
`map.values()` – to iterate over map values
`map.entries()` – to iterate over map entries
`map` – use object destructuring to iterate over map entries


```typescript

let nameAgeMapping = new Map<string, number>();

    //1. Iterate over map keys
for (let key of nameAgeMapping.keys()) {
    console.log(key);                   //Lokesh Raj John
}

//2. Iterate over map values
for (let value of nameAgeMapping.values()) {
    console.log(value);                 //37 35 40
}

//3. Iterate over map entries
for (let entry of nameAgeMapping.entries()) {
    console.log(entry[0], entry[1]);    //"Lokesh" 37 "Raj" 35 "John" 40
}

//4. Using object destructuring
for (let [key, value] of nameAgeMapping) {
    console.log(key, value);            //"Lokesh" 37 "Raj" 35 "John" 40
}



```

```typescript
const map1 = new Map([
  ['country', 'Chile'],
  ['age', 30],
]);
    const keys = [...map1.keys()]; // 👉️ ['country, 'age']
const values = [...map1.values()]; // 👉️ ['Chile', 30]
```
