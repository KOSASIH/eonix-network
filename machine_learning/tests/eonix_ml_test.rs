use eonix_ml::{EonixML, Model};
use std::fs;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_load_data() {
        let mut eonix_ml = EonixML::new();
        eonix_ml.load_data("data.csv").unwrap();
        assert!(eonix_ml.model.is_some());
    }

    #[test]
    fn test_predict() {
        let mut eonix_ml = EonixML::new();
        eonix_ml.load_data("data.csv").unwrap();
        let data = vec![1., 2., 3., 4., 5., 6.];
        let predictions = eonix_ml.predict(data);
        assert_eq!(predictions.len(), 6);
    }

    #[test]
    fn test_save_model() {
        let mut eonix_ml = EonixML::new();
        eonix_ml.load_data("data.csv").unwrap();
        eonix_ml.save_model("eonix_ml_model.bin").unwrap();
        assert!(fs::metadata("eonix_ml_model.bin").is_ok());
    }

    #[test]
    fn test_load_model() {
        let mut eonix_ml = EonixML::new();
        eonix_ml.load_model("eonix_ml_model.bin").unwrap();
        assert!(eonix_ml.model.is_some());
    }
}
