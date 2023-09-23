
## arrays
- in java arrays are predefined & of fixed size
```java
int[] nums = {25, 87, 69, 55};
// iterate
for (int number: nums) {
    System.out.println(number);
}

// indexing
int num = nums[index];

int N = nums.length;
for (int i=0; i<N; i++){     
             
}

// Define empty one with size
String names[] = new String[10];

// Array of objects with 4 elements
 Car cars[] = new Car[4];

  Car cars[] = {
                new Car("Toyota", 56600),
                new Car("Honda", 63500),                
        };

// to copy arrays
import java.util.Arrays;
String arrNew[] = Arrays.copyOf(arr, arr.length + 1);
```

## Arraylist

- in java arraylists are dynamic


```java
ArrayList<String> cars = new ArrayList<String>();
cars.add("toyota");
// acess by index
cars.get(0);
cars.set(0, "Opel");
cars.remove(0);
cars.clear();
cars.size();

//iterate
for (String i : cars) {
      System.out.println(i);
}
//Sort
Collections.sort(cars);  // Sort cars
```