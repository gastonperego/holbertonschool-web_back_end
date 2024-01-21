export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof(name) == 'string') { 
      this._name = name;
    }
    else {
      throw new TypeError('Name must be a string');
    }
    if (typeof(length) == 'number') { 
      this._length = length;
    }
    else {
      throw new TypeError('Length must be a number');
    }
    if (typeof(students) == 'object') { 
      this._students = students;
    }
    else {
      throw new TypeError('Students must be an array');
    }
  }
  get name() {
    return this._name
  }
  
  set name(new_name) {
    if (typeof(new_name) == 'string') { 
      this._name = new_name;
    }
    else {
      throw new TypeError('Name must be a string');
    }
  }
  
  get length() {
    return this._length
  }
  
  set length(new_length) {
    if (typeof(length) == 'number') { 
      this._length = length;
    }
    else {
      throw new TypeError('Length must be a number');
    }
  }
  
  get students() {
    return this._students
  }
  
  set students(new_students) {
    if (typeof(students) == 'object') { 
      this._students = new_students;
    }
    else {
      throw new TypeError('Students must be an array');
    }
  }
}
