# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import SlotSet, EventType, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

import pandas as pd
from actions import SGBD

sgbd = SGBD.mySGBD()

class ValidateProductForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_product_form"

    def validate_product_category(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `product_category` value."""

        if slot_value.lower() not in sgbd.allowed_categories:
            dispatcher.utter_message(text=f"We only accept those categories: {', '.join(sgbd.allowed_categories)}.")
            return {"product_category": None}
        dispatcher.utter_message(text=f"We have in {slot_value} category those RAMs: {', '.join(sgbd.get_RAM_by_category(slot_value))}.")
        return {"product_category": slot_value}

    def validate_product_RAM(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `product_RAM` value."""
        
        if slot_value not in sgbd.allowed_RAMs:
            dispatcher.utter_message(text=f"We don't have this in store. Please choose between: {', '.join(sgbd.allowed_RAMs)}.")
            return {"product_RAM": None}
        dispatcher.utter_message(text=f"You want to have {slot_value} in RAM. We have those processors: {', '.join(sgbd.get_processor_by_RAM(slot_value))}")
        return {"product_RAM": slot_value}
    
    def validate_product_processor(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `product_processor` value."""

        if slot_value not in sgbd.allowed_processors:
            dispatcher.utter_message(text=f"We only have thoses processors: {', '.join(sgbd.allowed_processors)}.")
            return {"product_processor": None}
        dispatcher.utter_message(text=f"You want to have the {slot_value} processor. We have those capacities in stock: {', '.join(sgbd.get_storage_capacity_by_processor(slot_value))}.")
        return {"product_processor": slot_value}
    
    def validate_product_storage_capacity(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `product_storage_capacity` value."""

        if slot_value not in sgbd.allowed_storage_capacities:
            dispatcher.utter_message(text=f"We only have thoses storage capacities: {', '.join(sgbd.allowed_storage_capacities)}.")
            return {"product_storage_capacity": None}
        
        message = ""
        brand_price_list = sgbd.get_brand_by_storage_capacity(slot_value)
        for brand_price in brand_price_list:
            brand = brand_price[0]
            price = brand_price[1]
            text = f"{brand}: {price}"
            message += text + ', '

        dispatcher.utter_message(text=f"You want to have the {slot_value} storage capacity. We have those brands in stock: {message}.")
        return {"product_storage_capacity": slot_value}
    
    def validate_product_brand(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `product_brand` value."""

        if slot_value not in sgbd.allowed_brands:
            dispatcher.utter_message(text=f"We only have thoses brands: {', '.join(sgbd.allowed_brands)}.")
            return {"product_brand": None}
        dispatcher.utter_message(text=f"You want to have {slot_value}. We have {', '.join(sgbd.get_product_quantity_by_brand(slot_value))} from this.")
        return {"product_brand": slot_value}
        
    def validate_product_quantity(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `product_quantity` value."""
        
        if int(slot_value) < 1 or int(slot_value) > sgbd.allowed_quantity:
            dispatcher.utter_message(text=f"We only have {sgbd.allowed_quantity} from this product.")
            return {"product_quantity": None}
        dispatcher.utter_message(text=f"OK! You want to have {slot_value} from this product.")
        return {"product_quantity": slot_value}
    
class SubmitProductForm(Action):
    def name(self) -> Text:
        return "action_submit_product_form"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[Dict[Text, Any]]:
        """Submit the order and update the quantity of the ordered product."""
        # submit the order

        ordered_quantity = tracker.get_slot("product_quantity")
        sgbd.update_quantity(ordered_quantity)
        dispatcher.utter_message(text="Your order has been successfully placed.")
        return []

class ResetProductForm(Action):
    def name(slef):
        return "action_reset_product_form"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ):
        """Reset `product form` values."""

        slots = ["product_category", "product_RAM", "product_processor", "product_storage_capacity", "product_brand", "product_quantity"]
        return [SlotSet(slot, None) for slot in slots]