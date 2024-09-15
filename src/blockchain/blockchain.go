package blockchain

import (
	"fmt"
	"sync"
)

// Blockchain represents a blockchain instance
type Blockchain struct {
	// Blocks is a list of blocks in the blockchain
	Blocks []*Block
	// Validators is a list of validators in the blockchain
	Validators []*Validator
	// Mutex is a mutex for concurrent access
	Mutex sync.RWMutex
}

// NewBlockchain creates a new blockchain instance
func NewBlockchain() *Blockchain {
	return &Blockchain{
		Blocks:    []*Block{},
		Validators: []*Validator{},
	}
}

// AddBlock adds a block to the blockchain
func (bc *Blockchain) AddBlock(block *Block) error {
	bc.Mutex.Lock()
	defer bc.Mutex.Unlock()
	// Check if the block is valid
	if !bc.IsValidBlock(block) {
		return fmt.Errorf("invalid block")
	}
	// Add the block to the blockchain
	bc.Blocks = append(bc.Blocks, block)
	return nil
}

// IsValidBlock checks if a block is valid
func (bc *Blockchain) IsValidBlock(block *Block) bool {
	// Check if the block's previous hash matches the last block's hash
	if len(bc.Blocks) > 0 && block.PreviousHash != bc.Blocks[len(bc.Blocks)-1].Hash {
		return false
	}
	// Check if the block's timestamp is newer than the last block's timestamp
	if len(bc.Blocks) > 0 && block.Timestamp.Before(bc.Blocks[len(bc.Blocks)-1].Timestamp) {
		return false
	}
	return true
}

// GetPublicKey gets a validator's public key
func (bc *Blockchain) GetPublicKey(address string) ([]byte, error) {
	for _, v := range bc.Validators {
		if v.Address == address {
			return v.PublicKey, nil
		}
	}
	return nil, fmt.Errorf("validator not found")
}
