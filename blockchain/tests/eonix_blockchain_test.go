package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestNewEonixBlockchain(t *testing.T) {
	bc := NewEonixBlockchain()
	assert.NotNil(t, bc)
	assert.NotNil(t, bc.db)
	assert.Empty(t, bc.chain)
}

func TestGenesisBlock(t *testing.T) {
	bc := NewEonixBlockchain()
	genesis := bc.GenesisBlock()
	assert.NotNil(t, genesis)
	assert.Equal(t, 0, genesis.Index)
	assert.Equal(t, "0", genesis.PreviousHash)
	assert.Equal(t, int64(1643723400), genesis.Timestamp)
	assert.Empty(t, genesis.Transactions)
}

func TestAddBlock(t *testing.T) {
	bc := NewEonixBlockchain()
	genesis := bc.GenesisBlock()
	bc.AddBlock(genesis)
	assert.Len(t, bc.chain, 1)
	assert.Equal(t, genesis, bc.chain[0])
}

func TestGetBlock(t *testing.T) {
	bc := NewEonixBlockchain()
	genesis := bc.GenesisBlock()
	bc.AddBlock(genesis)
	block, err := bc.GetBlock(0)
	assert.Nil(t, err)
	assert.Equal(t, genesis, block)
}

func TestTransaction(t *testing.T) {
	tx := Transaction{
		ID:        "tx1",
		Timestamp: 1643723400,
		Sender:    "sender1",
		Recipient: "recipient1",
		Amount:    10.0,
	}
	assert.NotNil(t, tx)
}

func TestBlock(t *testing.T) {
	block := Block{
		Index:        1,
		PreviousHash: "prev_hash",
		Timestamp:    1643723401,
		Transactions: []Transaction{},
	}
	assert.NotNil(t, block)
}

func main() {
}
