package validator

import (
	"crypto/ecdsa"
	"crypto/rand"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
)

// Validator represents a validator
type Validator struct {
	// Address is the validator's address
	Address string
	// PublicKey is the validator's public key
	PublicKey []byte
	// PrivateKey is the validator's private key
	PrivateKey *ecdsa.PrivateKey
}

// NewValidator creates a new validator
func NewValidator() (*Validator, error) {
	privateKey, err := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
	if err != nil {
		return nil, err
	}
	publicKey := privateKey.Public().(*ecdsa.PublicKey)
	address := fmt.Sprintf("%x", sha256.Sum256(publicKey.X.Bytes())[0:20])
	return &Validator{
		Address:    address,
		PublicKey:  publicKey.X.Bytes(),
		PrivateKey: privateKey,
	}, nil
}

// Sign signs a message with the validator's private key
func (v *Validator) Sign(message []byte) (string, error) {
	hash := sha256.Sum256(message)
	sig, err := ecdsa.Sign(rand.Reader, v.PrivateKey, hash[:])
	if err != nil {
		return "", err
	}
	return hex.EncodeToString(sig), nil
}

// Equal checks if two validators are equal
func (v *Validator) Equal(other *Validator) bool {
	return v.Address == other.Address
}
