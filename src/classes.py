from abc import ABC, abstractmethod

import requests
import json
import os

class Parser(ABC):
    "Абстрактый класс"
    @abstractmethod
    def get_request(self):
        pass

    @abstractmethod
    def get_info(self):
        pass
