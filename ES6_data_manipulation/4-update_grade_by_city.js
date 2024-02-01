export default function updateStudentGradeByCity(students, city, grades) {
  let filtered_students = students.filter((student) => student.location === city)
  let updated = filtered_students.map((student) => {
    let grade = 'N/A';
    for (const g of grades) {
      if (g.studentId === student.id) {
        grade = g.grade;
      }
    }
    return { ...student, grade };
  });
  return updated
}
