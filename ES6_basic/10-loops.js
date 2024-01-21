export default function appendToEachArrayValue(array, appendString) {
  let array2 = []  
  for (const idx of array) {
      const value = array[idx];
      array2[idx] = appendString + value;
    }
  
    return array2;
  }