package eonix

import (
	"crypto/ecdsa"
	"encoding/hex"
	"fmt"
	"testing"
)

func TestGenerateKeyPair(t *testing.T) {
	privateKey, publicKey, err := GenerateKeyPair()
	if err != nil {
		t.Fatal(err)
	}
	if privateKey == nil || publicKey == nil {
		t.Fatal("Failed to generate key pair")
	}
}

func TestGetAddressFromPublicKey(t *testing.T) {
	privateKey, publicKey, err := GenerateKeyPair()
	if err != nil {
		t.Fatal(err)
	}
	address, err := GetAddressFromPublicKey(publicKey)
	if err != nil {
		t.Fatal(err)
	}
	if address == "" {
		t.Fatal("Failed to get address from public key")
	}
}

func TestGetAddressFromPrivateKey(t *testing.T) {
	privateKey, _, err := GenerateKeyPair()
	if err != nil {
		t.Fatal(err)
	}
	address, err := GetAddressFromPrivateKey(privateKey)
	if err != nil {
		t.Fatal(err)
	}
	if address == "" {
		t.Fatal("Failed to get address from private key")
	}
}

func TestSign(t *testing.T) {
	privateKey, _, err := GenerateKeyPair()
	if err != nil {
		t.Fatal(err)
	}
	message := []byte("Hello, World!")
	signature, err := Sign(privateKey, message)
	if err != nil {
		t.Fatal(err)
	}
	if signature == nil {
		t.Fatal("Failed to sign message")
	}
}

func TestVerify(t *testing.T) {
	privateKey, publicKey, err := GenerateKeyPair()
	if err != nil {
		t.Fatal(err)
	}
	message := []byte("Hello, World!")
	signature, err := Sign(privateKey, message)
	if err != nil {
		t.Fatal(err)
	}
	if !Verify(publicKey, message, signature) {
		t.Fatal("Failed to verify signature")
	}
}
