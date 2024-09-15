package eonix

import (
	"crypto/ecdsa"
	"crypto/rand"
	"encoding/hex"
	"fmt"
	"math/big"
)

// GenerateKeyPair generates a new ECDSA key pair
func GenerateKeyPair() (*ecdsa.PrivateKey, *ecdsa.PublicKey, error) {
	privateKey, err := ecdsa.GenerateKey(ecdsa.S256(), rand.Reader)
	if err != nil {
		return nil, nil, err
	}
	publicKey := privateKey.Public()
	return privateKey, publicKey.(*ecdsa.PublicKey), nil
}

// GetAddressFromPublicKey returns the Ethereum address from a public key
func GetAddressFromPublicKey(publicKey *ecdsa.PublicKey) (string, error) {
	publicKeyBytes := elliptic.Marshal(publicKey, publicKey.X, publicKey.Y)
	hash := sha3.New256()
	hash.Write(publicKeyBytes[1:])
	address := hex.EncodeToString(hash.Sum(nil)[12:])
	return "0x" + address, nil
}

// GetAddressFromPrivateKey returns the Ethereum address from a private key
func GetAddressFromPrivateKey(privateKey *ecdsa.PrivateKey) (string, error) {
	publicKey := privateKey.Public()
	return GetAddressFromPublicKey(publicKey.(*ecdsa.PublicKey))
}

// Sign signs a message with a private key
func Sign(privateKey *ecdsa.PrivateKey, message []byte) ([]byte, error) {
	hash := sha3.New256()
	hash.Write(message)
	hashedMessage := hash.Sum(nil)
	signature, err := ecdsa.Sign(rand.Reader, privateKey, hashedMessage)
	if err != nil {
		return nil, err
	}
	return signature, nil
}

// Verify verifies a signature with a public key
func Verify(publicKey *ecdsa.PublicKey, message []byte, signature []byte) bool {
	hash := sha3.New256()
	hash.Write(message)
	hashedMessage := hash.Sum(nil)
	return ecdsa.Verify(publicKey, hashedMessage, signature)
}
