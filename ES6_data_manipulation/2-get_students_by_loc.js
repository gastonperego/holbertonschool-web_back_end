export default function getStudentsByLocation(array, city) {
  return array.filter((obj) => obj.location === city);
}
