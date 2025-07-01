"""
You're absolutely right — training_pipeline.py is not strictly required for your project to run predictions via Flask.
✅ When training_pipeline.py is not required:
You've already trained your model.
Your model (model.pkl) and preprocessor (preprocessor.pkl) are saved inside the artifacts/ folder.
Your Flask app is purely used for inference (prediction).

🔄 So when is training_pipeline.py helpful?
When you want to retrain your model from scratch automatically (e.g., on new data).
During experimentation, testing model performance with new features or hyperparameters.
In production, if you build an automated training pipeline (e.g., scheduled daily retraining).
"""