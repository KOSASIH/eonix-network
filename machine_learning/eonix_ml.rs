extern crate linfa;
extern crate ndarray;
extern crate rand;

use linfa::prelude::*;
use ndarray::{Array, ArrayView};
use rand::Rng;

struct EonixML {
    model: linfa::clustering::KMeans,
}

impl EonixML {
    fn new() -> Self {
        EonixML {
            model: linfa::clustering::KMeans::new(3, 10),
        }
    }

    fn load_data(&mut self, file_path: &str) -> Result<(), Box<dyn std::error::Error>> {
        let data = ndarray::io::csv::CsvReader::from_path(file_path)?.into_array();
        self.model.fit(&data)?;
        Ok(())
    }

    fn predict(&self, data: &ArrayView<f64>) -> Array<f64> {
        self.model.predict(data)
    }

    fn save_model(&self, file_path: &str) -> Result<(), Box<dyn std::error::Error>> {
        self.model.save(file_path)?;
        Ok(())
    }

    fn load_model(&mut self, file_path: &str) -> Result<(), Box<dyn std::error::Error>> {
        self.model.load(file_path)?;
        Ok(())
    }
}

fn main() {
    let mut eonix_ml = EonixML::new();
    eonix_ml.load_data("data.csv").unwrap();
    let data = ndarray::array![1., 2., 3., 4., 5., 6.];
    let predictions = eonix_ml.predict(&data.view());
    println!("Predictions: {:?}", predictions);
    eonix_ml.save_model("eonix_ml_model.bin").unwrap();
}
