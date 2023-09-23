```java


HashMap<Character, Integer> letters = new HashMap<Character, Integer>();

HashMap<String, String> capitalCities = new HashMap<String, String>();
capitalCities.put("England", "London");

capitalCities.get("England");
capitalCities.remove("England");
capitalCities.clear();
capitalCities.size();

boolean result= hashMap.containsKey(valueToBeChecked);
boolean result = hashMap.containsValue(valueToBeChecked);


// Iterate over a hash map
for (String i : capitalCities.keySet()) {
  System.out.println(i);
}
// Print values
for (String i : capitalCities.values()) {
  System.out.println(i);
}


```