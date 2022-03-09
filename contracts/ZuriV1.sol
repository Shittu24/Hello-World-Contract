// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract HelloWorld {
    uint256 number;
    address public owner;
    event NumberChanged(uint256 newNumber);

    constructor() {
        owner = msg.sender;
    }

    function store(uint256 newNumber) public {
        number = newNumber;
        emit NumberChanged(newNumber);
    }

    function retrieve() public view returns(uint256) {
       return number;
    }

    function increment() public {
        number = number + 4;
        emit NumberChanged(number);

    }

}