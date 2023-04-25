# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionReceiveAccountNumber(Action):

    def name(self) -> Text:
        return "action_receive_account_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"I'll remember your account number which is : {text}!")
        return [SlotSet("account_number", text)]

class ActionReceiveName(Action):

    def name(self) -> Text:
        return "action_receive_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"I'll remember your name {text}!")
        return [SlotSet("name", text)]

class ActionReceivePhoneNumber(Action):

    def name(self) -> Text:
        return "action_receive_phone_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"I'll remember your phone number, {text}!")
        return [SlotSet("phone_number", text)]


class ActionSayNameAccountNumPhoneNum(Action):

    def name(self) -> Text:
        return "action_say_name_account_num_phone_num"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        account_number = tracker.get_slot("account_number")
        name = tracker.get_slot("name")
        phone_number = tracker.get_slot("phone_number")

        if not name:
            dispatcher.utter_message(text="Sorry But you haven't provided details.")
        else:
            dispatcher.utter_message(text=f"Your name is {name}! Your account number is: {account_number}. And your phone number is: {phone_number}")
        return []