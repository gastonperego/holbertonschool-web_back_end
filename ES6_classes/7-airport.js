export default class Airport {
    constructor(name, code) {
        if (typeof(name) === 'string') {
            this._name = name
        }
        else {
            throw TypeError('Name must be a string')
        }
        if (typeof(code) === 'string') {
            this._code = code
        }
        else {
            throw TypeError('Name must be a string')
        }
    }

    toString() {
        return `[object ${this._code}]`
    }
}