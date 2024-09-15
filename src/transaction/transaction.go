package transaction

import (
	"crypto/rand"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
)

// Transaction represents a transaction
type Transaction struct {
	// Hash is the hash of the transaction
	Hash string
	// From is the sender's address
	From string
	// To is the recipient's address
	To string
	// Amount is the amount of tokens to be transferred
	Amount int
	// Timestamp is the timestamp of the transaction
	Timestamp time.Time
	// Signature is the signature of the transaction
	Signature string
}

// NewTransaction creates a new transaction
func NewTransaction(from, to string, amount int) *Transaction {
	tx := &Transaction{
		From:     from,
		To:       to,
		Amount:   amount,
		Timestamp: time.Now(),
	}
	tx.Hash = tx.calculateHash()
	return tx
}

// calculateHash calculates the hash of the transaction
func (tx *Transaction) calculateHash() string {
	hash := sha256.Sum256([]byte(tx.From + tx.To + fmt.Sprintf("%d", tx.Amount) + tx.Timestamp.String()))
	return hex.EncodeToString(hash[:])
}
