package validator

import (
	"testing"
)

func TestValidator(t *testing.T) {
	// Create a new validator
	validator, err := NewValidator()
	if err != nil {
		t.Fatal(err)
	}

	// Test the validator's address
	address := validator.Address()
	if len(address) != 40 {
		t.Fatal("invalid validator address")
	}

	// Test the validator's public key
	publicKey := validator.PublicKey()
	if len(publicKey) != 64 {
		t.Fatal("invalid validator public key")
	}

	// Test the validator's sign function
	message := []byte("hello")
	signature, err := validator.Sign(message)
	if err != nil {
		t.Fatal(err)
	}

	// Verify the signature
	if !validator.Verify(message, signature) {
		t.Fatal("signature verification failed")
	}
}
