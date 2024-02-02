export default function updateUniqueItems(map) {
  for (const array of map) {
    if (array[1] === 1) {
        map.set(array[0], 100);
    }
  }
  return map;
}
