export default function updateStudentGradeByCity(students, city, grades) {
  const filteredStudents = students.filter((student) => student.location === city);
  const updated = filteredStudents.map((student) => {
    let grade = 'N/A';
    for (const g of grades) {
      if (g.studentId === student.id) {
        grade = g.grade;
      }
    }
    return { ...student, grade };
  });
  return updated;
}
