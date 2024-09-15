pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/test/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/test/ERC20.sol";
import "./eonix_smart_contracts.sol";

contract EonixSmartContractTest {
    EonixSmartContract public eonix;

    constructor() public {
        eonix = new EonixSmartContract();
    }

    function testTransfer() public {
        address sender = address(0x1);
        address recipient = address(0x2);
        uint256 amount = 100;

        eonix.transfer(sender, recipient, amount);

        assert(eonix.balanceOf(sender) == 0);
        assert(eonix.balanceOf(recipient) == amount);
    }

    function testApprove() public {
        address owner = address(0x1);
        address spender = address(0x2);
        uint256 amount = 100;

        eonix.approve(owner, spender, amount);

        assert(eonix.allowance(owner, spender) == amount);
    }

    function testTransferFrom() public {
        address sender = address(0x1);
        address recipient = address(0x2);
        uint256 amount = 100;

        eonix.approve(sender, address(this), amount);
        eonix.transferFrom(sender, recipient, amount);

        assert(eonix.balanceOf(sender) == 0);
        assert(eonix.balanceOf(recipient) == amount);
    }

    function testBurn() public {
        address owner = address(0x1);
        uint256 amount = 100;

        eonix.burn(owner, amount);

        assert(eonix.balanceOf(owner) == 0);
        assert(eonix.totalSupply() == 0);
    }

    function testMint() public {
        address recipient = address(0x1);
        uint256 amount = 100;

        eonix.mint(recipient, amount);

        assert(eonix.balanceOf(recipient) == amount);
        assert(eonix.totalSupply() == amount);
    }
}
