export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof(name) == 'string') { 
      this._name = name;
    }
    if (typeof(length) == 'number') { 
      this._length = length;
    }
    if (typeof(students) == 'object') { 
      this._students = students;
    }
  }
  get name() {
    return this._name
  }

  set name(new_name) {
    if (typeof(new_name) == 'string') { 
      this._name = new_name;
    }
  }
  
  get length() {
    return this._length
  }

  set length(new_length) {
    if (typeof(length) == 'number') { 
      this._length = length;
    }
  }

  get students() {
    return this._students
  }

  set students(new_students) {
    if (typeof(students) == 'object') { 
      this._students = new_students;
    }
  }
}
