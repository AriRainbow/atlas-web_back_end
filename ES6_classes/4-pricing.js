import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
        throw new TypeError('Amount must be a number';)
    }
    if (!(currency instanceof Currency)) {
      throw new TypeError('Curreny must be a Currency instance');
    }
    this._amount = amount;
    this._currency = currency;
  }
  get amount() {
    return this._amount;
  }
  set amount(newAmount) {
    if (tyoeof newAmount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    this._amount = newAmount;
  }
  get currency() {
    return this._currency;
  }
  set currency(newCUrrency) {
    if (!(newCurrency instanceof Currency)) {
      throw new TypeError('Currency must be a Currancy instance');
    }
    this._currency = newCurrency;
  }
  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this.currency.code})`;
  }
  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('Both amount and conversionRate must be numbers');
    }
    return amount * conversionRate;
  }
}
