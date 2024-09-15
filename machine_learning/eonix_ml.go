package main

import (
	"fmt"
	"log"

	"github.com/chewxy/gorgonia"
	"github.com/chewxy/gorgonia/tensor"
)

type EonixML struct {
	model *gorgonia.Executable
}

func NewEonixML() *EonixML {
	return &EonixML{}
}

func (e *EonixML) LoadData(file_path string) error {
	// Load data from file
	data, err := LoadDataFromFile(file_path)
	if err != nil {
		return err
	}

	// Create a new Gorgonia tensor from the data
	t := tensor.New(tensor.WithShape(2, 3), tensor.WithBacking(data))

	// Create a new Gorgonia graph
	g := gorgonia.NewGraph()

	// Create a new Gorgonia node for the input data
	inputNode := gorgonia.NewNode(g, "input", t, gorgonia.WithName("input"))

	// Create a new Gorgonia node for the output data
	outputNode := gorgonia.NewNode(g, "output", t, gorgonia.WithName("output"))

	// Create a new Gorgonia node for the model
	modelNode := gorgonia.NewNode(g, "model", t, gorgonia.WithName("model"))

	// Create a new Gorgonia executable from the graph
	e.model, err = gorgonia.NewExecutable(g, gorgonia.BindDualValues(inputNode, outputNode, modelNode))
	if err != nil {
		return err
	}

	return nil
}

func (e *EonixML) Predict(data []float64) ([]float64, error) {
	// Create a new Gorgonia tensor from the input data
	t := tensor.New(tensor.WithShape(2, 3), tensor.WithBacking(data))

	// Run the model on the input data
	output, err := e.model.Run(map[string]tensor.Tensor{"input": t})
	if err != nil {
		return nil, err
	}

	// Get the output data from the tensor
	outputData := output["output"].Data()

	return outputData, nil
}

func (e *EonixML) SaveModel(file_path string) error {
	// Save the model to a file
	err := e.model.Save(file_path)
	if err != nil {
		return err
	}

	return nil
}

func (e *EonixML) LoadModel(file_path string) error {
	// Load the model from a file
	err := e.model.Load(file_path)
	if err != nil {
		return err
	}

	return nil
}

func main() {
	e := NewEonixML()
	err := e.LoadData("data.csv")
	if err != nil {
		log.Fatal(err)
	}

	data := []float64{1, 2, 3, 4, 5, 6}
	predictions, err := e.Predict(data)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Predictions:", predictions)

	err = e.SaveModel("eonix_ml_model.bin")
	if err != nil {
		log.Fatal(err)
	}
}
