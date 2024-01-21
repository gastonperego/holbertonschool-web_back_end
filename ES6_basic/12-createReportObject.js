export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberOfDepartments(employeesList) {
      let num = 0
      for (let department in employeesList) {
        num += 1
      }
      return num
    }
  }
}
