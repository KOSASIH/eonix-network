package eonixconsensus

import (
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
)

func TestEonixConsensus_AddValidator(t *testing.T) {
	consensus := NewEonixConsensus(nil, nil, nil)
	validator := NewValidator("public_key", "private_key")
	consensus.AddValidator(validator)
	assert.Len(t, consensus.validators, 1)
}

func TestEonixConsensus_RemoveValidator(t *testing.T) {
	consensus := NewEonixConsensus(nil, nil, nil)
	validator := NewValidator("public_key", "private_key")
	consensus.AddValidator(validator)
	consensus.RemoveValidator("public_key")
	assert.Len(t, consensus.validators, 0)
}

func TestEonixConsensus_CreateNewBlock(t *testing.T) {
	consensus := NewEonixConsensus(nil, nil, nil)
	transactions := []Transaction{{}, {}}
	block, err := consensus.CreateNewBlock(transactions)
	assert.Nil(t, err)
	assert.NotNil(t, block)
}

func TestEonixConsensus_VerifyBlock(t *testing.T) {
	consensus := NewEonixConsensus(nil, nil, nil)
	block := Block{transactions: []Transaction{{}, {}}}
	signature, err := consensus.crypto.Sign(block.Hash(), "private_key")
	assert.Nil(t, err)
	block.Signature = signature
	assert.True(t, consensus.VerifyBlock(&block))
}

func TestEonixConsensus_StartConsensus(t *testing.T) {
	consensus := NewEonixConsensus(nil, nil, nil)
	go consensus.StartConsensus()
	time.Sleep(2 * time.Second)
	assert.NotNil(t, consensus.currentBlock)
}

func BenchmarkEonixConsensus_CreateNewBlock(b *testing.B) {
	consensus := NewEonixConsensus(nil, nil, nil)
	transactions := make([]Transaction, 100)
	for i := 0; i < 100; i++ {
		transactions[i] = Transaction{}
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_, err := consensus.CreateNewBlock(transactions)
		if err != nil {
			b.Fatal(err)
		}
	}
}
