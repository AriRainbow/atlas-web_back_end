export default function getStudentIdSum(students) {
  return students.reduce((sum, student) => sum + student.id, 0);
}
