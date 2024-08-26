from abc import ABC, abstractmethod


class GDFTRepository(ABC):
    @abstractmethod
    def acquireTokenFromPretrainedModel(self):
        pass

    @abstractmethod
    def acquireModelFromPretrainedModel(self):
        pass

    @abstractmethod
    def configDataCollator(self, tokenizer):
        pass

    @abstractmethod
    def configTrainingParameter(self):
        pass

    @abstractmethod
    def configTrainer(self, model, traininigParameter, needToTrainDataset, tokenizer):
        pass

    @abstractmethod
    def trainFineTuning(self, trainer):
        pass

    @abstractmethod
    def encodeTokenizer(self, tokenizer, text):
        pass

    @abstractmethod
    def generateText(self, model, inputIds):
        pass

    @abstractmethod
    def decodeTokenizer(self, tokenizer, output):
        pass