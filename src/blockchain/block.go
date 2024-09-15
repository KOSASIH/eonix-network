package blockchain

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"time"
)

// Block represents a block in the blockchain
type Block struct {
	// Hash is the hash of the block
	Hash string
	// PreviousHash is the hash of the previous block
	PreviousHash string
	// Timestamp is the timestamp of the block
	Timestamp time.Time
	// Validator is the validator who created the block
	Validator *Validator
	// Transactions is a list of transactions in the block
	Transactions []*Transaction
	// Signature is the signature of the block
	Signature string
}

// NewBlock creates a new block
func NewBlock(previousHash string, validator *Validator, transactions []*Transaction) *Block {
	block := &Block{
		PreviousHash: previousHash,
		Timestamp:    time.Now(),
		Validator:    validator,
		Transactions: transactions,
	}
	block.Hash = block.calculateHash()
	return block
}

// calculateHash calculates the hash of the block
func (block *Block) calculateHash() string {
	hash := sha256.Sum256([]byte(block.PreviousHash + block.Timestamp.String() + block.Validator.Address + strings.Join(block.getTransactionHashes(), "")))
	return hex.EncodeToString(hash[:])
}

// getTransactionHashes gets the hashes of the transactions in the block
func (block *Block) getTransactionHashes() []string {
	hashes := []string{}
	for _, tx := range block.Transactions {
		hashes = append(hashes, tx.Hash)
	}
	return hashes
}
