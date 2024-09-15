package peer

import (
	"fmt"
	"net"
)

// Peer represents a peer in the network
type Peer struct {
	// Address is the peer's address
	Address net.Addr
	// Connection is the peer's connection
	Connection net.Conn
}

// NewPeer creates a new peer
func NewPeer(address net.Addr, connection net.Conn) *Peer {
	return &Peer{
		Address:    address,
		Connection: connection,
	}
}

// Send sends a message to the peer
func (p *Peer) Send(message []byte) error {
	_, err := p.Connection.Write(message)
	return err
}

// Equal checks if two peers are equal
func (p *Peer) Equal(other *Peer) bool {
	return p.Address.String() == other.Address.String()
}
