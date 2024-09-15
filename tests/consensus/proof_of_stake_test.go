package consensus

import (
	"testing"
)

 func TestProofOfStake(t *testing.T) {
	// Create a new validator
	validator, err := NewValidator()
	if err != nil {
		t.Fatal(err)
	}

	// Create a new blockchain
	blockchain, err := NewBlockchain()
	if err != nil {
		t.Fatal(err)
	}

	// Create a new block
	block, err := NewBlock(validator, blockchain)
	if err != nil {
		t.Fatal(err)
	}

	// Test the proof of stake algorithm
	proof, err := block.ProofOfStake()
	if err != nil {
		t.Fatal(err)
	}

	// Verify the proof
	if !proof.Verify() {
		t.Fatal("proof verification failed")
	}
}
