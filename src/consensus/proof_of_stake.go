package consensus

import (
	"crypto/rand"
	 "crypto/sha256"
	"encoding/hex"
	"fmt"
	"math/big"
	"time"
)

// ProofOfStake represents a proof of stake consensus algorithm
type ProofOfStake struct {
	// Blockchain is the blockchain instance
	Blockchain *Blockchain
	// Validators is a list of validators
	Validators []*Validator
}

// NewProofOfStake creates a new proof of stake instance
func NewProofOfStake(blockchain *Blockchain) *ProofOfStake {
	return &ProofOfStake{
		Blockchain: blockchain,
		Validators: []*Validator{},
	}
}

// Validate validates a block
func (pos *ProofOfStake) Validate(block *Block) error {
	// Check if the block is valid
	if !pos.Blockchain.IsValidBlock(block) {
		return fmt.Errorf("invalid block")
	}
	// Check if the validator is authorized
	if !pos.IsAuthorizedValidator(block.Validator) {
		return fmt.Errorf("unauthorized validator")
	}
	// Check if the block is signed correctly
	if !pos.IsSignedCorrectly(block) {
		return fmt.Errorf("invalid signature")
	}
	return nil
}

// IsAuthorizedValidator checks if a validator is authorized
func (pos *ProofOfStake) IsAuthorizedValidator(validator *Validator) bool {
	// Check if the validator is in the list of validators
	for _, v := range pos.Validators {
		if v.Equal(validator) {
			return true
		}
	}
	return false
}

// IsSignedCorrectly checks if a block is signed correctly
func (pos *ProofOfStake) IsSignedCorrectly(block *Block) bool {
	// Get the validator's public key
	pubKey, err := pos.Blockchain.GetPublicKey(block.Validator.Address)
	if err != nil {
		return false
	}
	// Verify the signature
	sig, err := hex.DecodeString(block.Signature)
	if err != nil {
		return false
	}
	hash := sha256.Sum256(block.Hash())
	if !ecdsa.Verify(pubKey, hash[:], sig) {
		return false
	}
	return true
}
