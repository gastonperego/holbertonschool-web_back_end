import Currency from './3-currency.mjs';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof (amount) == 'number') {
      this._amount = amount;
    } else {
      throw new TypeError('Amount must be a number');
    }

    if (currency instanceof Currency) {
      this._currency = currency;
    } else {
      throw new TypeError('Currency must be a currency object');
    }
  }

  get amount() {
    return this._amount;
  }

  set amount(newamount) {
    if (typeof (newamount) == 'number') {
      this._amount = newamount;
    } else {
      throw new TypeError('Amount must be a number');
    }
  }

  get currency() {
    return this._currency;
  }

  set currency(newcurrency) {
    if (newcurrency instanceof Currency) {
      this._currency = newcurrency;
    } else {
      throw new TypeError('Currency must be a currency object');
    }
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}