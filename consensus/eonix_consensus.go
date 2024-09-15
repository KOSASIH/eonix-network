package consensus

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"math/big"
	"sync"
	"time"

	"github.com/eonix-project/eonix-network/blockchain"
	"github.com/eonix-project/eonix-network/crypto"
	"github.com/eonix-project/eonix-network/network"
)

// EonixConsensus represents the Eonix consensus algorithm
type EonixConsensus struct {
	// Blockchain instance
	blockchain *blockchain.Blockchain
	// Network instance
	network *network.Network
	// Crypto instance
	crypto *crypto.Crypto
	// Validator set
	validators []*Validator
	// Current block
	currentBlock *blockchain.Block
	// Lock for concurrent access
	lock sync.RWMutex
}

// NewEonixConsensus creates a new Eonix consensus instance
func NewEonixConsensus(blockchain *blockchain.Blockchain, network *network.Network, crypto *crypto.Crypto) *EonixConsensus {
	return &EonixConsensus{
		blockchain: blockchain,
		network:    network,
		crypto:     crypto,
		validators: make([]*Validator, 0),
	}
}

// AddValidator adds a new validator to the consensus algorithm
func (ec *EonixConsensus) AddValidator(validator *Validator) {
	ec.lock.Lock()
	defer ec.lock.Unlock()
	ec.validators = append(ec.validators, validator)
}

// RemoveValidator removes a validator from the consensus algorithm
func (ec *EonixConsensus) RemoveValidator(validator *Validator) {
	ec.lock.Lock()
	defer ec.lock.Unlock()
	for i, v := range ec.validators {
		if v.Equal(validator) {
			ec.validators = append(ec.validators[:i], ec.validators[i+1:]...)
			return
		}
	}
}

// CreateNewBlock creates a new block and adds it to the blockchain
func (ec *EonixConsensus) CreateNewBlock(transactions []*blockchain.Transaction) (*blockchain.Block, error) {
	// Create a new block with the given transactions
	block := blockchain.NewBlock(transactions)
	// Calculate the block hash
	blockHash := ec.calculateBlockHash(block)
	// Sign the block with the validator's private key
	signature, err := ec.crypto.Sign(blockHash, ec.validators[0].PrivateKey)
	if err != nil {
		return nil, err
	}
	// Add the signature to the block
	block.Signature = signature
	// Add the block to the blockchain
	ec.blockchain.AddBlock(block)
	return block, nil
}

// calculateBlockHash calculates the hash of a block
func (ec *EonixConsensus) calculateBlockHash(block *blockchain.Block) []byte {
	hash := sha256.New()
	hash.Write(block.PrevBlockHash)
	hash.Write(block.TransactionsHash)
	hash.Write(block.Timestamp)
	hash.Write(block.Nonce)
	return hash.Sum(nil)
}

// VerifyBlock verifies a block and its signature
func (ec *EonixConsensus) VerifyBlock(block *blockchain.Block) bool {
	// Calculate the block hash
	blockHash := ec.calculateBlockHash(block)
	// Verify the signature
	return ec.crypto.Verify(blockHash, block.Signature, ec.validators[0].PublicKey)
}

// StartConsensus starts the consensus algorithm
func (ec *EonixConsensus) StartConsensus() {
	go func() {
		for {
			// Get the current block
			ec.lock.RLock()
			currentBlock := ec.currentBlock
			ec.lock.RUnlock()
			// Create a new block if the current block is old
			if currentBlock == nil || time.Since(currentBlock.Timestamp) > 10*time.Second {
				transactions := ec.network.GetTransactions()
				block, err := ec.CreateNewBlock(transactions)
				if err != nil {
					fmt.Println(err)
					continue
				}
				ec.lock.Lock()
				ec.currentBlock = block
				ec.lock.Unlock()
			}
			// Sleep for 1 second
			time.Sleep(1 * time.Second)
		}
	}()
}

// Validator represents a validator in the consensus algorithm
type Validator struct {
	PublicKey  []byte
	PrivateKey []byte
}

// Equal checks if two validators are equal
func (v *Validator) Equal(other *Validator) bool {
	return bytes.Equal(v.PublicKey, other.PublicKey) && bytes.Equal(v.PrivateKey, other.PrivateKey)
}
