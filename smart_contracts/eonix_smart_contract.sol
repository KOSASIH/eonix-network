pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/Address.sol";

contract EonixSmartContract {
    using SafeERC20 for address;
    using SafeMath for uint256;
    using Address for address;

    // Mapping of user balances
    mapping (address => uint256) public balances;

    // Mapping of allowances
    mapping (address => mapping (address => uint256)) public allowances;

    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event emitted when an allowance is approved
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Event emitted when a token is burned
    event Burn(address indexed owner, uint256 value);

    // Event emitted when a token is minted
    event Mint(address indexed owner, uint256 value);

    // Owner of the contract
    address private owner;

    // Total supply of tokens
    uint256 public totalSupply;

    // Token name
    string public name;

    // Token symbol
    string public symbol;

    // Token decimals
    uint8 public decimals;

    // Mapping of token holders
    mapping (address => bool) public tokenHolders;

    // Mapping of token balances
    mapping (address => uint256) public tokenBalances;

    // Mapping of token allowances
    mapping (address => mapping (address => uint256)) public tokenAllowances;

    // Constructor function
    constructor() public {
        owner = msg.sender;
        totalSupply = 100000000 * (10 ** uint256(decimals));
        name = "Eonix Token";
        symbol = "EON";
        decimals = 18;
    }

    // Function to transfer tokens
    function transfer(address recipient, uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(amount);
        balances[recipient] = balances[recipient].add(amount);
        emit Transfer(msg.sender, recipient, amount);
    }

    // Function to approve an allowance
    function approve(address spender, uint256 amount) public {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
    }

    // Function to transfer tokens from another address
    function transferFrom(address sender, address recipient, uint256 amount) public {
        require(allowances[sender][msg.sender] >= amount, "Insufficient allowance");
        require(balances[sender] >= amount, "Insufficient balance");
        balances[sender] = balances[sender].sub(amount);
        balances[recipient] = balances[recipient].add(amount);
        emit Transfer(sender, recipient, amount);
    }

    // Function to burn tokens
    function burn(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(amount);
        totalSupply = totalSupply.sub(amount);
        emit Burn(msg.sender, amount);
    }

    // Function to mint tokens
    function mint(address recipient, uint256 amount) public {
        require(msg.sender == owner, "Only the owner can mint tokens");
        totalSupply = totalSupply.add(amount);
        balances[recipient] = balances[recipient].add(amount);
        emit Mint(recipient, amount);
    }

    // Function to get the balance of a user
    function balanceOf(address user) public view returns (uint256) {
        return balances[user];
    }

    // Function to get the allowance of a user
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    // Function to get the total supply of tokens
    function totalSupply() public view returns (uint256) {
        return totalSupply;
    }
}
