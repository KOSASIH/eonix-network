package network

import (
	"fmt"
	"net"
)

// Network represents a network instance
type Network struct {
	// Peers is a list of peers in the network
	Peers []*Peer
	// Mutex is a mutex for concurrent access
	Mutex sync.RWMutex
}

// NewNetwork creates a new network instance
func NewNetwork() *Network {
	return &Network{
		Peers: []*Peer{},
	}
}

// AddPeer adds a peer to the network
func (n *Network) AddPeer(peer *Peer) error {
	n.Mutex.Lock()
	defer n.Mutex.Unlock()
	// Check if the peer is already in the network
	for _, p := range n.Peers {
		if p.Equal(peer) {
			return fmt.Errorf("peer already in network")
		}
	}
	// Add the peer to the network
	n.Peers = append(n.Peers, peer)
	return nil
}

// Broadcast broadcasts a message to all peers in the network
func (n *Network) Broadcast(message []byte) error {
	n.Mutex.RLock()
	defer n.Mutex.RUnlock()
	for _, peer := range n.Peers {
		err := peer.Send(message)
		if err != nil {
			return err
		}
	}
	return nil
}
