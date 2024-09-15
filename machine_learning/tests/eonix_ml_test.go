package eonix_ml

import (
	"testing"
	"os"
)

func TestLoadData(t *testing.T) {
	eonixML := NewEonixML()
	err := eonixML.LoadData("data.csv")
	if err != nil {
		t.Errorf("Failed to load data: %v", err)
	}
	if eonixML.model == nil {
		t.Errorf("Model is nil after loading data")
	}
}

func TestPredict(t *testing.T) {
	eonixML := NewEonixML()
	err := eonixML.LoadData("data.csv")
	if err != nil {
		t.Errorf("Failed to load data: %v", err)
	}
	data := []float64{1, 2, 3, 4, 5, 6}
	predictions, err := eonixML.Predict(data)
	if err != nil {
		t.Errorf("Failed to make predictions: %v", err)
	}
	if len(predictions) != 6 {
		t.Errorf("Expected 6 predictions, got %d", len(predictions))
	}
}

func TestSaveModel(t *testing.T) {
	eonixML := NewEonixML()
	err := eonixML.LoadData("data.csv")
	if err != nil {
		t.Errorf("Failed to load data: %v", err)
	}
	err = eonixML.SaveModel("eonix_ml_model.bin")
	if err != nil {
		t.Errorf("Failed to save model: %v", err)
	}
	if _, err := os.Stat("eonix_ml_model.bin"); os.IsNotExist(err) {
		t.Errorf("Model file does not exist")
	}
}

func TestLoadModel(t *testing.T) {
	eonixML := NewEonixML()
	err := eonixML.LoadModel("eonix_ml_model.bin")
	if err != nil {
		t.Errorf("Failed to load model: %v", err)
	}
	if eonixML.model == nil {
		t.Errorf("Model is nil after loading")
	}
}
