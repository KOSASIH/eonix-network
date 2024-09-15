package blockchain

import (
	"testing"
)

func TestBlock(t *testing.T) {
	// Create a new blockchain
	blockchain, err := NewBlockchain()
	if err != nil {
		t.Fatal(err)
	}

	// Create a new block
	block, err := NewBlock(nil, blockchain)
	if err != nil {
		t.Fatal(err)
	}

	// Test the block's hash
	hash := block.Hash()
	if len(hash) != 64 {
		t.Fatal("invalid block hash")
	}

	// Test the block's transactions
	transactions := block.Transactions()
	if len(transactions) != 0 {
		t.Fatal("block should have no transactions")
	}
}
