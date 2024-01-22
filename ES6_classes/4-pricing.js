import Currency from "./3-currency.mjs";

export default class Pricing {
    constructor(amount , currency) {
        if (typeof(amount) == 'number') {
            this._amount = amount
        }
        else {
            throw TypeError('Amount must be a number')
        }
        if (typeof(currency) == 'object'){
            this._currency = currency
        }
        else {
            throw TypeError('Currency must be an object')
        }
    }

    get amount() {
        return this._amount
    }

    set amount(newamount) {
        if (typeof(newamount) == 'number') {
            this._amount = newamount
        }
        else {
            throw TypeError('Amount must be a number')
        } 
    }

    get currency() {
        return this._currency
    }

    set currency(newcurrency) {
        if (typeof(newcurrency) == 'object'){
            this._currency = newcurrency
        }
        else {
            throw TypeError('Currency must be an object')
        }
    }
    
    displayFullPrice() {
        return `${this._amount} ${this.currency.name} (${this.currency.code})`
    }

    convertPrice(amount, conversion_rate) {
        if (typeof(amount) == 'number' && typeof(conversion_rate) == 'number') {
            return amount * conversion_rate
        }
        else {
            throw TypeError('Both arguments must be numbers')
        }
    }
}
