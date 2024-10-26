import keras
from src.Tuner import Tuner
from typing import List, Dict


class ModelCreator(Tuner):
    def __init__ (self,
                  stock_symbol: str,
                  fmt: str,
                  intervals: List[str],
                  max_trials: int = 10,
                  executions_per_trial: int = 3,
                  directory: str = "tuning_histories",
                  ) -> None:
        
        super().__init__(fmt,
                         max_trials,
                         executions_per_trial,
                         directory)
        
        self.stock_symbol = stock_symbol
        self.intervals = intervals
        self.models = None
    
    def train_tune (self,
                    epochs: int = 10,
                    batch_size: int = 32,
                    metric: str = "val_loss",
                    plot: bool = False,
                    verbose: bool = True) -> Dict[str, keras.Model]:
        
        models: Dict[str, keras.Model] = {}
        for interval in self.intervals:
            model_name: str = f"{interval}_{self.stock_symbol}_model"
            print(f"Tuning for interval: {interval}")
            
            models[model_name] = self.__tune(self.stock_symbol,
                                           interval,
                                           epochs,
                                           batch_size,
                                           metric,
                                           plot,
                                           verbose)
        
        self.models = models
        return models