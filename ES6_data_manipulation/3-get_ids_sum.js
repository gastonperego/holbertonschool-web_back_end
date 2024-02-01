export default function getStudentIdsSum(array) {
  return array.reduce((lastValue, obj) => lastValue + obj.id, 0);
}
