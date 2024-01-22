export default class HolbertonClass {
    constructor(size, location) {
        if (typeof(size) === 'number') {
            this._size = size
        }
        else {
            throw TypeError('Size must be a nimber')
        }
        if (typeof(location) === 'string') {
            this._location = location
        }
        else {
            throw TypeError('location must be a string')
        }
        
    }

    toString() {
        return this._location
    }

    valueOf() {
        return this._size
    }
}