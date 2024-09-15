package network

import (
	"testing"
	"net"
)

func TestNetwork(t *testing.T) {
	// Create a new network
	network, err := NewNetwork()
	if err != nil {
		t.Fatal(err)
	}

	// Create a new peer
	peer, err := NewPeer(nil, nil)
	if err != nil {
		t.Fatal(err)
	}

	// Add the peer to the network
	err = network.AddPeer(peer)
	if err != nil {
		t.Fatal(err)
	}

	// Test the network's peers
	peers := network.Peers()
	if len(peers) != 1 {
		t.Fatal("network should have one peer")
	}

	// Test the network's broadcast function
	err = network.Broadcast([]byte("hello"))
	if err != nil {
		t.Fatal(err)
	}
}
